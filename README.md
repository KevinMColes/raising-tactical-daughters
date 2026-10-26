# Raising Tactical Daughters

Static five-page site, published with GitHub Pages at https://raisingtacticaldaughters.com/.

- Home: `/`
- Our Story: `/our-story/`
- Complete guide: `/raising-her-ready/`
- Community: `/community/`
- Speaking: `/speaking/`
- Field guide: `/downloads/raising-her-ready-field-guide.pdf`

Shared styling is in `assets/site.css`. Photographs and the original shield logo are in `images/`; optimized WebP photographs preserve the original content. No build step or third-party form service is required.

Speaking inquiries link to https://calendly.com/kevinmcoles/speaking.

Run `python scripts/check_site.py` to verify internal links, guide anchors, image metadata, structured data, and the 22-page PDF. The checker uses PyMuPDF for PDF validation.

Keep the CNAME file and `.nojekyll`. When changing shared CSS, update its version query in all five pages.
