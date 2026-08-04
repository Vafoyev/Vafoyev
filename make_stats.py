# -*- coding: utf-8 -*-
"""
GitHub statistikasi kartasini yasaydi (dark + light).

Nega o'zimizniki?  github-readme-stats.vercel.app ommaviy nusxasi o'chirilgan
(503 DEPLOYMENT_PAUSED), streak-stats esa <img> ichida animatsiyasiz ko'rinmaydi.
Bu skript ma'lumotni to'g'ridan-to'g'ri GitHub'dan oladi va statik SVG chizadi —
tashqi servisga umuman bog'liq emas.

Manbalar (hammasi ochiq, token shart emas):
  https://api.github.com/users/{user}
  https://api.github.com/users/{user}/repos
  https://github.com/users/{user}/contributions   (hissa kalendari)

GITHUB_TOKEN muhit o'zgaruvchisi bo'lsa, til statistikasi bayt aniqligida
hisoblanadi va rate-limit muammosi bo'lmaydi.

Ishlatish: python make_stats.py
Chiqadi:   stats-dark.svg  stats-light.svg
"""

import datetime as dt
import io
import json
import os
import re
import sys
import urllib.error
import urllib.request

USER = "Vafoyev"
HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()

SANS = "'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace"

PALETTES = {
    "dark": {
        "bg": "#0A101F", "card": "#0E1626", "grid": "#1B2740", "border": "#22304D",
        "text": "#F8FAFC", "muted": "#94A3B8", "dim": "#64748B",
        "cyan": "#22D3EE", "purple": "#A78BFA", "green": "#10B981", "amber": "#FBBF24",
        "heat": ["#16203A", "#0E4A5C", "#12849E", "#22D3EE", "#7DEFFF"],
    },
    "light": {
        "bg": "#FFFFFF", "card": "#F8FAFC", "grid": "#E2E8F0", "border": "#CBD5E1",
        "text": "#0F172A", "muted": "#475569", "dim": "#64748B",
        "cyan": "#0891B2", "purple": "#7C3AED", "green": "#059669", "amber": "#D97706",
        "heat": ["#EBEDF0", "#C7E9F0", "#7FD0E0", "#0891B2", "#06617A"],
    },
}

LANG_COLORS = {
    "Dart": "#00B4AB", "Kotlin": "#A97BFF", "Java": "#B07219", "Python": "#3572A5",
    "JavaScript": "#F1E05A", "TypeScript": "#3178C6", "C++": "#F34B7D", "C": "#555555",
    "HTML": "#E34C26", "CSS": "#563D7C", "C#": "#178600", "Shell": "#89E051",
    "Swift": "#F05138", "Ruby": "#701516", "Go": "#00ADD8", "PHP": "#4F5D95",
    "Jupyter Notebook": "#DA5B0B", "CMake": "#DA3434", "Makefile": "#427819",
    "Objective-C": "#438EFF", "Vue": "#41B883", "Dockerfile": "#384D54",
    "Batchfile": "#C1F12E", "PowerShell": "#012456", "Rust": "#DEA584",
    "SCSS": "#C6538C", "Blade": "#F7523F", "Procfile": "#A0A0A0",
}
FALLBACK_COLORS = ["#22D3EE", "#A78BFA", "#10B981", "#FBBF24", "#F472B6", "#60A5FA"]


# ── tarmoq ───────────────────────────────────────────────────────────────────
def fetch(url, as_json=True):
    req = urllib.request.Request(url, headers={
        "User-Agent": "vafoyev-profile-stats",
        "Accept": "application/vnd.github+json" if as_json else "text/html",
    })
    if TOKEN:
        req.add_header("Authorization", "Bearer %s" % TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode("utf-8", "replace")
    return json.loads(raw) if as_json else raw


# ── ma'lumot ─────────────────────────────────────────────────────────────────
def get_profile():
    return fetch("https://api.github.com/users/%s" % USER)


def get_repos():
    repos, page = [], 1
    while True:
        batch = fetch("https://api.github.com/users/%s/repos?per_page=100&page=%d" % (USER, page))
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def get_languages(repos):
    """Tillarni baytlar bo'yicha hisoblaydi; rate-limit bo'lsa asosiy tilga qaytadi."""
    own = [r for r in repos if not r.get("fork")]
    totals = {}
    try:
        for r in own:
            for lang, n in fetch(r["languages_url"]).items():
                totals[lang] = totals.get(lang, 0) + n
        if totals:
            return totals, "bytes"
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print("  ! til baytlarini olish uzildi (%s), asosiy tilga o'tildi" % e)

    totals = {}
    for r in own:
        if r.get("language"):
            totals[r["language"]] = totals.get(r["language"], 0) + 1
    return totals, "repos"


def get_contributions():
    """Hissa kalendarini oladi: [(sana, son, daraja), ...] va streak'lar."""
    html = fetch("https://github.com/users/%s/contributions" % USER, as_json=False)

    counts = {}
    for m in re.finditer(r'<tool-tip[^>]*for="(contribution-day-component-[\d-]+)"[^>]*>'
                         r'([^<]*)</tool-tip>', html):
        cid, txt = m.group(1), m.group(2)
        num = re.match(r"([\d,]+)\s+contribution", txt)
        counts[cid] = int(num.group(1).replace(",", "")) if num else 0

    days = []
    for m in re.finditer(r'<td[^>]*data-date="(\d{4}-\d{2}-\d{2})"[^>]*'
                         r'id="(contribution-day-component-[\d-]+)"[^>]*'
                         r'data-level="(\d)"', html):
        date, cid, level = m.group(1), m.group(2), int(m.group(3))
        days.append((date, counts.get(cid, 0), level))

    days.sort(key=lambda d: d[0])
    return days


def streaks(days):
    """Joriy va eng uzun streak. Bugungi kun hali bo'sh bo'lsa streak uzilmaydi."""
    today = dt.date.today().isoformat()
    longest = run = 0
    for _, n, _ in days:
        run = run + 1 if n > 0 else 0
        longest = max(longest, run)

    current = 0
    for date, n, _ in reversed(days):
        if n > 0:
            current += 1
        elif date == today:
            continue          # bugun hali boshlanmagan bo'lishi mumkin
        else:
            break
    return current, longest


# ── chizish ──────────────────────────────────────────────────────────────────
def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def human(n):
    if n >= 1000:
        return "%.1fk" % (n / 1000.0)
    return str(n)


def card(theme, data):
    p = PALETTES[theme]
    W, PAD = 1200, 34
    CW = W - 2 * PAD

    o = io.StringIO()
    body = io.StringIO()

    # ── stat plitkalari ──
    tiles = [
        ("PUBLIC REPOS",   human(data["repos"]),          "cyan"),
        ("TOTAL STARS",    human(data["stars"]),          "amber"),
        ("FOLLOWERS",      human(data["followers"]),      "purple"),
        ("CONTRIBUTIONS",  human(data["contrib_total"]),  "green"),
        ("CURRENT STREAK", "%d d" % data["streak_cur"],   "cyan"),
    ]
    ty, th = 108, 86
    tw = (CW - 4 * 14) // 5
    for i, (label, value, ck) in enumerate(tiles):
        x = PAD + i * (tw + 14)
        acc = p[ck]
        body.write('<rect x="%d" y="%d" width="%d" height="%d" rx="13" fill="%s" stroke="%s"/>'
                   % (x, ty, tw, th, p["card"], p["border"]))
        body.write('<rect x="%d" y="%d" width="3.5" height="%d" rx="1.75" fill="%s" opacity="0.85"/>'
                   % (x, ty + 18, th - 36, acc))
        body.write('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s" '
                   'letter-spacing="1.3">%s</text>' % (x + 20, ty + 28, MONO, p["dim"], label))
        body.write('<text x="%d" y="%d" font-family="%s" font-size="30" font-weight="800" '
                   'fill="%s">%s</text>' % (x + 19, ty + 66, SANS, acc, esc(value)))

    # ── tillar ──
    ly = ty + th + 30
    body.write('<text x="%d" y="%d" font-family="%s" font-size="12" font-weight="700" '
               'fill="%s" letter-spacing="1.6">TOP LANGUAGES</text>' % (PAD, ly, MONO, p["cyan"]))
    body.write('<text x="%d" y="%d" font-family="%s" font-size="11" fill="%s" text-anchor="end">'
               '%s</text>' % (PAD + CW, ly, MONO, p["dim"], esc(data["lang_basis"])))

    langs = data["langs"]
    total = sum(v for _, v in langs) or 1
    bx, by, bh = PAD, ly + 12, 14
    body.write('<clipPath id="barclip"><rect x="%d" y="%d" width="%d" height="%d" rx="7"/></clipPath>'
               % (bx, by, CW, bh))
    body.write('<g clip-path="url(#barclip)">')
    cx = float(bx)
    for i, (name, val) in enumerate(langs):
        w = CW * val / float(total)
        body.write('<rect x="%.2f" y="%d" width="%.2f" height="%d" fill="%s"/>'
                   % (cx, by, w + 0.5, bh, lang_color(name, i)))
        cx += w
    body.write('</g>')

    # legenda: 4 ustun
    gy = by + bh + 26
    colw = CW // 4
    for i, (name, val) in enumerate(langs):
        gx = PAD + (i % 4) * colw
        row = i // 4
        yy = gy + row * 24
        body.write('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (gx + 5, yy - 4, lang_color(name, i)))
        body.write('<text x="%d" y="%d" font-family="%s" font-size="12.5" fill="%s">%s</text>'
                   % (gx + 18, yy, SANS, p["text"], esc(name)))
        body.write('<text x="%d" y="%d" font-family="%s" font-size="11.5" fill="%s">%.1f%%</text>'
                   % (gx + 18 + len(name) * 7.2 + 8, yy, MONO, p["dim"], 100.0 * val / total))

    rows = (len(langs) + 3) // 4
    hy = gy + rows * 24 + 26

    # ── hissa issiqlik xaritasi ──
    body.write('<text x="%d" y="%d" font-family="%s" font-size="12" font-weight="700" '
               'fill="%s" letter-spacing="1.6">CONTRIBUTION ACTIVITY</text>'
               % (PAD, hy, MONO, p["green"]))
    body.write('<text x="%d" y="%d" font-family="%s" font-size="11" fill="%s" text-anchor="end">'
               'longest streak %d days</text>'
               % (PAD + CW, hy, MONO, p["dim"], data["streak_max"]))

    days = data["days"]
    # birinchi ustun yakshanbadan boshlanishi uchun to'ldirish
    first = dt.date.fromisoformat(days[0][0]) if days else dt.date.today()
    pad_start = (first.weekday() + 1) % 7          # Mon=0 -> Sun=0
    ncols = (pad_start + len(days) + 6) // 7
    # katak o'lchami kartaning to'liq kengligiga moslanadi
    gap = 3.0
    pitch = CW / float(ncols)
    cell = pitch - gap
    grid_y = hy + 26
    label_y = grid_y - 6

    seen_months = set()
    for idx, (date, n, level) in enumerate(days):
        slot = pad_start + idx
        col, row = slot // 7, slot % 7
        x = PAD + col * pitch
        y = grid_y + row * pitch
        body.write('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="3.5" fill="%s"/>'
                   % (x, y, cell, cell, p["heat"][min(level, 4)]))
        d = dt.date.fromisoformat(date)
        if d.day <= 7 and d.month not in seen_months and col < ncols - 3:
            seen_months.add(d.month)
            body.write('<text x="%.2f" y="%d" font-family="%s" font-size="10" fill="%s">%s</text>'
                       % (x, label_y, MONO, p["dim"], d.strftime("%b")))

    grid_h = 7 * pitch - gap
    legend_y = grid_y + grid_h + 24
    lx = PAD + CW - 150
    body.write('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s">Less</text>'
               % (lx, legend_y, MONO, p["dim"]))
    for i, c in enumerate(p["heat"]):
        body.write('<rect x="%d" y="%d" width="11" height="11" rx="2.5" fill="%s"/>'
                   % (lx + 32 + i * 15, legend_y - 9, c))
    body.write('<text x="%d" y="%d" font-family="%s" font-size="10.5" fill="%s">More</text>'
               % (lx + 32 + 5 * 15 + 4, legend_y, MONO, p["dim"]))

    H = legend_y + 24

    # ── ramka ──
    o.write('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
            'fill="none" role="img" aria-label="GitHub statistics">' % (W, H, W, H))
    o.write('<defs>'
            '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0%%" stop-color="%s"/><stop offset="55%%" stop-color="%s"/>'
            '<stop offset="100%%" stop-color="%s"/></linearGradient>'
            '<linearGradient id="bgfade" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/></linearGradient>'
            '<pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse">'
            '<path d="M34 0H0V34" fill="none" stroke="%s" stroke-width="1" stroke-opacity="0.55"/>'
            '</pattern></defs>'
            % (p["cyan"], p["purple"], p["green"], p["bg"], p["card"], p["grid"]))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#bgfade)"/>' % (W, H))
    o.write('<rect width="%d" height="%d" rx="18" fill="url(#grid)" opacity="0.4"/>' % (W, H))
    o.write('<rect x="0.5" y="0.5" width="%d" height="%d" rx="18" fill="none" stroke="%s"/>'
            % (W - 1, H - 1, p["border"]))
    o.write('<text x="%d" y="54" font-family="%s" font-size="28" font-weight="800" '
            'fill="url(#accent)" letter-spacing="1.5">GITHUB STATS</text>' % (PAD, SANS))
    o.write('<text x="%d" y="80" font-family="%s" font-size="13.5" fill="%s">'
            '@%s &#183; %s holatiga</text>'
            % (PAD, MONO, p["dim"], USER, data["updated"]))
    o.write('<rect x="%d" y="92" width="%d" height="1" fill="%s"/>' % (PAD, CW, p["border"]))
    o.write(body.getvalue())
    o.write('</svg>')
    return o.getvalue()


def lang_color(name, i):
    return LANG_COLORS.get(name, FALLBACK_COLORS[i % len(FALLBACK_COLORS)])


def main():
    print("GitHub'dan ma'lumot olinmoqda%s..." % (" (token bilan)" if TOKEN else ""))
    try:
        prof = get_profile()
        repos = get_repos()
        days = get_contributions()
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        sys.exit("Ma'lumot olinmadi: %s" % e)

    lang_totals, basis = get_languages(repos)
    top = sorted(lang_totals.items(), key=lambda kv: -kv[1])[:8]
    cur, longest = streaks(days)

    data = {
        "repos": prof.get("public_repos", 0),
        "followers": prof.get("followers", 0),
        "stars": sum(r.get("stargazers_count", 0) for r in repos if not r.get("fork")),
        "contrib_total": sum(n for _, n, _ in days),
        "streak_cur": cur,
        "streak_max": longest,
        "langs": top,
        "lang_basis": "bayt bo'yicha" if basis == "bytes" else "repo bo'yicha",
        "days": days,
        "updated": dt.date.today().isoformat(),
    }

    print("  repos=%d  stars=%d  followers=%d  contributions=%d  streak=%d/%d  langs=%d"
          % (data["repos"], data["stars"], data["followers"], data["contrib_total"],
             cur, longest, len(top)))

    for theme in ("dark", "light"):
        name = "stats-%s.svg" % theme
        svg = card(theme, data)
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
            f.write(svg)
        print("  %-18s %6.1f KB" % (name, len(svg) / 1024.0))


if __name__ == "__main__":
    main()
