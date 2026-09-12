# Comics

This folder is for the reader-facing graphic version of `Seven Minutes After Midnight`.

Use it for generated chapter covers and interior comic pages after a chapter has been adapted from prose into page-and-panel ChatGPT image prompts.

Chapter front and back covers are colored time-slip BL railway romance manga/manhwa/manhua cover illustrations. Interior pages are black-and-white time-slip railway romance manga/manhwa/manhua manuscript pages.

## Intended Structure

Use an arc/season folder before every chapter folder. Do not add bare chapter-number folders directly under `Comics`.

```text
Comics/
  style-guide.md
  01-Arc-Or-Season-Name-In-Camel-Case/
    README.md
    Chapter-01-Title-Of-The-Chapter-In-Camel-Case/
      chapter.md
      chapter-01-front-cover-chatgpt-image-prompt.md
      front.webp
      page-001-chatgpt-image-prompt.md
      1.webp
      page-002-chatgpt-image-prompt.md
      2.webp
      chapter-01-back-cover-chatgpt-image-prompt.md
      back.webp
    Chapter-02-Title-Of-The-Chapter-In-Camel-Case/
      chapter.md
      page-001-chatgpt-image-prompt.md
      1.webp
  02-Arc-Or-Season-Name-In-Camel-Case/
    README.md
    Chapter-01-Title-Of-The-Chapter-In-Camel-Case/
      chapter.md
      page-001-chatgpt-image-prompt.md
      1.webp
    Chapter-02-Title-Of-The-Chapter-In-Camel-Case/
      chapter.md
      page-001-chatgpt-image-prompt.md
      1.webp
```

## Naming Rules

- Arc/season folder format: `01-Arc-Or-Season-Name-In-Camel-Case`, `02-Arc-Or-Season-Name-In-Camel-Case`, etc.
- Each arc/season folder contains a `README.md` with the readable arc title and chapter list.
- Use either `Arc` or `Season` in the folder name. Do not type `Arc/Season`, because `/` creates another directory.
- Chapter folder format: `Chapter-01-Title-Of-The-Chapter-In-Camel-Case`, `Chapter-02-Title-Of-The-Chapter-In-Camel-Case`, etc.
- Chapter prose file: `chapter.md` inside the matching chapter folder.
- Page prompt files remain `page-001-chatgpt-image-prompt.md`, `page-002-chatgpt-image-prompt.md`, etc.
- Final reader images remain `1.webp`, `2.webp`, `3.webp`, etc. inside the matching chapter folder.
- Chapter covers stay `front.webp` and `back.webp` inside the matching chapter folder.
- If an arc or season title is not final yet, use a clear temporary folder name such as `01-Season-01` and rename it before final app ingestion.

## Current Folders

- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/README.md`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-01-The-Cafe-That-Opened-For-Seven-Minutes/chapter.md`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-02-A-Letter-Through-The-Service-Window/`
- `Comics/01-Arc-The-Fire-At-San-Aurelio-Junction/Chapter-02-A-Letter-Through-The-Service-Window/chapter.md`

## Production Rules

- Check `../characters.md` before generating or editing any page. From a nested chapter folder, reference it as `../../../characters.md`.
- Check `style-guide.md` before generating or editing any page. From a nested chapter folder, reference it as `../../style-guide.md`.
- Put every chapter under the correct numbered arc/season folder, not directly under `Comics/` and not in a bare chapter-number folder.
- Use the prose chapter title in the chapter folder name, and store the prose manuscript there as `chapter.md`.
- Keep `chapter.md`, cover prompts, page prompts, generated WebP images, and future chapter notes together in the same chapter folder.
- Keep the prose manuscript as `chapter.md` inside its matching chapter folder; do not leave prose chapter files at the story root.
- Use colored time-slip BL railway romance manga/manhwa/manhua style for chapter front/back covers.
- Use black-and-white time-slip railway romance manga/manhwa/manhua manuscript style for reader-facing pages.
- Do not mix colored interior pages, grayscale webtoon, painterly concept art, and manga manuscript styles inside the same interior chapter sequence.
- Keep the actual panel script, dialogue, captions, clock text, station signs, object labels, and SFX inside each `page-###-chatgpt-image-prompt.md` file.
- Keep character faces, outfits, props, and body language consistent across pages.
- Keep Daniel's silver-threaded close curls, nose-bridge scar, amber-tinted conservation glasses, slate chore jacket, cotton gloves, and careful conservator posture consistent.
- Keep Tomas's long dark wavy hair, jade-green hair cord, stray face-framing strands, flour marks, rolled cafe sleeves, brown waist apron, and warm baker body language consistent.
- Keep time-slip lettering readable and minimal: short signs, clock faces, short notes, and no paragraphs of tiny text.
- Keep every interior panel on a page in one consistent ink and screentone style.
- If a new recurring character appears, add them to `../characters.md` before generating final pages.
- Generated pages in this folder should be considered the version that readers see in the app.
- Save generated covers and pages as final WebP files inside the chapter folder (`front.webp`, `back.webp`, `1.webp`, `2.webp`, etc.).
