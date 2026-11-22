#!/usr/bin/env python3
"""Build ops/Unghosted-Financial-Model.xlsx (live formulas) and print a scenario summary.
Every assumption is an editable blue cell on the Assumptions sheet."""
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

OUT = Path(__file__).resolve().parent.parent / "ops" / "Unghosted-Financial-Model.xlsx"
BLUE = Font(color="1F4FB4", bold=True); HDR = PatternFill("solid", fgColor="0F2A3D"); WH = Font(color="FFFFFF", bold=True)

# name, conservative, base, strong, format, note
A = [
    ("Prices", None, None, None, None, None),
    ("price_starter", 27, 27, 27, "$", "Ghost-Proof Kit"),
    ("price_system", 67, 67, 67, "$", "Unghosted System"),
    ("price_pro", 127, 127, 127, "$", "Pro Bundle"),
    ("price_club", 19, 19, 19, "$", "Ghost Club monthly"),
    ("Sales mix of one-time orders", None, None, None, None, None),
    ("mix_starter", .40, .35, .30, "%", "Share of orders"),
    ("mix_system", .45, .45, .45, "%", ""),
    ("mix_pro", .15, .20, .25, "%", "Must sum to 100% with the two above"),
    ("Traffic & conversion (monthly, at month 12)", None, None, None, None, None),
    ("visitors_m1", 300, 500, 800, "#", "Month 1 visitors (launch, communities, affiliates)"),
    ("visitor_growth", .15, .22, .30, "%", "Monthly growth in visitors (SEO compounding)"),
    ("conv_purchase", .008, .012, .018, "%", "Visitors who buy directly"),
    ("conv_optin", .04, .06, .08, "%", "Visitors who take the free guide"),
    ("optin_to_buy", .03, .05, .07, "%", "Free-guide subscribers who later buy"),
    ("buyer_to_club", .05, .08, .12, "%", "Buyers who join Ghost Club"),
    ("club_churn", .12, .09, .07, "%", "Club members cancelling per month"),
    ("Costs & leakage", None, None, None, None, None),
    ("payhip_fee", .05, .05, .05, "%", "Payhip free plan (switch to Plus $29/mo above ~$1,000/mo sales)"),
    ("processor_pct", .029, .029, .029, "%", "Stripe/PayPal card fee"),
    ("processor_fixed", .30, .30, .30, "$", "Per order"),
    ("refund_rate", .06, .05, .04, "%", "Share of revenue refunded"),
    ("affiliate_share", .30, .40, .50, "%", "Share of sales via partners/affiliates (partner-led launch)"),
    ("affiliate_rate", .30, .30, .30, "%", "Commission"),
    ("fixed_monthly", 2, 12, 25, "$", "Domain ($1) + email tool once list grows + misc"),
]


def main():
    wb = Workbook(); ws = wb.active; ws.title = "Assumptions"
    ws.append(["Assumption", "Conservative", "Base", "Strong", "Notes"])
    for c in ws[1]: c.fill, c.font = HDR, WH
    for w, col in zip([30, 14, 14, 14, 60], "ABCDE"): ws.column_dimensions[col].width = w
    ref = {}
    for name, c, b, s, fmt, note in A:
        if c is None:
            ws.append([name]); ws.cell(ws.max_row, 1).font = Font(bold=True, color="E8962E"); continue
        ws.append([name, c, b, s, note]); r = ws.max_row; ref[name] = r
        for col in (2, 3, 4):
            cell = ws.cell(r, col); cell.font = BLUE
            cell.number_format = {"$": '"$"#,##0.00', "%": "0.0%", "#": "#,##0"}[fmt]
    ws.append([]); ws.append(["Blue cells are inputs. Change them and every other sheet recalculates. These are planning estimates, not guaranteed results."])

    for si, (sname, col) in enumerate([("Conservative", "B"), ("Base", "C"), ("Strong", "D")]):
        m = wb.create_sheet(f"12mo {sname}")
        g = lambda k: f"Assumptions!${col}${ref[k]}"
        heads = ["Month", "Visitors", "Direct orders", "New subscribers", "Orders from email", "Total orders", "Avg order $",
                 "One-time sales $", "New club members", "Club members", "Club revenue $", "Gross revenue $", "Refunds $",
                 "Payhip + processor fees $", "Affiliate commissions $", "Fixed costs $", "Net profit $", "Cumulative profit $"]
        m.append(heads)
        for c in m[1]: c.fill, c.font = HDR, WH; c.alignment = Alignment(wrap_text=True)
        m.row_dimensions[1].height = 42
        for i in range(12):
            r = i + 2
            aov = f"({g('mix_starter')}*{g('price_starter')}+{g('mix_system')}*{g('price_system')}+{g('mix_pro')}*{g('price_pro')})"
            row = [
                i + 1,
                f"={g('visitors_m1')}*(1+{g('visitor_growth')})^(A{r}-1)",
                f"=B{r}*{g('conv_purchase')}",
                f"=B{r}*{g('conv_optin')}",
                f"={'D'+str(r-1) if r > 2 else 0}*{g('optin_to_buy')}",  # subscribers buy the following month
                f"=C{r}+E{r}",
                f"={aov}",
                f"=F{r}*G{r}",
                f"=F{r}*{g('buyer_to_club')}",
                f"={'J'+str(r-1) if r > 2 else 0}*(1-{g('club_churn')})+I{r}",
                f"=J{r}*{g('price_club')}",
                f"=H{r}+K{r}",
                f"=L{r}*{g('refund_rate')}",
                f"=L{r}*({g('payhip_fee')}+{g('processor_pct')})+(F{r}+J{r})*{g('processor_fixed')}",
                f"=(L{r}-M{r})*{g('affiliate_share')}*{g('affiliate_rate')}",
                f"={g('fixed_monthly')}",
                f"=L{r}-M{r}-N{r}-O{r}-P{r}",
                f"=Q{r}" if r == 2 else f"=R{r-1}+Q{r}",
            ]
            m.append(row)
            for ci in range(2, 19):
                m.cell(r, ci).number_format = '#,##0' if ci in (2, 3, 4, 5, 6, 9, 10) else '"$"#,##0'
        m.append(["Year 1", "=SUM(B2:B13)", "", "", "", "=SUM(F2:F13)", "", "=SUM(H2:H13)", "", "", "=SUM(K2:K13)", "=SUM(L2:L13)", "=SUM(M2:M13)", "=SUM(N2:N13)", "=SUM(O2:O13)", "=SUM(P2:P13)", "=SUM(Q2:Q13)", ""])
        for c in m[14]: c.font = Font(bold=True)
        for ci in range(2, 18): m.cell(14, ci).number_format = '"$"#,##0' if ci > 7 else '#,##0'
        for col_l in "ABCDEFGHIJKLMNOPQR": m.column_dimensions[col_l].width = 13
        m.freeze_panes = "B2"

    t = wb.create_sheet("Targets")
    t.column_dimensions["A"].width = 44; t.column_dimensions["B"].width = 18
    t.append(["What it takes to reach a monthly net profit target (Base assumptions)", ""]); t["A1"].font = Font(bold=True, size=13)
    t.append(["Target monthly net profit", 3000]); t["B2"].font = BLUE; t["B2"].number_format = '"$"#,##0'
    t.append(["Net margin per $ of one-time sales", f"=1-Assumptions!C{ref['refund_rate']}-Assumptions!C{ref['payhip_fee']}-Assumptions!C{ref['processor_pct']}-(1-Assumptions!C{ref['refund_rate']})*Assumptions!C{ref['affiliate_share']}*Assumptions!C{ref['affiliate_rate']}"])
    t["B3"].number_format = "0.0%"
    t.append(["Average order value", "='12mo Base'!G2"]); t["B4"].number_format = '"$"#,##0.00'
    t.append(["Net profit per order", f"=B4*B3-Assumptions!C{ref['processor_fixed']}"]); t["B5"].number_format = '"$"#,##0.00'
    t.append(["Orders per month needed (no club)", f"=(B2+Assumptions!C{ref['fixed_monthly']})/B5"]); t["B6"].number_format = '#,##0'
    t.append(["Visitors per month needed (direct + email)", f"=B6/(Assumptions!C{ref['conv_purchase']}+Assumptions!C{ref['conv_optin']}*Assumptions!C{ref['optin_to_buy']})"]); t["B7"].number_format = '#,##0'
    t.append(["Break-even orders per month (fixed costs only)", f"=Assumptions!C{ref['fixed_monthly']}/B5"]); t["B8"].number_format = '0.0'
    wb.save(OUT)

    # print python-computed summary (mirrors the formulas) for docs
    for idx, sname in enumerate(["Conservative", "Base", "Strong"]):
        v = {n: (c, b, s)[idx] for n, c, b, s, *_ in A if c is not None}
        aov = v["mix_starter"] * v["price_starter"] + v["mix_system"] * v["price_system"] + v["mix_pro"] * v["price_pro"]
        subs_prev, club, cum, tot = 0, 0, 0, {"gross": 0, "net": 0, "orders": 0}
        snap = {}
        for mth in range(1, 13):
            vis = v["visitors_m1"] * (1 + v["visitor_growth"]) ** (mth - 1)
            orders = vis * v["conv_purchase"] + subs_prev * v["optin_to_buy"]
            subs_prev = vis * v["conv_optin"]
            club = club * (1 - v["club_churn"]) + orders * v["buyer_to_club"]
            gross = orders * aov + club * v["price_club"]
            refunds = gross * v["refund_rate"]
            fees = gross * (v["payhip_fee"] + v["processor_pct"]) + (orders + club) * v["processor_fixed"]
            aff = (gross - refunds) * v["affiliate_share"] * v["affiliate_rate"]
            net = gross - refunds - fees - aff - v["fixed_monthly"]
            cum += net; tot["gross"] += gross; tot["net"] += net; tot["orders"] += orders
            if mth in (3, 6, 12): snap[mth] = (round(vis), round(orders), round(club), round(gross), round(net))
        print(sname, "AOV", round(aov, 2), "snap(m: visitors, orders, club, gross, net)", snap,
              "Y1 gross", round(tot["gross"]), "Y1 net", round(tot["net"]), "Y1 orders", round(tot["orders"]))


if __name__ == "__main__":
    main()
