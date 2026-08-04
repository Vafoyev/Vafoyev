# -*- coding: utf-8 -*-
"""
Vafoyev GitHub profile — SVG generator.
Bitta shablondan dark + light temadagi banner va loyihalar devorini yasaydi.

Ishlatish:  python make_avatar.py   (avval avatar)
            python generate.py
Chiqadi:    dark.svg  light.svg  projects-dark.svg  projects-light.svg
"""

import base64
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NAME = "VAFOYEV"
TAGLINE = "Full-Stack | IoT | Drone Systems Developer"
SUBLINE = "Building the future of robotics, one system at a time"

PALETTES = {
    "dark": {
        "bg": "#0A101F", "card": "#0E1626", "grid": "#1B2740", "border": "#22304D",
        "text": "#F8FAFC", "muted": "#94A3B8", "dim": "#64748B",
        "cyan": "#22D3EE", "purple": "#A78BFA", "green": "#10B981", "amber": "#FBBF24",
        "chip_bg": "#131F35", "chip_text": "#CBD5E1",
    },
    "light": {
        "bg": "#FFFFFF", "card": "#F8FAFC", "grid": "#E2E8F0", "border": "#CBD5E1",
        "text": "#0F172A", "muted": "#475569", "dim": "#64748B",
        "cyan": "#0891B2", "purple": "#7C3AED", "green": "#059669", "amber": "#D97706",
        "chip_bg": "#F1F5F9", "chip_text": "#334155",
    },
}

SANS = "'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace"

HERO_CHIPS = ["Flutter", "Kotlin", "C++", "ESP32", "Node.js", "Firebase"]

# ── Ionicons uslubidagi chiziqli ikonkalar (24x24 koordinata maydoni) ─────────
ICONS = {
    "car": '<path d="M4 11.5 6 6.2A2.5 2.5 0 0 1 8.4 4.5h7.2A2.5 2.5 0 0 1 18 6.2l2 5.3"/>'
           '<rect x="2.5" y="11.5" width="19" height="6.5" rx="2"/>'
           '<circle cx="7" cy="19.6" r="1.4"/><circle cx="17" cy="19.6" r="1.4"/>',
    "navigate": '<path d="M20.5 3.5 3.8 10.6a.6.6 0 0 0 .05 1.1l6.6 2.4 2.4 6.6a.6.6 0 0 0 1.1.05z"/>',
    "drone": '<circle cx="5" cy="5" r="2.8"/><circle cx="19" cy="5" r="2.8"/>'
             '<circle cx="5" cy="19" r="2.8"/><circle cx="19" cy="19" r="2.8"/>'
             '<rect x="9" y="9" width="6" height="6" rx="1.6"/>'
             '<path d="M7 7l2 2M17 7l-2 2M7 17l2-2M17 17l-2-2"/>',
    "wallet": '<rect x="2.5" y="5.5" width="19" height="14" rx="3"/>'
              '<path d="M2.5 10h19"/><circle cx="17" cy="15" r="1.3"/>',
    "medkit": '<rect x="2.5" y="7" width="19" height="13" rx="2.5"/>'
              '<path d="M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M12 11v6M9 14h6"/>',
    "football": '<circle cx="12" cy="12" r="9"/>'
                '<path d="M12 7.2l4.3 3.1-1.65 5.1H9.35L7.7 10.3z"/>'
                '<path d="M12 3v4.2M20.6 10.3l-4.3 3.1M17.6 20.4l-2.95-4.1'
                'M6.4 20.4l2.95-4.1M3.4 10.3l4.3 3.1"/>',
    "nutrition": '<path d="M7 3.5v7a2.5 2.5 0 0 0 5 0v-7M9.5 3.5v17'
                 'M17.5 3.5c-1.4 1.9-2 3.8-2 6.2 0 1.6.8 2.6 2 2.6v8.2"/>',
    "bus": '<rect x="4" y="3.5" width="16" height="13.5" rx="2.5"/>'
           '<path d="M4 10.5h16M7.5 17v3M16.5 17v3"/>'
           '<circle cx="8" cy="13.8" r="1"/><circle cx="16" cy="13.8" r="1"/>',
    "book": '<path d="M4 5A2 2 0 0 1 6 3h13.5v14.5H6a2 2 0 0 0-2 2z"/>'
            '<path d="M4 19.5A2 2 0 0 1 6 17.5h13.5V21H6a2 2 0 0 1-2-1.5z"/>',
    "school": '<path d="M2.5 8.8 12 4.2l9.5 4.6L12 13.4z"/>'
              '<path d="M6.3 11.2V16c0 1.7 2.6 3 5.7 3s5.7-1.3 5.7-3v-4.8"/>'
              '<path d="M21.5 8.8v5"/>',
    "people": '<circle cx="9.2" cy="8" r="3.3"/>'
              '<path d="M2.8 20c0-3.4 2.9-5.7 6.4-5.7s6.4 2.3 6.4 5.7"/>'
              '<path d="M16.2 5.1a3.3 3.3 0 0 1 0 6.2"/>'
              '<path d="M17.6 14.8c2.2.7 3.6 2.6 3.6 5.2"/>',
    "briefcase": '<rect x="2.5" y="7" width="19" height="13" rx="2.5"/>'
                 '<path d="M8.5 7V5.4A1.4 1.4 0 0 1 9.9 4h4.2a1.4 1.4 0 0 1 1.4 1.4V7'
                 'M2.5 12.6h19M11 12.6v2"/>',
    "fingerprint": '<path d="M12 3.4A8.6 8.6 0 0 0 3.4 12v2.2"/>'
                   '<path d="M20.6 12A8.6 8.6 0 0 0 16 4.4"/>'
                   '<path d="M12 7.2A4.8 4.8 0 0 0 7.2 12v3.4"/>'
                   '<path d="M16.8 12a4.8 4.8 0 0 0-1.9-3.8"/>'
                   '<path d="M12 10.6A1.4 1.4 0 0 0 10.6 12v5.6"/>'
                   '<path d="M13.9 12.4v5.8"/><path d="M5.6 18.4a9 9 0 0 0 1.8 2"/>',
    "chip": '<rect x="6" y="6" width="12" height="12" rx="2.2"/>'
            '<rect x="9.6" y="9.6" width="4.8" height="4.8" rx="1"/>'
            '<path d="M9.2 3v3M14.8 3v3M9.2 18v3M14.8 18v3'
            'M3 9.2h3M3 14.8h3M18 9.2h3M18 14.8h3"/>',
    "cloud": '<path d="M6.6 18.5h10.6a4.2 4.2 0 0 0 .6-8.4A6.2 6.2 0 0 0 6.2 11.2'
             'a3.7 3.7 0 0 0 .4 7.3z"/>',
    "code": '<path d="M8.6 7.4 3.4 12l5.2 4.6M15.4 7.4 20.6 12l-5.2 4.6M13.6 4l-3.2 16"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6"/>'
             '<path d="M12 3c2.6 2.9 2.6 15.1 0 18M12 3c-2.6 2.9-2.6 15.1 0 18"/>',
    "videocam": '<rect x="2.5" y="6.5" width="12.2" height="11" rx="2.6"/>'
                '<path d="M14.7 10.6 21 7.2v9.6l-6.3-3.4z"/>',
    "sparkles": '<path d="M11 3.2l1.7 4.4 4.4 1.7-4.4 1.7L11 15.4 9.3 11 4.9 9.3 9.3 7.6z"/>'
                '<path d="M18 14.4l.85 2.2 2.2.85-2.2.85-.85 2.2-.85-2.2-2.2-.85 2.2-.85z"/>',
    "cart": '<circle cx="9.2" cy="19.4" r="1.6"/><circle cx="17.4" cy="19.4" r="1.6"/>'
            '<path d="M2.6 3.6h2.7l2.4 11.4h10.9l1.9-7.9H6.2"/>',
    "server": '<rect x="3" y="3.4" width="18" height="6.2" rx="2"/>'
              '<rect x="3" y="14.4" width="18" height="6.2" rx="2"/>'
              '<path d="M6.9 6.5h.02M6.9 17.5h.02M10.5 6.5h4M10.5 17.5h4"/>',
    "flask": '<path d="M9.4 3.4v6.3L4.6 17.9A2.1 2.1 0 0 0 6.4 21h11.2a2.1 2.1 0 0 0 1.8-3.1'
             'l-4.8-8.2V3.4"/><path d="M8 3.4h8M7.2 14.2h9.6"/>',
    "shield": '<path d="M12 3.2l8 3v5.9c0 4.4-3.2 7.9-8 8.7-4.8-.8-8-4.3-8-8.7V6.2z"/>'
              '<path d="M9 12l2.2 2.2L15.2 10"/>',
    "phone": '<rect x="6" y="2.6" width="12" height="18.8" rx="3"/>'
             '<path d="M10.5 5.4h3M12 18.3h.02"/>',
}

# ── Loyihalar ────────────────────────────────────────────────────────────────
# (ikonka, nomi, izohi, stack)
SECTIONS = [
    ("MOBILE APPS", "cyan", [
        ("wallet",    "justmoney",        "Personal finance & budget tracker", "Flutter"),
        ("medkit",    "MindCare",         "Ruhiy salomatlik ilovasi",          "Flutter"),
        ("football",  "iStadium",         "Stadion bron qilish platformasi",   "Flutter"),
        ("bus",       "BusPro",           "Real-time avtobus kuzatish, Urganch", "Flutter"),
        ("book",      "E-Qollanma",       "E-Darslik.AI o'quv platformasi",    "Flutter · Kotlin"),
        ("school",    "Edu Pro",          "Chizmachilik test va o'quv dasturi", "Flutter"),
        ("people",    "OneFamily",        "Oila uchun mobil ilova",            "Flutter · Kotlin"),
        ("briefcase", "RGD Business",     "Balans, mahsulot va MLM boshqaruvi", "Flutter · Kotlin"),
        ("nutrition", "fit_taom",         "Fitness va ovqatlanish rejasi",     "Flutter"),
        ("car",       "A1Taxi Driver",    "Haydovchi uchun taksi ilovasi",     "Java · Kotlin"),
        ("navigate",  "A1Taxi Client",    "Yo'lovchi uchun taksi ilovasi",     "Java"),
        ("phone",     "Catelnium Agent",  "Windows IoT agent ilovasi",         "Flutter"),
    ]),
    ("DRONE & ROBOTICS", "purple", [
        ("drone",  "A1techAir",     "Dron boshqaruvi mobil ilovasi",     "Java · Kotlin"),
        ("chip",   "MSDK 2.5",      "DJI Mobile SDK 2.5 integratsiyasi", "Kotlin"),
        ("drone",  "DJ Mavaric",    "DJI Mavic parvoz kontrolleri",      "Kotlin"),
        ("server", "Drone Backend", "Telemetriya serveri va web panel",  "Python"),
    ]),
    ("IoT & EMBEDDED", "green", [
        ("flask",       "Smart City MQ-136", "H2S gaz sensori tuguni",        "C++ · ESP32"),
        ("shield",      "SkyGuard AI",       "Dronga o'rnatilgan gaz detektori", "ESP32 · Flutter"),
        ("fingerprint", "FingerprintBack",   "Barmoq izi bilan kirish nazorati", "Arduino · Python"),
    ]),
    ("AI & COMPUTER VISION", "amber", [
        ("sparkles", "AqilUstun",         "Gemini Live asosidagi aqlli domofon", "Python"),
        ("code",     "AqilUstun Bridge",  "Hikvision ↔ AI ko'prigi",            "Python"),
        ("videocam", "HikVision FaceID",  "Yuz aniqlash agenti",                 "Python"),
        ("phone",    "FaceID Agent",      "FaceID mobil klienti",                "Flutter · Kotlin"),
    ]),
    ("BACKEND & WEB", "cyan", [
        ("server", "A1Taxi Server",      "Taksi platformasi backendi",   "Java · Maven"),
        ("globe",  "Lernify CS",         "O'quv platformasi web ilovasi", "TypeScript · React"),
        ("code",   "UzbTech Hackathon",  "Hakaton loyihasi",              "JavaScript · TS"),
        ("cart",   "Shopping Dashboard", "Do'kon boshqaruv paneli",       "JavaScript"),
        ("globe",  "Kallavaram",         "Web ilova",                     "JavaScript"),
    ]),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# MUHIM: bu yerda "paydo bo'lish" (fade-in / typewriter) animatsiyalari ataylab yo'q.
#
# README'da SVG <img> sifatida yuklanadi va bu holatda brauzer SMIL taymlaynini
# ko'pincha 0-kadrda to'xtatib qo'yadi. Boshlang'ich qiymati 0 bo'lgan har qanday
# animatsiya (opacity="0" yoki width="0") kontentni butunlay ko'rinmas qoldiradi.
# Shu sababli faqat "bezak" animatsiyalar ishlatiladi: ularning boshlang'ich holati
# ham to'liq ko'rinadigan holat (propeller aylanishi, halqa puls, nur o'ynashi).


def avatar_b64():
    path = os.path.join(HERE, "avatar.png")
    if not os.path.exists(path):
        raise SystemExit("avatar.png topilmadi — avval `python make_avatar.py` ni ishlating")
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def icon(name, x, y, size, color, sw=2.0):
    """Ikonkani (x,y) dan boshlab size x size kvadratga chizadi."""
    k = size / 24.0
    return ('<g transform="translate(%.2f,%.2f) scale(%.4f)" fill="none" stroke="%s" '
            'stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round">%s</g>'
            % (x, y, k, color, sw / k, ICONS[name]))


def chip(x, y, label, p, h=34, fs=14, pad=15):
    w = int(len(label) * fs * 0.60) + pad * 2
    s = ('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s" stroke="%s"/>'
         '<text x="%d" y="%d" font-family="%s" font-size="%d" fill="%s">%s</text>'
         % (x, y, w, h, h // 2, p["chip_bg"], p["border"],
            x + pad, y + h // 2 + int(fs * 0.36), MONO, fs, p["chip_text"], esc(label)))
    return s, x + w + 10


def defs(p):
    return (
        '<defs>'
        '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0%%" stop-color="%s"/><stop offset="55%%" stop-color="%s"/>'
        '<stop offset="100%%" stop-color="%s"/></linearGradient>'
        '<linearGradient id="bgfade" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/></linearGradient>'
        '<radialGradient id="glowC"><stop offset="0%%" stop-color="%s" stop-opacity="0.30"/>'
        '<stop offset="100%%" stop-color="%s" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="glowP"><stop offset="0%%" stop-color="%s" stop-opacity="0.26"/>'
        '<stop offset="100%%" stop-color="%s" stop-opacity="0"/></radialGradient>'
        '<pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse">'
        '<path d="M34 0H0V34" fill="none" stroke="%s" stroke-width="1" stroke-opacity="0.55"/>'
        '</pattern>'
        '</defs>'
    ) % (p["cyan"], p["purple"], p["green"], p["bg"], p["card"],
         p["cyan"], p["cyan"], p["purple"], p["purple"], p["grid"])


def neon_avatar(cx, cy, r, p, b64):
    """Pixel-art avatar + neon halqalar."""
    d = r * 2
    o = ['<g>']
    # tashqi yumshoq nur
    o.append('<circle cx="%d" cy="%d" r="%d" fill="url(#glowC)" opacity="0.9"/>' % (cx, cy, r + 55))
    # aylanuvchi uzuq halqa
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="14 10" opacity="0.55">'
             '<animateTransform attributeName="transform" type="rotate" '
             'from="0 %d %d" to="360 %d %d" dur="22s" repeatCount="indefinite"/>'
             '</circle>' % (cx, cy, r + 16, p["purple"], cx, cy, cx, cy))
    # neon nurlanish qatlamlari
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="12" opacity="0.10"/>'
             % (cx, cy, r + 4, p["cyan"]))
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="6" opacity="0.22"/>'
             % (cx, cy, r + 4, p["cyan"]))
    # rasm
    o.append('<image x="%d" y="%d" width="%d" height="%d" image-rendering="pixelated" '
             'href="data:image/png;base64,%s"/>' % (cx - r, cy - r, d, d, b64))
    # asosiy gradientli halqa + puls
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="url(#accent)" stroke-width="3">'
             '<animate attributeName="opacity" values="1;0.55;1" dur="3.2s" repeatCount="indefinite"/>'
             '</circle>' % (cx, cy, r + 3))
    # "online" nuqtasi
    bx, by = cx + int(r * 0.70), cy + int(r * 0.70)
    o.append('<circle cx="%d" cy="%d" r="11" fill="%s" stroke="%s" stroke-width="3"/>'
             % (bx, by, p["green"], p["bg"]))
    o.append('<circle cx="%d" cy="%d" r="11" fill="none" stroke="%s" stroke-width="2" opacity="0">'
             '<animate attributeName="r" values="11;22" dur="2.4s" repeatCount="indefinite"/>'
             '<animate attributeName="opacity" values="0.7;0" dur="2.4s" repeatCount="indefinite"/>'
             '</circle>' % (bx, by, p["green"]))
    o.append('</g>')
    return "".join(o)


def drone(cx, cy, p):
    out = ['<g transform="translate(%d,%d)">' % (cx, cy)]
    for delay in (0, 1.3, 2.6):
        out.append('<circle cx="0" cy="0" r="40" fill="none" stroke="%s" stroke-width="1.5" opacity="0">'
                   '<animate attributeName="r" values="40;140" dur="3.9s" begin="%ss" repeatCount="indefinite"/>'
                   '<animate attributeName="opacity" values="0.5;0" dur="3.9s" begin="%ss" repeatCount="indefinite"/>'
                   '</circle>' % (p["cyan"], delay, delay))
    out.append('<g><animateTransform attributeName="transform" type="translate" '
               'values="0,-5; 0,5; 0,-5" dur="3.4s" repeatCount="indefinite" calcMode="spline" '
               'keySplines="0.4 0 0.6 1; 0.4 0 0.6 1" keyTimes="0;0.5;1"/>')
    arms = [(-68, -47), (68, -47), (-68, 47), (68, 47)]
    for dx, dy in arms:
        out.append('<line x1="0" y1="0" x2="%d" y2="%d" stroke="%s" stroke-width="4" '
                   'stroke-linecap="round" opacity="0.85"/>' % (dx, dy, p["purple"]))
    for idx, (dx, dy) in enumerate(arms):
        spin = "0 0 0;360 0 0" if idx % 2 == 0 else "360 0 0;0 0 0"
        out.append('<g transform="translate(%d,%d)">'
                   '<circle r="28" fill="none" stroke="%s" stroke-width="2" opacity="0.55"/>'
                   '<g><animateTransform attributeName="transform" type="rotate" values="%s" '
                   'dur="0.42s" repeatCount="indefinite"/>'
                   '<ellipse rx="27" ry="4.5" fill="%s" opacity="0.75"/>'
                   '<ellipse rx="4.5" ry="27" fill="%s" opacity="0.45"/></g>'
                   '<circle r="4" fill="%s"/></g>'
                   % (dx, dy, p["cyan"], spin, p["cyan"], p["cyan"], p["purple"]))
    out.append('<rect x="-40" y="-25" width="80" height="50" rx="14" fill="%s" '
               'stroke="url(#accent)" stroke-width="2.5"/>' % p["card"])
    out.append('<rect x="-24" y="-12" width="48" height="15" rx="7.5" fill="%s" opacity="0.35"/>'
               % p["cyan"])
    out.append('<circle cx="0" cy="31" r="12" fill="%s" stroke="%s" stroke-width="2.5"/>'
               % (p["card"], p["green"]))
    out.append('<circle cx="0" cy="31" r="4.5" fill="%s">'
               '<animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/>'
               '</circle>' % p["green"])
    out.append('</g></g>')
    return "".join(out)


def hero(theme, b64):
    p = PALETTES[theme]
    W, H = 1200, 430
    TX = 288  # matn boshlanish nuqtasi
    o = io.StringIO()
    o.write('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'fill="none" role="img" aria-label="%s">' % (W, H, W, H, NAME))
    o.write(defs(p))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#bgfade)"/>' % (W, H))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#grid)" opacity="0.5"/>' % (W, H))
    o.write('<circle cx="1010" cy="60" r="240" fill="url(#glowC)">'
            '<animate attributeName="opacity" values="0.75;1;0.75" dur="6s" repeatCount="indefinite"/>'
            '</circle>')
    o.write('<circle cx="70" cy="410" r="230" fill="url(#glowP)">'
            '<animate attributeName="opacity" values="1;0.7;1" dur="7.5s" repeatCount="indefinite"/>'
            '</circle>')
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))
    o.write('<rect x="18" y="0" width="%d" height="3" rx="1.5" fill="url(#accent)" opacity="0.9"/>'
            % (W - 36))

    o.write(neon_avatar(146, 208, 92, p, b64))
    o.write(drone(1035, 210, p))

    o.write('<text x="%d" y="98" font-family="%s" font-size="17" fill="%s" letter-spacing="1.5">'
            '<tspan fill="%s">$</tspan> whoami<tspan fill="%s">_</tspan></text>'
            % (TX, MONO, p["muted"], p["green"], p["cyan"]))
    o.write('<text x="%d" y="176" font-family="%s" font-size="64" font-weight="800" '
            'fill="url(#accent)" letter-spacing="2">%s</text>' % (TX - 2, SANS, esc(NAME)))
    o.write('<rect x="%d" y="192" width="140" height="5" rx="2.5" fill="url(#accent)"/>' % TX)
    o.write('<text x="%d" y="246" font-family="%s" font-size="23" font-weight="600" fill="%s">%s</text>'
            % (TX, SANS, p["text"], esc(TAGLINE)))
    # terminal kursori — boshlang'ich holati ko'rinadigan, faqat miltillaydi
    o.write('<rect x="%d" y="226" width="2.5" height="24" fill="%s">'
            '<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/>'
            '</rect>' % (TX + 542, p["cyan"]))
    o.write('<text x="%d" y="282" font-family="%s" font-size="15.5" fill="%s">%s</text>'
            % (TX, SANS, p["muted"], esc(SUBLINE)))

    x = TX
    for label in HERO_CHIPS:
        s, x = chip(x, 326, label, p)
        o.write(s)

    o.write('</svg>')
    return o.getvalue()


def projects(theme):
    p = PALETTES[theme]
    W = 1200
    PAD, COLS = 22, 4
    TW, TH, GX, GY = 278, 84, 14, 12
    HEAD_H, SEC_GAP = 40, 16

    # balandlikni oldindan hisoblash
    y = 108
    for _, _, items in SECTIONS:
        rows = (len(items) + COLS - 1) // COLS
        y += HEAD_H + rows * (TH + GY) + SEC_GAP
    H = y + 12

    o = io.StringIO()
    o.write('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'fill="none" role="img" aria-label="All projects">' % (W, H, W, H))
    o.write(defs(p))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#bgfade)"/>' % (W, H))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#grid)" opacity="0.4"/>' % (W, H))
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))

    total = sum(len(i) for _, _, i in SECTIONS)
    o.write('<text x="%d" y="54" font-family="%s" font-size="28" font-weight="800" '
            'fill="url(#accent)" letter-spacing="1.5">ALL PROJECTS</text>' % (PAD + 12, SANS))
    o.write('<text x="%d" y="80" font-family="%s" font-size="13.5" fill="%s">'
            '%d loyiha &#183; mobil, dron, IoT, AI va backend</text>'
            % (PAD + 12, MONO, p["dim"], total))
    o.write('<rect x="%d" y="92" width="%d" height="1" fill="%s"/>'
            % (PAD + 12, W - 2 * (PAD + 12), p["border"]))

    y = 108
    n = 0
    for title, acc_key, items in SECTIONS:
        acc = p[acc_key]
        o.write('<rect x="%d" y="%d" width="4" height="16" rx="2" fill="%s"/>'
                % (PAD + 12, y + 8, acc))
        o.write('<text x="%d" y="%d" font-family="%s" font-size="14" font-weight="700" '
                'fill="%s" letter-spacing="1.6">%s</text>'
                % (PAD + 26, y + 21, MONO, acc, esc(title)))
        o.write('<text x="%d" y="%d" font-family="%s" font-size="12" fill="%s">%d</text>'
                % (W - PAD - 24, y + 21, MONO, p["dim"], len(items)))
        y += HEAD_H

        for i, (ic, name, desc, stack) in enumerate(items):
            cx = PAD + (i % COLS) * (TW + GX)
            cy = y + (i // COLS) * (TH + GY)
            o.write('<g>')
            o.write('<rect x="%d" y="%d" width="%d" height="%d" rx="13" fill="%s" stroke="%s"/>'
                    % (cx, cy, TW, TH, p["card"], p["border"]))
            o.write('<rect x="%d" y="%d" width="3.5" height="%d" rx="1.75" fill="%s" opacity="0.85"/>'
                    % (cx, cy + 20, TH - 40, acc))
            # ikonka qutisi
            o.write('<rect x="%d" y="%d" width="40" height="40" rx="11" fill="%s" opacity="0.13"/>'
                    % (cx + 16, cy + 22, acc))
            o.write(icon(ic, cx + 24, cy + 30, 24, acc, sw=1.9))
            o.write('<text x="%d" y="%d" font-family="%s" font-size="15" font-weight="700" '
                    'fill="%s">%s</text>' % (cx + 68, cy + 32, SANS, p["text"], esc(name)))
            o.write('<text x="%d" y="%d" font-family="%s" font-size="11.5" fill="%s">%s</text>'
                    % (cx + 68, cy + 50, SANS, p["muted"], esc(desc)))
            o.write('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s" '
                    'letter-spacing="0.3">%s</text>'
                    % (cx + 68, cy + 68, MONO, acc, esc(stack)))
            o.write('</g>')
            n += 1

        rows = (len(items) + COLS - 1) // COLS
        y += rows * (TH + GY) + SEC_GAP

    o.write('</svg>')
    return o.getvalue()


def main():
    b64 = avatar_b64()
    files = {
        "dark.svg": hero("dark", b64),
        "light.svg": hero("light", b64),
        "projects-dark.svg": projects("dark"),
        "projects-light.svg": projects("light"),
    }
    for name, content in files.items():
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("  %-20s %6.1f KB" % (name, len(content) / 1024.0))
    print("\nTayyor.")


if __name__ == "__main__":
    main()
