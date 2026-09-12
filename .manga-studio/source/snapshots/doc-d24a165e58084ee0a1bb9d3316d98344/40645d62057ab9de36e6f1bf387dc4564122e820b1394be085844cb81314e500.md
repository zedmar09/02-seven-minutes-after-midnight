# Comics Style Guide

Use this file as the visual lock for generated comic pages.

## Cover Color Rule

- Chapter front and back covers are colored time-slip BL railway romance manga/manhwa/manhua cover illustrations.
- Interior comic pages remain black-and-white time-slip railway romance manga/manhwa/manhua manuscript pages.
- Do not apply the black-and-white interior-page rule to chapter cover prompt files such as `chapter-01-front-cover-chatgpt-image-prompt.md`, `chapter-01-back-cover-chatgpt-image-prompt.md`, `front-cover-chatgpt-image-prompt.md`, or `back-cover-chatgpt-image-prompt.md`.

## Black-And-White Time-Slip Railway Romance Manga/Manhwa/Manhua Style Lock

- Format: black-and-white manga/manhwa/manhua comic manuscript page.
- Page feel: mature BL time-slip romance, historical mystery, railway noir, emotional thriller, quiet adult longing, and print-ready monochrome art.
- Linework: expressive hand-drawn ink lines, refined adult faces, elegant hair rendering, detailed hands, precise architectural backgrounds, chipped tile, cafe counters, service windows, archival boxes, newsprint, scorch marks, and consistent line weight across every panel.
- Rendering: pure black, white, grayscale screentone, cross-hatching, hatching, smoke texture, steam, dust motes, rain streaks, glass reflections, flour dust, and strong black fills.
- Human Finish: faces should have lived-in asymmetry, natural expressions, believable eye focus, imperfect hair strands, correct hands, and small work-worn details. Avoid plastic smoothness or generic AI-pretty character faces.
- No color for reader pages: do not generate colored webtoon pages, painterly concept art, tinted eyes, colored lighting, or grayscale copies of colored pages.
- Color-coded story elements translate into value and texture: Daniel's slate-blue chore jacket becomes medium-dark screentone, Tomas's jade-green hair cord becomes pale gray cord with a clean highlight, warm cafe amber becomes soft white glow with gray halo, brass becomes white shine cuts with dark ink edges, old paper becomes speckled mid-gray, and firelight becomes harsh white glow swallowed by black smoke.
- Detail level: keep close-ups, clock faces, letters, pastries, photographs, conservation tools, cafe hardware, station signs, and service-window threshold effects at a consistent manga/manhwa detail density.
- Avoid: palace robes, crowns, phoenix hairpins, xianxia warrior costumes, half-masks, gothic coffins, mourning cloaks, supernatural conductor figures, teenage station uniforms, red scarves, school-uniform protagonists, corporate revenge suits, debt ledger boxes, loyalty percentages, hospital-thriller framing, chibi comedy, photorealism, 3D render, western superhero comics, muddy grayscale, unreadable text, and random character redesigns.

## Prompt Workflow

For new comic work, use the arc/season-first structure. Keep the prose chapter file and all comic production files inside this path shape:

```text
Comics/<NN-Arc-Or-Season-Name-In-Camel-Case>/README.md
Comics/<NN-Arc-Or-Season-Name-In-Camel-Case>/<Chapter-NN-Title-Of-The-Chapter-In-Camel-Case>/chapter.md
Comics/<NN-Arc-Or-Season-Name-In-Camel-Case>/<Chapter-NN-Title-Of-The-Chapter-In-Camel-Case>/page-###-chatgpt-image-prompt.md
```

Use the next arc or season number for each new arc, and use the prose chapter title in the chapter folder name. The arc/season `README.md` stores the readable arc title, synopsis notes, and chapter list. Do not add bare chapter-number folders directly under `Comics`.

The prompt must be self-contained so it can be copied into ChatGPT to generate the image. After approval and external conversion, save the final WebP image in the same chapter folder as `1.webp`, `2.webp`, `3.webp`, etc. Chapter covers should be saved in the same chapter folder as `front.webp` and `back.webp`.

## Panel Pacing Rule

Panel order and panel count can change when it improves romance tension, mystery, fear, or readability. Prompts should define the required story beats and emotional progression, but the layout may rearrange panels as long as the reader can follow the time-slip clearly.

For first-touch moments, the cafe transformation, the service-window exchange, the seven-minute countdown, and chapter-ending fire clues, use fewer larger panels when stronger. A full-page splash, two-panel page, or one dominant reveal panel is allowed if it makes the moment more powerful and easier to understand.

Do not mechanically reuse the same page grid. Compose each page like a real manga/manhwa page: archival investigation can use smaller evidence panels, while romance and time-slip reveals should breathe in larger panels.


## Lettering Rule

The prompt may request readable speech bubbles, captions, SFX, clock faces, station signs, cafe signs, handwritten notes, and newspaper headlines directly in the generated image. Keep dialogue, signs, and labels short and uppercase so they have the best chance of rendering cleanly.

Important signs and notes:

```text
CAFE SIETE
```

```text
12:00
```

```text
12:07
```

```text
TOMAS
```

```text
I AM REAL.
```

```text
I WILL BRING BETTER BREAD.
```

```text
FIRE STARTS IN THE SERVICE CORRIDOR.
```

## Daniel Visual Lock

Daniel Soriano must stay consistent: adult man, 36 years old, warm brown skin rendered in mid-tone values, close-cropped black curls with early silver at the temples, long narrow face, tired dark eyes, small healed cut across the bridge of his nose, thin rectangular amber-tinted conservation glasses translated as clear glasses with pale shine, slate-blue chore jacket as medium-dark screentone, neutral shirt, dark trousers, soft-soled shoes, cotton conservation gloves, careful posture, archival folder, flashlight, notebook, and conservation tools.

Do not give Daniel round Jiho-style glasses, ash-brown corporate undercut, mole identity, black mourning cloak, courier braids, school uniform, palace robes, half-mask, fantasy-prince styling, or teenage proportions.

## Tomas Visual Lock

Tomas Rivera must stay consistent: adult man, 28 years old, sun-warm tan skin rendered with warm mid-gray screentone, bright dark eyes, strong brows, lean baker's forearms, long dark wavy hair past his shoulders when loose, hair tied low with a thin jade-green cord translated as a pale gray tie, loose strands constantly falling across his cheeks and mouth, cream short-sleeved 1980s cafe shirt, faint collar embroidery, high-waisted dark trousers, flour-marked brown waist apron as medium screentone, leather work shoes, brass pastry tongs, cafe towel, and handwritten notes on wax paper.

Do not give Tomas palace immortal styling, xianxia warrior hair, ghost-prince features, gothic warlord posture, masked noble design, school mystery-boy proportions, corporate suits, or modern idol polish. His long hair is romantic but practical, always connected to baking work.

## San Aurelio And Cafe Visual Rules

- San Aurelio Junction should feel like a real historical railway station: arched windows, green-and-cream tiles translated into alternating gray values, brass signs, ticket windows, platform clocks, stained glass transoms, iron beams, rain gutters, old fans, and platform announcement speakers.
- 2026 station spaces should feel abandoned: dust, broken tile, redevelopment banners, plywood, rust, scattered plaster, archive folders, caution tape, cracked glass, cold rain, and darkness beyond flashlight beams.
- 1986 station spaces should feel alive: warm cafe bulbs, coffee steam, pastry case, handwritten menus, ceiling fans, rail passengers as silhouettes, paper cups, wet coats, station announcements, and motion outside the cafe.
- Cafe Siete should be split by time. The same counter can exist in both eras during the seven minutes, but the surroundings disagree.
- The service window is the most important visual motif. It should feel narrow, intimate, and dangerous: small enough for plates, letters, and hands, not large enough for a body.
- Object aging should be visible but elegant: bread drying and cracking, paper yellowing, ink fading, photographs warping, metal tarnishing, and smoke stains appearing after crossing time.
- Romance should read through proximity, exchanged objects, interrupted jokes, careful glances, fingers touching across the threshold, and the pain of running out of minutes.
