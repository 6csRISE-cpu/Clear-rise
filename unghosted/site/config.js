/*
 * Unghosted site settings: the ONLY file the owner (or Claude) needs to edit to go live.
 * Paste each link from Payhip after creating the product. Empty links show "Opening soon".
 */
window.UNGHOSTED = {
  // Paid buttons stay "Opening soon" until this is true. Turn on ONLY after hosting with clear
  // commercial-use terms is in place (Vercel Hobby is non-commercial) and the E2E tests pass.
  sellingEnabled: false,
  links: {
    free:    "https://payhip.com/b/9QTX8",  // Payhip $0 product: "5 Texts That Win Back Missed Calls" (added Nov 23, 2026)
    starter: "https://payhip.com/b/6D8Lo",  // Payhip product: Ghost-Proof Kit, $27 (added Nov 23, 2026)
    system:  "",  // Payhip product: Unghosted System, $67
    pro:     "",  // Payhip product: Pro Bundle, $127
    club:    "",  // Payhip membership: Ghost Club, $19/mo
    clubYear:"",  // Payhip membership: Ghost Club annual, $159/yr
    support: "https://tally.so/r/db9DvD",  // Tally support form (live)
    affiliates: "", // Payhip affiliate sign-up link (sent to approved partners)
    partnerApply: "https://tally.so/r/KpVJZX", // Tally partner application (live)
    partnerLicense: "", // Payhip Partner License product ($297)
    feedback: "https://tally.so/r/Yj4Mkz" // Tally feedback survey (live), used in email E
  },
  supportEmail: "",  // e.g. "support@unghostedhq.com" once the domain + email forwarding exist; empty = links go to the support form
  legalName: "[Owner legal name or business entity]",
  mailingAddress: "[Business mailing address, required in marketing emails]",
  governingState: "[State]",
  analyticsToken: "" // Cloudflare Web Analytics token (free). Leave empty to disable.
};

(function () {
  const c = window.UNGHOSTED;
  document.addEventListener("DOMContentLoaded", function () {
    const PAID = ["starter", "system", "pro", "club", "clubYear", "partnerLicense"];
    document.querySelectorAll("[data-link]").forEach(function (a) {
      const key = a.dataset.link;
      const url = (PAID.indexOf(key) > -1 && !c.sellingEnabled) ? "" : c.links[key];
      if (url) { a.href = url; }
      else { a.removeAttribute("href"); a.classList.add("soon"); a.setAttribute("aria-disabled", "true"); a.title = "Opening soon"; if (a.dataset.soon) a.textContent = a.dataset.soon; }
    });
    document.querySelectorAll("[data-cfg]").forEach(function (el) { el.textContent = c[el.dataset.cfg] || ""; });
    document.querySelectorAll("[data-mail]").forEach(function (a) {
      if (c.supportEmail) { a.href = "mailto:" + c.supportEmail; a.textContent = c.supportEmail; }
      else { a.href = c.links.support; a.textContent = "our support form"; a.target = "_blank"; a.rel = "noopener"; }
    });
    document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    if (c.analyticsToken) {
      const s = document.createElement("script");
      s.defer = true; s.src = "https://static.cloudflareinsights.com/beacon.min.js";
      s.setAttribute("data-cf-beacon", JSON.stringify({ token: c.analyticsToken }));
      document.head.appendChild(s);
    }
  });
})();
