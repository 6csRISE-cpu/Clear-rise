#!/usr/bin/env bash
# Package product ZIPs for upload to Payhip. Run after build_products.py and render_pdfs.mjs.
set -euo pipefail
cd "$(dirname "$0")/../products/dist"
rm -rf pkg && mkdir -p pkg
mk() { # name, files...
  local name=$1; shift; local d="pkg/$name"; mkdir -p "$d"
  for f in "$@"; do cp "$f" "$d/"; done
  cat > "$d/READ-ME-FIRST.txt" <<TXT
Thanks for buying Unghosted!

1. Open the PDF first. It's the guide, start to finish.
2. The .docx files are editable copies (Word, Google Docs or Pages).
3. The .xlsx file is your tracker and scorecard (Excel or Google Sheets).
4. Templates-Import CSV = every template in one list, for bulk import into your texting/CRM app.

Need help? Reply to your purchase email. We answer within 2 business days.
Refunds: 30-day money-back guarantee, see unghostedhq.vercel.app/legal/refunds.html

License: for use in one business. Please don't resell or share the files.
TXT
  (cd pkg && zip -qr "$name.zip" "$name")
  echo "packaged $name.zip"
}
mk Unghosted-Ghost-Proof-Kit pdf/01-missed-call-and-quote-kit.pdf docx/01-missed-call-and-quote-kit.docx Unghosted-Follow-Up-Tracker.xlsx Templates-Import-Starter.csv
mk Unghosted-System pdf/01-missed-call-and-quote-kit.pdf pdf/02-revenue-recovery-system.pdf docx/01-missed-call-and-quote-kit.docx docx/02-revenue-recovery-system.docx Unghosted-Follow-Up-Tracker.xlsx Templates-Import-System.csv Customer-List-Template.csv
mk Unghosted-Pro-Bundle pdf/01-missed-call-and-quote-kit.pdf pdf/02-revenue-recovery-system.pdf pdf/03-trade-packs.pdf pdf/04-implementation-playbook.pdf docx/01-missed-call-and-quote-kit.docx docx/02-revenue-recovery-system.docx docx/03-trade-packs.docx docx/04-implementation-playbook.docx Unghosted-Follow-Up-Tracker.xlsx Templates-Import-Pro.csv Customer-List-Template.csv pdf/2026-12-december.pdf
for m in pdf/20*.pdf; do b=$(basename "$m" .pdf); mk "Unghosted-Ghost-Club-$b" "$m" "docx/$b.docx"; done
cp pdf/00-five-texts.pdf pkg/Unghosted-5-Texts-Free-Guide.pdf
ls -la pkg/*.zip pkg/*.pdf
