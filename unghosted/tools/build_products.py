#!/usr/bin/env python3
"""Build Unghosted product files from Markdown sources.

Outputs (in products/dist/):
  html/<name>.html   print-ready HTML (rendered to PDF by render_pdfs.mjs)
  docx/<name>.docx   editable Word versions (via pandoc)
  Templates-Import.csv   every template, one row each, for bulk import
  Customer-List-Template.csv
  Unghosted-Follow-Up-Tracker.xlsx  tracker + scorecard with formulas

Run:  python3 tools/build_products.py && node tools/render_pdfs.mjs && bash tools/package.sh
"""
import csv, html, re, subprocess, sys
from pathlib import Path

import markdown
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "products" / "src"
DIST = ROOT / "products" / "dist"
(DIST / "html").mkdir(parents=True, exist_ok=True)
(DIST / "docx").mkdir(parents=True, exist_ok=True)

INK, ACCENT, TEAL, PAPER = "#111111", "#D7FF3A", "#2B3BFF", "#F3EFE6"

CSS = f"""
@page {{ size: Letter; margin: 0.75in 0.8in 0.8in; }}
* {{ box-sizing: border-box; }}
body.compact h1 {{ page-break-before: auto; margin-top: 22px; }}
body {{ font-family: Inter, 'DejaVu Sans', sans-serif; color: {INK}; font-size: 10.5pt; line-height: 1.55; margin: 0; }}
.cover {{ height: 9.2in; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always;
  background: radial-gradient(500px 300px at 90% 0%, rgba(215,255,58,.35), transparent 60%), {INK}; color: #fff; padding: 0.9in 0.7in; border-radius: 6px; }}
.cover .brand {{ font-weight: 900; letter-spacing: -.02em; font-size: 18pt; display:flex; align-items:center; gap:10px; }}
.cover .brand svg {{ width: 30px; height: 30px; }}
.cover .title {{ font-weight:900; font-family: 'Inter Display', Inter, sans-serif; font-size: 42pt; line-height: 1.0; letter-spacing: -.03em; margin: 0 0 14px; border: 0; color: #fff; padding: 0; }}
.cover .sub {{ font-size: 15pt; opacity: .88; max-width: 5in; }}
.cover .product {{ display:inline-block; font-family: 'JetBrains Mono', monospace; font-size: 9.5pt; text-transform: uppercase; letter-spacing: .04em; color: {INK}; background: {ACCENT}; padding: 3px 8px; border-radius: 3px; font-weight: 700; margin-bottom: 18px; }}
.cover .foot {{ font-size: 9pt; opacity: .7; }}
h1 {{ font-family: 'Inter Display', Inter, sans-serif; font-weight: 900; letter-spacing: -.02em; font-size: 22pt; color: {INK}; margin: 0 0 12px; padding-top: 4px; border-bottom: 6px solid {ACCENT}; padding-bottom: 6px; page-break-before: always; }}
.content > h1:first-child {{ page-break-before: avoid; }}
h2 {{ font-size: 14pt; color: {TEAL}; margin: 20px 0 8px; }}
h3 {{ font-size: 11.5pt; margin: 16px 0 6px; color: {INK}; page-break-after: avoid; }}
p {{ margin: 6px 0; }}
blockquote {{ margin: 8px 0 12px; padding: 10px 14px; background: {PAPER}; border: 1.5px solid {INK}; border-left: 7px solid {INK}; border-radius: 6px; page-break-inside: avoid; }}
blockquote p {{ margin: 3px 0; }}
code {{ font-family: 'JetBrains Mono', monospace; font-size: 9pt; background: #EEF3F5; padding: 1px 4px; border-radius: 3px; }}
table {{ border-collapse: collapse; width: 100%; margin: 10px 0 14px; font-size: 9.5pt; page-break-inside: avoid; }}
th {{ background: {INK}; color: #fff; text-align: left; padding: 6px 8px; font-weight: 600; }}
td {{ border-bottom: 1px solid #DDE3E7; padding: 6px 8px; vertical-align: top; }}
tr:nth-child(even) td {{ background: #F6F8F9; }}
hr {{ border: 0; border-top: 1px solid #DDE3E7; margin: 18px 0; }}
ul, ol {{ padding-left: 22px; margin: 6px 0; }}
li {{ margin: 3px 0; }}
strong {{ color: {INK}; }}
a {{ color: {TEAL}; }}
"""

FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse(path: Path):
    text = path.read_text()
    meta = {}
    m = FRONT.match(text)
    if m:
        for line in m.group(1).splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        text = text[m.end():]
    return meta, text


def render_html(meta, body_md):
    body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists"])
    t = html.escape
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{t(meta.get('title',''))}</title>
<style>{CSS}</style></head><body class="{'compact' if meta.get('compact') else ''}">
<section class="cover"><div class="brand"><svg viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10v11.2c0 .7.8 1 1.3.5l1.9-1.9 1.9 1.9c.4.4 1 .4 1.4 0L12 20l1.5 1.7c.4.4 1 .4 1.4 0l1.9-1.9 1.9 1.9c.5.5 1.3.2 1.3-.5V10c0-4.4-3.6-8-8-8z" fill="#D7FF3A"/><circle cx="9.2" cy="10" r="1.7" fill="#111"/><circle cx="14.8" cy="10" r="1.7" fill="#111"/></svg>unghosted</div>
<div><div class="product">{t(meta.get('product',''))}</div><div class="title">{t(meta.get('title',''))}</div>
<div class="sub">{t(meta.get('subtitle',''))}</div></div>
<div class="foot">© 2026 Unghosted · unghostedhq.vercel.app · Licensed for one business. Don't resell it, don't share it. Ghosting us isn't cool either.<br>
This guide is practical business guidance, not legal advice.</div></section>
<main class="content">{body}</main></body></html>"""


def extract_templates(name, body_md):
    """Pull every blockquote template, named by its nearest heading."""
    rows, heading, buf, mtype = [], "", [], ""
    skip_prefixes = ("**Fill-Ins", "**Before you", "**Why", "**Consent", "**Seasons", "**Fill-ins")

    def flush():
        if buf:
            txt = " ".join(s.strip() for s in buf).strip()
            if txt and not txt.startswith(skip_prefixes) and not txt.startswith("**") and heading != "AI Prompt Pack" and name != "The Texting Rules":
                low = (heading + " " + txt).lower()
                channel = "Email" if ("email" in low or "subject" in low) else ("Phone" if "call" in heading.lower() or "script" in low or "voicemail" in low else "Text")
                rows.append({"source": name, "name": heading, "channel": channel, "message_type": mtype, "text": txt})
            buf.clear()

    for line in body_md.splitlines():
        if line.startswith("# "):
            flush(); heading = line.lstrip("#").strip(); mtype = ""
            if heading.startswith("Part 1"): mtype = "1 Reply"
            if "Phone Scripts" in heading or "Staff Scripts" in heading: mtype = "Live call"
        elif line.startswith("#"):
            flush(); heading = line.lstrip("#").strip()
        elif line.startswith("**Message type →"):
            flush(); m2 = re.match(r"\*\*Message type → (\d) · (\w+)", line); mtype = f"{m2.group(1)} {m2.group(2)}" if m2 else mtype
        elif line.startswith(">"):
            buf.append(line[1:].strip() or "\n")
        else:
            flush()
            low = line.strip().lower()
            if low.startswith("**missed-call text"): mtype = "1 Reply"
            elif low.startswith("**quote angle") or low.startswith("**top objections"): mtype = "2 Service"
            elif low.startswith("**seasonal campaign"): mtype = "3 Marketing"
            m = re.match(r"- \*(Text|Email subject)\:\*\s*[\"“]([^\"”]*)", line.strip())
            if m:
                rows.append({"source": name, "name": heading, "channel": "Text" if m.group(1) == "Text" else "Email", "message_type": "3 Marketing", "text": m.group(2).strip()})
    flush()
    return rows


def build_xlsx(path: Path):
    wb = Workbook()
    hdr_fill = PatternFill("solid", fgColor="0F2A3D")
    hdr_font = Font(bold=True, color="FFFFFF")
    thin = Side(style="thin", color="DDE3E7")

    def header(ws, cols, widths):
        ws.append(cols)
        for i, c in enumerate(ws[1], 1):
            c.fill, c.font = hdr_fill, hdr_font
            c.alignment = Alignment(vertical="center", wrap_text=True)
            ws.column_dimensions[c.column_letter].width = widths[i - 1]
        ws.freeze_panes = "A2"
        ws.row_dimensions[1].height = 30

    # 1. Start Here
    ws = wb.active; ws.title = "Start Here"
    lines = [
        ("Unghosted Follow-Up Tracker & Scorecard", Font(bold=True, size=16, color="0F2A3D")),
        ("", None),
        ("1. 'Leads & Quotes' — log every missed call and quote. Tick each touch as you send it.", None),
        ("2. 'Rebooking' — paste this month's past-customer list; mark who you contacted and who booked.", None),
        ("3. 'Scorecard' — fills itself in from the other tabs. Check it on the 1st of each month.", None),
        ("", None),
        ("Tip: in Google Sheets use File > Import to open this file. Everything still works.", Font(italic=True, color="1F6F80")),
    ]
    for text, f in lines:
        ws.append([text])
        if f: ws.cell(ws.max_row, 1).font = f
    ws.column_dimensions["A"].width = 100

    # 2. Leads & Quotes
    ws = wb.create_sheet("Leads & Quotes")
    cols = ["Date", "Name", "Phone", "Source", "Job", "Quote $", "Missed call?", "T1", "T2", "T3", "T4", "T5", "Result", "Won $", "Notes"]
    header(ws, cols, [12, 18, 15, 14, 22, 10, 12, 6, 6, 6, 6, 6, 11, 10, 30])
    dv_yn = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
    dv_tick = DataValidation(type="list", formula1='"✓"', allow_blank=True)
    dv_res = DataValidation(type="list", formula1='"Open,Won,Lost,Later"', allow_blank=True)
    dv_src = DataValidation(type="list", formula1='"Missed call,Phone,Website,Google,Referral,Repeat,Other"', allow_blank=True)
    for dv in (dv_yn, dv_tick, dv_res, dv_src): ws.add_data_validation(dv)
    dv_yn.add("G2:G500"); dv_tick.add("H2:L500"); dv_res.add("M2:M500"); dv_src.add("D2:D500")
    for r in range(2, 501):
        ws.cell(r, 1).number_format = "yyyy-mm-dd"
        ws.cell(r, 6).number_format = ws.cell(r, 14).number_format = '"$"#,##0'

    # 3. Rebooking
    ws = wb.create_sheet("Rebooking")
    header(ws, ["Name", "Phone", "Email", "Texts OK?", "Last job", "Last job date", "Contacted (date)", "Booked?", "Booked $", "Notes"],
           [18, 15, 24, 10, 20, 13, 15, 9, 10, 30])
    dv2 = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True); ws.add_data_validation(dv2)
    dv2.add("D2:D1000"); dv2.add("H2:H1000")
    for r in range(2, 1001):
        ws.cell(r, 6).number_format = ws.cell(r, 7).number_format = "yyyy-mm-dd"
        ws.cell(r, 9).number_format = '"$"#,##0'

    # 4. Other wins
    ws = wb.create_sheet("Other Wins")
    header(ws, ["Date", "Type", "Customer", "Value $", "Notes"], [12, 24, 20, 10, 40])
    dv3 = DataValidation(type="list", formula1='"Cancellation saved,Referral job,New review,Plan member joined,Plan member cancelled"', allow_blank=True)
    ws.add_data_validation(dv3); dv3.add("B2:B1000")
    for r in range(2, 1001):
        ws.cell(r, 1).number_format = "yyyy-mm-dd"; ws.cell(r, 4).number_format = '"$"#,##0'

    # 5. Scorecard (all-time, formula-driven)
    ws = wb.create_sheet("Scorecard")
    ws.column_dimensions["A"].width = 34; ws.column_dimensions["B"].width = 16; ws.column_dimensions["C"].width = 60
    ws.append(["Metric", "Value", "How it's calculated"])
    for c in ws[1]: c.fill, c.font = hdr_fill, hdr_font
    L, R, O = "'Leads & Quotes'", "Rebooking", "'Other Wins'"
    rows = [
        ("Missed calls logged", f'=COUNTIF({L}!G2:G500,"Yes")', "Leads with Missed call? = Yes", "0"),
        ("Missed calls won", f'=COUNTIFS({L}!G2:G500,"Yes",{L}!M2:M500,"Won")', "Missed-call leads marked Won", "0"),
        ("Missed-call recovery rate", "=IFERROR(B3/B2,0)", "Won ÷ logged", "0%"),
        ("Quotes sent", f'=COUNTIF({L}!F2:F500,">0")', "Rows with a quote amount", "0"),
        ("Quotes won", f'=COUNTIFS({L}!F2:F500,">0",{L}!M2:M500,"Won")', "Quoted rows marked Won", "0"),
        ("Quote close rate", "=IFERROR(B6/B5,0)", "Won ÷ sent", "0%"),
        ("Past customers contacted", f'=COUNTA({R}!G2:G1000)', "Rows with a contacted date", "0"),
        ("Rebooked", f'=COUNTIF({R}!H2:H1000,"Yes")', "Booked? = Yes", "0"),
        ("Rebooking rate", "=IFERROR(B9/B8,0)", "Rebooked ÷ contacted", "0%"),
        ("Cancellations saved", f'=COUNTIF({O}!B2:B1000,"Cancellation saved")', "From Other Wins", "0"),
        ("Referral jobs", f'=COUNTIF({O}!B2:B1000,"Referral job")', "From Other Wins", "0"),
        ("New reviews", f'=COUNTIF({O}!B2:B1000,"New review")', "From Other Wins", "0"),
        ("Plan members (net)", f'=COUNTIF({O}!B2:B1000,"Plan member joined")-COUNTIF({O}!B2:B1000,"Plan member cancelled")', "Joined − cancelled", "0"),
        ("RECOVERED REVENUE", f'=SUM({L}!N2:N500)+SUM({R}!I2:I1000)+SUM({O}!D2:D1000)', "Won $ + Booked $ + Other Wins value", '"$"#,##0'),
    ]
    for name, f, how, fmt in rows:
        ws.append([name, f, how]); ws.cell(ws.max_row, 2).number_format = fmt
        for c in ws[ws.max_row]: c.border = Border(bottom=thin)
    ws.cell(ws.max_row, 1).font = Font(bold=True, color="E8962E", size=13)
    ws.cell(ws.max_row, 2).font = Font(bold=True, size=13)
    wb.save(path)


def main():
    all_templates = []
    order = {"free": 0, "starter": 1, "system": 2, "pro": 3, "club": 4}
    sources = sorted(SRC.rglob("*.md"), key=lambda q: (order.get(q.parent.name, 9), q.name))
    for p in sources:
        meta, body = parse(p)
        name = p.stem
        (DIST / "html" / f"{name}.html").write_text(render_html(meta, body))
        subprocess.run(["pandoc", "-f", "markdown", "-t", "docx", "--metadata", f"title={meta.get('title','')}",
                        "-o", str(DIST / "docx" / f"{name}.docx"), "-"], input=body.encode(), check=True)
        if p.parent.name in ("starter", "system", "pro", "club"):
            for row in extract_templates(meta.get("title", name), body):
                row["tier"] = p.parent.name; all_templates.append(row)

    tiers = {"Starter": {"starter"}, "System": {"starter", "system"}, "Pro": {"starter", "system", "pro"}}
    for label, keep in tiers.items():
        with open(DIST / f"Templates-Import-{label}.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["source", "name", "channel", "message_type", "text"], extrasaction="ignore"); w.writeheader()
            w.writerows(r for r in all_templates if r["tier"] in keep)
    with open(DIST / "Customer-List-Template.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["first_name", "last_name", "phone", "email", "texts_ok", "address", "last_job", "last_job_date", "last_job_value", "plan_member", "notes"])
        w.writerow(["Sam", "Example", "555-0100", "sam@example.com", "Yes", "12 Sample St", "AC tune-up", "2026-05-14", "149", "No", "Delete this example row"])
    build_xlsx(DIST / "Unghosted-Follow-Up-Tracker.xlsx")
    print(f"Built {len(sources)} guides, {len(all_templates)} templates")


if __name__ == "__main__":
    sys.exit(main())
