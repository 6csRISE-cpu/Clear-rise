#!/usr/bin/env python3
"""Build ops/Owner-Dashboard.xlsx: a one-page monthly log with KPIs auto-calculated and checked against targets."""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.formatting.rule import FormulaRule

OUT = Path(__file__).resolve().parent.parent / "ops" / "Owner-Dashboard.xlsx"
HDR = PatternFill("solid", fgColor="0F2A3D"); WH = Font(color="FFFFFF", bold=True); BLUE = Font(color="1F4FB4")
GOOD = PatternFill("solid", fgColor="DDF2E5"); BAD = PatternFill("solid", fgColor="FBE3D6")

wb = Workbook()
log = wb.active; log.title = "Monthly Log"
inputs = [("Month", "Where to find it"), ("Visitors", "Cloudflare → Web Analytics"), ("Free-guide downloads", "Payhip → free product sales"),
          ("Kit orders", "Payhip → Analytics"), ("System orders", "Payhip"), ("Pro orders", "Payhip"), ("New Club members", "Payhip → Memberships"),
          ("Club cancellations", "Payhip → Memberships"), ("Active Club members (end)", "Payhip → Memberships"), ("Gross revenue $", "Payhip → Analytics"),
          ("Refunds $", "Payhip → Sales (refunded)"), ("Payhip + processor fees $", "Payhip/Stripe/PayPal reports"), ("Affiliate payouts $", "Payhip → Affiliates"),
          ("Tools & other costs $", "Your card statement"), ("Email open rate %", "MailerLite → Reports"), ("Support tickets", "Inbox + Tally")]
log.append([h for h, _ in inputs]); log.append([w for _, w in inputs])
for c in log[1]: c.fill, c.font = HDR, WH; c.alignment = Alignment(wrap_text=True)
for c in log[2]: c.font = Font(italic=True, color="6B7F8C", size=9); c.alignment = Alignment(wrap_text=True)
log.row_dimensions[1].height = 34; log.row_dimensions[2].height = 30
for i, col in enumerate("ABCDEFGHIJKLMNOP"): log.column_dimensions[col].width = 14
months = ["Dec 2026", "Jan 2027", "Feb 2027", "Mar 2027", "Apr 2027", "May 2027", "Jun 2027", "Jul 2027", "Aug 2027", "Sep 2027", "Oct 2027", "Nov 2027"]
for m in months:
    log.append([m] + [None] * 15)
    r = log.max_row
    for ci in range(2, 17):
        c = log.cell(r, ci); c.font = BLUE
        c.number_format = '"$"#,##0' if 10 <= ci <= 14 else ("0.0%" if ci == 15 else "#,##0")
log.freeze_panes = "B3"

k = wb.create_sheet("KPIs", 0)
k.column_dimensions["A"].width = 30
for col in "BCDEFGHIJKLM": k.column_dimensions[col].width = 11
k.append(["Unghosted Owner Dashboard"]); k["A1"].font = Font(bold=True, size=16, color="0F2A3D")
k.append(["Fill in blue cells on 'Monthly Log'. Green = on/above target, orange = below. Targets are Base-case planning assumptions, adjust in column N."])
k["A2"].font = Font(italic=True, color="6B7F8C")
k.append(["KPI"] + months + ["Target"])
for c in k[3]: c.fill, c.font = HDR, WH
L = "'Monthly Log'!"
kpis = [
    ("Net profit $", lambda r: f"=IF({L}J{r}=\"\",\"\",{L}J{r}-{L}K{r}-{L}L{r}-{L}M{r}-{L}N{r})", '"$"#,##0', 500, ">="),
    ("Orders (one-time)", lambda r: f"=IF({L}J{r}=\"\",\"\",{L}D{r}+{L}E{r}+{L}F{r})", "#,##0", 10, ">="),
    ("Avg order value $", lambda r: f"=IFERROR(({L}D{r}*27+{L}E{r}*67+{L}F{r}*127)/({L}D{r}+{L}E{r}+{L}F{r}),\"\")", '"$"#,##0', 60, ">="),
    ("Visitor → buyer %", lambda r: f"=IFERROR(({L}D{r}+{L}E{r}+{L}F{r})/{L}B{r},\"\")", "0.0%", 0.012, ">="),
    ("Visitor → free guide %", lambda r: f"=IFERROR({L}C{r}/{L}B{r},\"\")", "0.0%", 0.05, ">="),
    ("Refund rate %", lambda r: f"=IFERROR({L}K{r}/{L}J{r},\"\")", "0.0%", 0.06, "<="),
    ("Club members", lambda r: f"=IF({L}I{r}=\"\",\"\",{L}I{r})", "#,##0", 10, ">="),
    ("Club churn %", lambda r: f"=IFERROR({L}H{r}/({L}I{r}+{L}H{r}-{L}G{r}),\"\")", "0.0%", 0.10, "<="),
    ("Recurring revenue (MRR) $", lambda r: f"=IF({L}I{r}=\"\",\"\",{L}I{r}*19)", '"$"#,##0', 200, ">="),
    ("Email open rate %", lambda r: f"=IF({L}O{r}=\"\",\"\",{L}O{r})", "0.0%", 0.35, ">="),
    ("Support tickets", lambda r: f"=IF({L}P{r}=\"\",\"\",{L}P{r})", "#,##0", 15, "<="),
]
for name, f, fmt, target, op in kpis:
    row = [name] + [f(i + 3) for i in range(12)] + [target]
    k.append(row); r = k.max_row
    for ci in range(2, 15): k.cell(r, ci).number_format = fmt
    k.cell(r, 14).font = BLUE
    rng = f"B{r}:M{r}"
    k.conditional_formatting.add(rng, FormulaRule(formula=[f'AND(B{r}<>"",B{r}{op}$N{r})'], fill=GOOD))
    k.conditional_formatting.add(rng, FormulaRule(formula=[f'AND(B{r}<>"",NOT(B{r}{op}$N{r}))'], fill=BAD))
k.freeze_panes = "B4"
k.append([]); k.append(["Rule of thumb: fix the single worst orange number each month. Don't redesign anything that's green."])
k.cell(k.max_row, 1).font = Font(bold=True, color="C77412")
wb.save(OUT); print("dashboard ok")
