#!/usr/bin/env python3
"""Verify every product ZIP contains exactly the files the customer paid for, that every PDF renders,
spreadsheets open, CSVs carry message types, and no old branding leaks into deliverables.
Usage: python3 tools/test_packages.py → exits 1 on failure; writes ops/qa/package-results.json"""
import csv, io, json, subprocess, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
PKG = ROOT / "products" / "dist" / "pkg"
COMMON = {"READ-ME-FIRST.txt", "Unghosted-Follow-Up-Tracker.xlsx"}
KIT = {"00-texting-rules.pdf", "01-missed-call-and-quote-kit.pdf", "01-missed-call-and-quote-kit.docx", "Templates-Import-Starter.csv"}
SYSTEM = {"00-texting-rules.pdf", "01-missed-call-and-quote-kit.pdf", "02-revenue-recovery-system.pdf", "01-missed-call-and-quote-kit.docx",
          "02-revenue-recovery-system.docx", "Templates-Import-System.csv", "Customer-List-Template.csv"}
PRO = {"00-texting-rules.pdf", "01-missed-call-and-quote-kit.pdf", "02-revenue-recovery-system.pdf", "03-trade-packs.pdf", "04-implementation-playbook.pdf",
       "01-missed-call-and-quote-kit.docx", "02-revenue-recovery-system.docx", "03-trade-packs.docx", "04-implementation-playbook.docx",
       "Templates-Import-Pro.csv", "Customer-List-Template.csv", "2026-12-december.pdf"}
EXPECTED = {
    "Unghosted-Ghost-Proof-Kit.zip": KIT | COMMON,
    "Unghosted-System.zip": SYSTEM | COMMON,
    "Unghosted-Pro-Bundle.zip": PRO | COMMON,
    "Unghosted-Partner-License.zip": PRO | COMMON | {"PARTNER-LICENSE.txt"},
}
results = []
def ok(name, passed, detail=""):
    results.append({"name": name, "pass": bool(passed), "detail": detail})
    if not passed: print("FAIL", name, detail)

for z, want in EXPECTED.items():
    p = PKG / z
    ok(f"{z}: exists", p.exists())
    if not p.exists(): continue
    with zipfile.ZipFile(p) as zf:
        names = {Path(n).name for n in zf.namelist() if not n.endswith("/")}
        ok(f"{z}: exact file list", names == want, f"missing={sorted(want-names)} extra={sorted(names-want)}")
        for n in zf.namelist():
            data = zf.read(n) if not n.endswith("/") else b""
            if n.endswith(".pdf"):
                r = subprocess.run(["pdfinfo", "-"], input=data, capture_output=True)
                pages = next((int(l.split()[-1]) for l in r.stdout.decode().splitlines() if l.startswith("Pages:")), 0)
                ok(f"{z}/{Path(n).name}: PDF renders (pages={pages})", pages >= 2)
                txt = subprocess.run(["pdftotext", "-", "-"], input=data, capture_output=True).stdout.decode(errors="ignore")
                ok(f"{z}/{Path(n).name}: no old brand", "clearrise" not in txt.lower())
            if n.endswith(".xlsx"):
                wb = load_workbook(io.BytesIO(data)); ok(f"{z}/{Path(n).name}: workbook opens with Scorecard", "Scorecard" in wb.sheetnames)
            if n.endswith(".csv") and "Templates" in n:
                rows = list(csv.DictReader(io.StringIO(data.decode())))
                ok(f"{z}/{Path(n).name}: {len(rows)} templates, all typed", rows and all(r["message_type"] for r in rows))

for z in sorted(PKG.glob("Unghosted-Ghost-Club-*.zip")):
    with zipfile.ZipFile(z) as zf:
        names = {Path(n).name for n in zf.namelist() if not n.endswith("/")}
        ok(f"{z.name}: pack PDF + DOCX + readme", any(n.endswith(".pdf") for n in names) and any(n.endswith(".docx") for n in names) and "READ-ME-FIRST.txt" in names, sorted(names))
free = PKG / "Unghosted-5-Texts-Free-Guide.pdf"
ok("free guide PDF exists", free.exists())

# Docx deliverables: no old brand
for d in (ROOT / "products" / "dist" / "docx").glob("*.docx"):
    with zipfile.ZipFile(d) as zf:
        ok(f"{d.name}: no old brand", b"clearrise" not in zf.read("word/document.xml").lower())

failed = [r for r in results if not r["pass"]]
(ROOT / "ops" / "qa").mkdir(parents=True, exist_ok=True)
(ROOT / "ops" / "qa" / "package-results.json").write_text(json.dumps({"ran": datetime.now(timezone.utc).isoformat(), "total": len(results), "failed": len(failed), "results": results}, indent=1))
print(f"package checks: {len(results)-len(failed)}/{len(results)} passed")
sys.exit(1 if failed else 0)
