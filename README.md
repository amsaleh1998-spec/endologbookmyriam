# Endo Logbook Builder (Myriam Maroun Karam)

A step-by-step web form that fills the Saint Joseph University endodontic clinical logbook and downloads it as a Word file. Works on phones and computers.

**Open the app:** https://amsaleh1998-spec.github.io/endologbookmyriam/

This copy pre-fills the cover page with Student full name **Myriam Maroun Karam** and Student ID **190219** (both can still be edited in the first step).

## Files

- `index.html` – the complete app (template embedded). This is what GitHub Pages serves.
- `src/app.html` – app source with a placeholder for the template.
- `src/template.docx` – the blank logbook template, with extra "checked box" list styles.
- `src/build.py` – embeds the template into the app: run `python3 src/build.py` after editing the source.
