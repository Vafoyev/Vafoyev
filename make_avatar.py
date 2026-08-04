# -*- coding: utf-8 -*-
"""
Rasmni neon pixel-art avatarga aylantiradi.

Kirish : img/photo.jpg  (yoki img/ ichidagi birinchi rasm)
Chiqish: avatar.png      (pikselli, dumaloq, shaffof fonli)

Sozlash: GRID (piksel o'lchami), CROP (qaysi joyni kesish), SAT/CON.
Ishlatish: python make_avatar.py
"""

import glob
import os

from PIL import Image, ImageEnhance

HERE = os.path.dirname(os.path.abspath(__file__))

GRID = 76          # pixel-art panjarasi (kichikroq = yirikroq piksel)
OUT_PX = 608       # chiqish o'lchami (GRID ning karrasi bo'lsin)
SAT = 1.38         # ranglar to'yinganligi
CON = 1.14         # kontrast
BRI = 1.06         # yorqinlik
POSTERIZE = 5      # rang bitlari (kamroq = ko'proq "retro")

# Rasm qiyshiq — yuzni tik holatga keltirish uchun burish (gradus, soat strelkasiga teskari)
ROTATE = -30.0

# Yuzni kesish oynasi: (markaz_x, markaz_y, tomon) — asl rasm piksellarida.
# Burish ham shu markaz atrofida bajariladi, shuning uchun markaz joyida qoladi.
CROP = (1165, 555, 880)

# Neon rang gradingi (soyalarga ko'k, yorug'likka och havorang qo'shadi)
SHADOW_TINT = (10, 40, 70)
LIGHT_TINT = (140, 235, 255)
TINT_STRENGTH = 0.16


def find_photo():
    for pat in ("img/*.jpg", "img/*.jpeg", "img/*.png", "img/*.webp"):
        hits = sorted(glob.glob(os.path.join(HERE, pat)))
        if hits:
            return hits[0]
    raise SystemExit("img/ papkasida rasm topilmadi")


def tint(im):
    """Soyalarni ko'kimtir, yorug' joylarni neon-havorang qiladi."""
    px = im.load()
    w, h = im.size
    s = TINT_STRENGTH
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            lum = (r * 299 + g * 587 + b * 114) / 255000.0  # 0..1
            tr = SHADOW_TINT[0] + (LIGHT_TINT[0] - SHADOW_TINT[0]) * lum
            tg = SHADOW_TINT[1] + (LIGHT_TINT[1] - SHADOW_TINT[1]) * lum
            tb = SHADOW_TINT[2] + (LIGHT_TINT[2] - SHADOW_TINT[2]) * lum
            px[x, y] = (
                int(r * (1 - s) + tr * s),
                int(g * (1 - s) + tg * s),
                int(b * (1 - s) + tb * s),
            )
    return im


def pixel_circle_mask(size):
    """Chekkasi ham pikselli dumaloq niqob (silliq emas — retro ko'rinish)."""
    m = Image.new("L", (size, size), 0)
    px = m.load()
    c = (size - 1) / 2.0
    r = size / 2.0 - 0.5
    for y in range(size):
        for x in range(size):
            if (x - c) ** 2 + (y - c) ** 2 <= r * r:
                px[x, y] = 255
    return m


def main():
    src = find_photo()
    im = Image.open(src).convert("RGB")
    W, H = im.size
    print("Manba: %s  (%dx%d)" % (os.path.basename(src), W, H))

    cx, cy, side = CROP
    if ROTATE:
        im = im.rotate(ROTATE, resample=Image.BICUBIC, center=(cx, cy))
        print("Burildi: %.1f gradus" % ROTATE)
    half = side // 2
    box = (max(0, cx - half), max(0, cy - half),
           min(W, cx + half), min(H, cy + half))
    im = im.crop(box)
    print("Kesildi: %s" % (box,))

    im = ImageEnhance.Color(im).enhance(SAT)
    im = ImageEnhance.Contrast(im).enhance(CON)
    im = ImageEnhance.Brightness(im).enhance(BRI)

    # pixel-art panjarasiga tushirish
    small = im.resize((GRID, GRID), Image.LANCZOS)
    small = tint(small)
    small = small.quantize(colors=2 ** POSTERIZE * 2, method=Image.MEDIANCUT).convert("RGB")

    small.putalpha(pixel_circle_mask(GRID))

    big = small.resize((OUT_PX, OUT_PX), Image.NEAREST)
    out = os.path.join(HERE, "avatar.png")
    big.save(out, optimize=True)
    print("Yozildi: avatar.png  %dx%d  %.1f KB"
          % (OUT_PX, OUT_PX, os.path.getsize(out) / 1024.0))


if __name__ == "__main__":
    main()
