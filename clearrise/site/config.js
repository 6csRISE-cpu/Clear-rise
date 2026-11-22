/*
 * ClearRise site settings: the ONLY file the owner (or Claude) needs to edit to go live.
 * Paste each link from Payhip after creating the product. Empty links show "Opening soon".
 */
window.CLEARRISE = {
  links: {
    free:    "",  // Payhip $0 product: "5 Texts That Win Back Missed Calls"
    starter: "",  // Payhip product: Starter Kit, $27
    system:  "",  // Payhip product: Revenue Recovery System, $67
    pro:     "",  // Payhip product: Pro Bundle, $127
    club:    "",  // Payhip membership: Campaign Club, $19/mo
    clubYear:"",  // Payhip membership: Campaign Club annual, $159/yr
    support: "https://tally.so/r/db9DvD",  // Tally support form (live)
    affiliates: "", // Payhip affiliate sign-up link
    feedback: "https://tally.so/r/Yj4Mkz" // Tally feedback survey (live), used in email E
  },
  supportEmail: "support@clearrisetools.com",
  legalName: "[Owner legal name or business entity]",
  mailingAddress: "[Business mailing address, required in marketing emails]",
  governingState: "[State]",
  analyticsToken: "" // Cloudflare Web Analytics token (free). Leave empty to disable.
};

(function () {
  const c = window.CLEARRISE;
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-link]").forEach(function (a) {
      const url = c.links[a.dataset.link];
      if (url) { a.href = url; }
      else { a.removeAttribute("href"); a.classList.add("soon"); a.setAttribute("aria-disabled", "true"); a.title = "Opening soon"; if (a.dataset.soon) a.textContent = a.dataset.soon; }
    });
    document.querySelectorAll("[data-cfg]").forEach(function (el) { el.textContent = c[el.dataset.cfg] || ""; });
    document.querySelectorAll("[data-mail]").forEach(function (a) { a.href = "mailto:" + c.supportEmail; a.textContent = c.supportEmail; });
    document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    if (c.analyticsToken) {
      const s = document.createElement("script");
      s.defer = true; s.src = "https://static.cloudflareinsights.com/beacon.min.js";
      s.setAttribute("data-cf-beacon", JSON.stringify({ token: c.analyticsToken }));
      document.head.appendChild(s);
    }
  });
})();
