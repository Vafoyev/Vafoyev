# -*- coding: utf-8 -*-
"""
"Snake eating contributions" animatsiyasini yasaydi (dark + light).

Nega o'zimizniki?  Platane/snk GitHub Action'ini ishlatib bo'lmadi — akkaunt
billing sababli bloklangani uchun Actions umuman ishga tushmaydi. Bu skript
hissa kalendarini o'zi oladi va SVG'ni to'g'ridan-to'g'ri chizadi.

Animatsiya SMIL emas, CSS @keyframes bilan yozilgan. GitHub README'dagi SVG
<img> sifatida yuklanadi va bu holatda SMIL (<animate>, <animateMotion>)
0-kadrda qotib qoladi — tekshirildi, ilon joyidan qimirlamadi. CSS
animatsiyalari esa ishlaydi; Platane/snk ham aynan shu sababli CSS ishlatadi.

Boshlang'ich holat baribir to'liq rangli heatmap: animatsiya umuman
ishlamasa ham bo'sh quti emas, oddiy hissa jadvali ko'rinadi.

Ishlatish: python make_snake.py
Chiqadi:   snake-dark.svg  snake-light.svg
"""

import datetime as dt
import io
import os

from make_stats import PALETTES, USER, get_contributions

HERE = os.path.dirname(os.path.abspath(__file__))

ROWS = 7
CYCLE = 24.0          # to'liq aylanish davomiyligi (soniya)
SNAKE_LEN = 5         # bosh + tana bo'g'inlari
MONO = "ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace"

SNAKE_COLORS = {
    "dark":  ["#7DEFFF", "#22D3EE", "#1BB8D4", "#A78BFA", "#8B6FE0"],
    "light": ["#0891B2", "#0AA5CC", "#22D3EE", "#7C3AED", "#9B6BF0"],
}


def build_grid(days):
    """Kunlarni (ustun, qator) panjaraga joylaydi."""
    first = dt.date.fromisoformat(days[0][0])
    pad = (first.weekday() + 1) % 7           # Mon=0 -> yakshanbadan boshlanadi
    cells = {}
    for idx, (date, n, level) in enumerate(days):
        slot = pad + idx
        cells[(slot // 7, slot % 7)] = (date, n, level)
    ncols = (pad + len(days) + 6) // 7
    return cells, ncols


def serpentine(ncols):
    """Ilon yo'li: ustunma-ustun pastga-yuqoriga. Har qadam qo'shni katakka."""
    path = []
    for col in range(ncols):
        rows = range(ROWS) if col % 2 == 0 else range(ROWS - 1, -1, -1)
        for row in rows:
            path.append((col, row))
    return path


def build(theme, days):
    p = PALETTES[theme]
    snake_cols = SNAKE_COLORS[theme]

    cells, ncols = build_grid(days)
    path = serpentine(ncols)
    steps = len(path)
    step_dur = CYCLE / steps

    W, PAD = 1200, 34
    CW = W - 2 * PAD
    gap = 3.0
    pitch = CW / float(ncols)
    cell = pitch - gap
    grid_y = 58
    H = int(grid_y + ROWS * pitch + 34)

    def cx(col):
        return PAD + col * pitch

    def cy(row):
        return grid_y + row * pitch

    o = io.StringIO()
    o.write('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'fill="none" role="img" aria-label="Snake eating my contributions">' % (W, H, W, H))
    o.write('<defs><linearGradient id="bgfade" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/>'
            '</linearGradient>'
            '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0%%" stop-color="%s"/><stop offset="55%%" stop-color="%s"/>'
            '<stop offset="100%%" stop-color="%s"/></linearGradient></defs>'
            % (p["bg"], p["card"], p["cyan"], p["purple"], p["green"]))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#bgfade)"/>' % (W, H))
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))
    o.write('<text x="%d" y="38" font-family="%s" font-size="12" font-weight="700" '
            'fill="%s" letter-spacing="1.6">SNAKE EATING MY CONTRIBUTIONS</text>'
            % (PAD, MONO, p["cyan"]))
    o.write('<text x="%d" y="38" font-family="%s" font-size="11" fill="%s" text-anchor="end">'
            '@%s</text>' % (PAD + CW, MONO, p["dim"], USER))

    # ── CSS ──
    empty = p["heat"][0]
    css = io.StringIO()

    # Ilon yo'li: barcha bo'g'inlar bitta @keyframes'dan foydalanadi, faqat
    # animation-delay bilan bir-biridan orqada qoladi.
    css.write("@keyframes slither{")
    for i, (col, row) in enumerate(path):
        pct = 100.0 * i / (steps - 1)
        css.write("%.4f%%{transform:translate(%.2fpx,%.2fpx)}"
                  % (pct, cx(col) + cell / 2, cy(row) + cell / 2))
    css.write("}")
    css.write(".sn{animation:slither %.2fs linear infinite}" % CYCLE)

    # Har bir daraja uchun alohida "yeyilish" keyframe'i. Katak o'z vaqtida
    # o'chishi uchun animation-delay ishlatiladi (pastda, har katakda).
    flip = 1.0                                    # foizda: qachon rang o'chadi
    for lv in range(1, 5):
        css.write("@keyframes eat%d{0%%{fill:%s}%.2f%%{fill:%s}%.2f%%{fill:%s}100%%{fill:%s}}"
                  % (lv, p["heat"][lv], flip * 0.8, p["heat"][lv], flip, empty, empty))
        css.write(".e%d{animation:eat%d %.2fs linear infinite}" % (lv, lv, CYCLE))

    o.write('<style>%s</style>' % css.getvalue())

    # ── kataklar ──
    # Boshlang'ich fill = o'z rangi, shuning uchun animatsiyasiz ham to'liq ko'rinadi.
    for i, (col, row) in enumerate(path):
        info = cells.get((col, row))
        if info is None:
            continue
        _, n, level = info
        lv = min(level, 4)
        base = p["heat"][lv]
        attrs = ''
        if lv > 0:
            # katak ilon yetib kelgan paytda o'chsin
            delay = (i / float(steps)) * CYCLE - (flip / 100.0) * CYCLE
            attrs = ' class="e%d" style="animation-delay:%.3fs"' % (lv, delay)
        o.write('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="3.5" fill="%s"%s/>'
                % (cx(col), cy(row), cell, cell, base, attrs))

    # ── ilon ──
    # transform atributi — animatsiyasiz holat uchun: ilon panjara boshida turadi,
    # burchakka tushib qolmaydi. CSS ishlaganda uni keyframes bekor qiladi.
    sc, sr = path[0]
    home = (cx(sc) + cell / 2, cy(sr) + cell / 2)
    for k in range(SNAKE_LEN):
        size = cell * (1.0 - 0.07 * k)
        off = size / 2.0
        color = snake_cols[min(k, len(snake_cols) - 1)]
        o.write('<g class="sn" transform="translate(%.2f,%.2f)" style="animation-delay:%.4fs">'
                '<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="%.2f" fill="%s" '
                'opacity="%.2f"/></g>'
                % (home[0], home[1], k * step_dur,
                   -off, -off, size, size, size * 0.28, color, 1.0 - 0.12 * k))

    o.write('</svg>')
    return o.getvalue()


def main():
    print("Hissa kalendari olinmoqda...")
    days = get_contributions()
    print("  %d kun, %d hissa" % (len(days), sum(n for _, n, _ in days)))
    for theme in ("dark", "light"):
        name = "snake-%s.svg" % theme
        svg = build(theme, days)
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("  %-18s %6.1f KB" % (name, len(svg) / 1024.0))


if __name__ == "__main__":
    main()
