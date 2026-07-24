# Huzaifa Sheikh — Portfolio

A premium, dark-themed, animated portfolio built with React + Vite, Tailwind CSS, and Framer Motion.

## Getting started

```bash
npm install
npm run dev
```

Then open the printed local URL in your browser.

To build for production:

```bash
npm run build
npm run preview
```

## CV / Resume

Your CV is bundled at `public/Huzaifa_Sheikh_CV.pdf`. The Hero and Contact
sections each show two buttons:

- **View CV** — opens the PDF in a new browser tab
- **Download CV** — downloads it directly with the filename `Huzaifa_Sheikh_CV.pdf`

To replace it with an updated CV, just overwrite that file (keep the same
filename, or update `resumeUrl` in `src/data/data.js`).

## Editing content

All personal content (contact info, skills, experience, education, projects,
achievements) lives in one place: `src/data/data.js`. Update that file and
every section updates automatically.

## Contact form (EmailJS)

The contact form uses EmailJS so messages are sent without a backend.

1. Create a free account at https://www.emailjs.com
2. Create an Email Service and an Email Template
3. Open `src/components/Contact.jsx` and replace:
   - `EMAILJS_SERVICE_ID`
   - `EMAILJS_TEMPLATE_ID`
   - `EMAILJS_PUBLIC_KEY`

with the values from your EmailJS dashboard.

## Deploying

This is a static Vite app — it deploys as-is to Vercel, Netlify, GitHub Pages,
or any static host. Build with `npm run build` and deploy the generated
`dist/` folder.
