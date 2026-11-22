#!/usr/bin/env python3
"""Render site pages (support, legal) and SEO guides from Markdown into the static site.
Also writes guides/index.html, sitemap.xml and robots.txt.   Run: python3 tools/build_site.py"""
import html, re
from datetime import date
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOMAIN = "https://unghostedhq.vercel.app"
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse(p):
    t = p.read_text(); meta = {}
    m = FRONT.match(t)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":"); meta[k.strip()] = v.strip()
        t = t[m.end():]
    return meta, t


def shell(meta, body, depth, cls="", extra=""):
    r = "../" * depth
    e = html.escape
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(meta['title'])} | Unghosted</title>
<meta name="description" content="{e(meta.get('description',''))}">
<link rel="canonical" href="{DOMAIN}/{meta['slug']}.html">
<meta property="og:title" content="{e(meta['title'])}"><meta property="og:description" content="{e(meta.get('description',''))}">
<meta property="og:image" content="{DOMAIN}/assets/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{r}assets/site.css">
<script src="{r}config.js"></script>{extra}</head><body>
<nav class="nav"><div class="wrap"><a class="brand" href="{r}index.html"><svg class="ghost" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="currentColor"/><circle cx="9.2" cy="10" r="1.7" fill="#D7FF3A"/><circle cx="14.8" cy="10" r="1.7" fill="#D7FF3A"/></svg>unghosted</a>
<div class="links"><a class="hide-sm" href="{r}guides/">Free guides</a><a class="hide-sm" href="{r}support.html">Support</a><a class="btn btn-dark btn-sm" href="{r}index.html#pricing">See pricing</a></div></div></nav>
<main class="article {cls}"><div class="wrap narrow">{body}</div></main>
<footer><div class="wrap cols"><div><a class="brand" href="{r}index.html"><svg class="ghost" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="currentColor"/><circle cx="9.2" cy="10" r="1.7" fill="#D7FF3A"/><circle cx="14.8" cy="10" r="1.7" fill="#D7FF3A"/></svg>unghosted</a><p>© <span data-year></span> <span data-cfg="legalName"></span></p></div>
<div><a href="{r}support.html">Support</a><br><a href="{r}legal/refunds.html">Refunds</a><br><a href="{r}legal/terms.html">Terms</a><br><a href="{r}legal/privacy.html">Privacy</a></div></div></footer>
</body></html>"""


CTA = """<div class="cta-box"><h2 style="margin-top:0;color:#fff">Free: 5 Texts That Win Back Missed Calls</h2>
<p>The five texts we'd set up first in any home-service business, plus a 5-minute setup guide.</p>
<a class="btn btn-primary" data-link="free" data-soon="Free guide: opening soon" href="#">Get the free guide</a>
<a class="btn btn-ghost" style="margin-left:8px" href="../index.html#pricing">See the full system</a></div>"""


def md(t):
    return markdown.markdown(t, extensions=["tables", "sane_lists"])


def main():
    urls = [("", "1.0")]
    for p in sorted((ROOT / "content" / "pages").glob("*.md")):
        meta, t = parse(p)
        depth = meta["slug"].count("/")
        out = SITE / f"{meta['slug']}.html"; out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(shell(meta, md(t), depth, "legal")); urls.append((f"{meta['slug']}.html", "0.3"))

    arts = []
    for p in sorted((ROOT / "marketing" / "seo" / "articles").glob("*.md")):
        meta, t = parse(p); meta["slug"] = "guides/" + meta["slug"]
        body = md(t)
        # insert CTA after the 2nd h2 and at the end
        parts = body.split("<h2", 3)
        if len(parts) == 4:
            body = parts[0] + "<h2" + parts[1] + "<h2" + parts[2] + CTA + "<h2" + parts[3]
        body = f'<div class="crumbs"><a href="./">Free guides</a></div><h1>{html.escape(meta["title"])}</h1>' + body + CTA
        ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":%s,'
              '"description":%s,"publisher":{"@type":"Organization","name":"Unghosted"},"datePublished":"%s"}</script>'
              % (repr_json(meta["title"]), repr_json(meta["description"]), date.today().isoformat()))
        (SITE / f"{meta['slug']}.html").write_text(shell(meta, body, 1, extra=ld))
        arts.append(meta); urls.append((f"{meta['slug']}.html", "0.8"))

    cards = "".join(f'<a class="card" style="text-decoration:none;color:inherit" href="{m["slug"].split("/")[1]}.html"><h3>{html.escape(m["title"])}</h3><p>{html.escape(m["description"])}</p></a>' for m in arts)
    idx = {"title": "Free Guides for Home Service Business Owners", "slug": "guides/index",
           "description": "Free, practical guides and templates: missed-call text back, quote follow-up, reviews, rebooking, referrals and maintenance plans."}
    (SITE / "guides").mkdir(exist_ok=True)
    (SITE / "guides" / "index.html").write_text(shell(idx, f'<span class="kicker">Free guides</span><h1>{idx["title"]}</h1><p class="lead">Copy-and-paste templates and plain-English playbooks for small home-service businesses.</p><div class="grid g2" style="margin-top:28px">{cards}</div>{CTA}', 1).replace(f'{DOMAIN}/guides/index.html', f'{DOMAIN}/guides/'))
    urls.append(("guides/", "0.7"))

    today = date.today().isoformat()
    sm = "".join(f"<url><loc>{DOMAIN}/{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>" for u, pr in urls)
    (SITE / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"site: {len(urls)} urls")


def repr_json(s):
    import json; return json.dumps(s)


if __name__ == "__main__":
    main()
