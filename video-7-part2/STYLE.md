# HyperFrames Video Context — TAP Academy Python Lesson Videos

**Context name:** `tap-python-lesson-video`
**Reference build:** `video-7` — *Python List Comprehension*, 659 s (10 m 59 s), delivered as
`python-list-comprehension-v2.mp4`
**Last updated:** 2026-09-29

---

## 0. How to use this file

Paste this whole file (or its path) into a **new chat** as the opening context, then say what the
next video is about. Everything below is already approved by me — do not redesign it, do not ask
me to re-choose colours or layout. Build the new lesson in this style and only ask about the
*teaching content*.

### Prompt 1 — a new video in this style

```text
Read C:\Users\kiran\OneDrive\Desktop\kiran\hyperframes-video-context.md - that is my approved
video style (context name: tap-python-lesson-video). Follow it exactly. Do not redesign the look,
do not ask me to re-choose colours, fonts or layout; everything in that file is already approved.

New video topic: <TOPIC HERE>

Start a new project in C:\Users\kiran\Documents\hyperframes, build it part by part, and after each
part run npm run check, take a snapshot of the new beats and look at it yourself, then give me the
Studio link with the timestamps. Don't render until I tell you to.
```

### Prompt 2 — extend or continue an existing video

```text
Read C:\Users\kiran\OneDrive\Desktop\kiran\hyperframes-video-context.md - my approved video style
(context name: tap-python-lesson-video). Follow it exactly.

I'm continuing C:\Users\kiran\Documents\hyperframes\video-N. Read its STYLE.md and its compositions
first so you know the current end state. Append the new parts at the end - never change anything
already built.

What to add next: <WHAT HERE>
```

### Prompt 3 — edit specific moments in a finished video

```text
Read C:\Users\kiran\OneDrive\Desktop\kiran\hyperframes-video-context.md - my approved video style.
Follow it exactly.

Project: C:\Users\kiran\Documents\hyperframes\video-N. Start the Studio preview and open
http://127.0.0.1:3002/#project/video-N. I'll send screenshots with timestamps; change only the
moments I point at, nothing else. Confirm each change with a snapshot at that timestamp.
```

The first line is what does the work — the rest is just the job.

If this file and an old memory note disagree, **this file wins** — it is the newest state.

---

## 1. Who and what

- I am a Python trainer at **TAP Academy**. These are lesson videos for students who watch on a
  classroom monitor from the back of the room.
- Tool: **HyperFrames**, CLI pinned per project (currently `hyperframes@0.8.58`).
- Frame: **1920 × 1080, 30 fps, no audio** unless I supply it.
- Projects live in `C:\Users\kiran\Documents\hyperframes\video-N`.
- Studio: `npx hyperframes preview --background --no-open` → `http://127.0.0.1:3002/#project/<name>`
  (video-5-part2 used :3003). Always check `preview --status` before restarting it.
- Finished renders: `renders/<kebab-name>.mp4` first, then **copy** to
  `C:\Users\kiran\OneDrive\Desktop\kiran\` and hash-check. Never render straight into OneDrive.
  New versions of an existing video get `-v2`, `-v3`… — never overwrite.

**The single most important rule:** text must be readable from the back of a classroom. When
something does not fit, *shrink the thing that is not being taught* (the window, the tiles) —
never the digits, never the teaching text, and never wrap a line that should read as one line.

### 1.1 Two style families — check which one a project belongs to

Everything in §§2–4 of this file is the **list / tile family**. There is a second approved family
for lessons that show memory instead of lists. They share the frame, the background, the code
window and the typing rules; they differ in what stands on the right.

| Family | Shows on the right | Governing spec | Built in |
|---|---|---|---|
| **List / tile** *(this file)* | Yellow tile rows, indices, gliding rings | **this file** | video-7 |
| **Code + memory** | Stack and Private Heap panels, object cards, address arrows | `video-template\STYLE.md` (from video-5-part2) | video-5, video-5-part2, video-6, video-8 |

Differences that matter when you move between them: the memory family sets code at **36 px on a
46 px grid** with plain text `#c8d3f5` (this family uses 52 px / 66 px and `#ffffff`), and its
dashed window border is 5.5 px dash 5/19.5 (this family thinned it to 3 px dash 3/13). Do not
mix the two — read the project's own `STYLE.md` first.

### 1.2 Project index

| Project | Lesson | State |
|---|---|---|
| `video-7` | List comprehension | **Done** → `python-list-comprehension-v2.mp4` (659 s). The reference build for this file. |
| `video-8` | **Type Casting** | **In progress in another chat** — see below |
| `video-5-part2`, `video-6` | Class / static variables | Done; the code + memory reference |
| `video-template` | — | Clean starting point for the code + memory family |
| `video-2`, `video-3`, `new-video`, `my-video` | Older | Leave alone unless asked |

**`video-8` — Type Casting (in progress, started 2026-09-29).** Do not treat it as finished and
do not rebuild what is already there; read its files first and append. Current state, 39.3 s:

1. `compositions/title-plaque.html` (0 – 18.3 s) — my plaque artwork pops up empty, then
   "Type Casting" types on one character at a time. The lettering is **one image shown through
   eleven bands**, so the finished title is the artwork itself, not a re-typeset copy
   (`tc-plaque.png`, `tc-letters.png`).
2. `compositions/type-map.html` (3.8 – 18.2 s) — four columns of casting functions on my arrow
   banners. The banner is `tc-banner.png` **3-sliced** (`border-width: 0 30px 0 83px`), so the
   badge and chevron keep their shape while the middle stretches to any word. Labels Nunito 700,
   46 px, white with a cyan rim (`#7ef6f8` → `#3ddcf2`). Connectors are three strokes on one
   path: body `#0b6ba8` 12.6 px, core `#02a8e9` 5.5 px, plus a halo — they **appear, they do not
   draw on**.
3. `compositions/blackboard.html` (18.2 – 39.3 s) — the title and map leave; a blackboard works
   `a = 24` into one byte: eight empty bits, base-2 format, the long division, the remainders read
   upwards, then what the leftmost bit means. The board is `bd-board.png` **nine-sliced** (80 px)
   so only the dark interior stretches; the division ladder is one image shown through five
   windows, because the bracket runs through every row.
4. `compositions/code-window.html` exists but is **commented out in `index.html`** — the video
   deliberately does not open on code. Give it a `data-start` and uncomment it when the lesson
   reaches code.

It follows the **code + memory** family (its own `STYLE.md`), with new artwork of its own:
`tc-*.png` for the title and map, `bd-*.png` for the blackboard.

---

## 2. Design style

### 2.1 Background
Flat **`#010101`**. No texture image, no gradient, no push-in, no vignette. (The old plaster
texture from video-2/3 is retired.)

### 2.2 Typefaces
| Use | Font | Weight |
|---|---|---|
| All code, indices, variable labels, traces | **JetBrains Mono** (fallback Consolas, monospace) | 400 for code, 500 for labels/indices |
| Question text, "Syntax" pill, panel headings | **SF Pro Display → Inter → Segoe UI** | 700 |

`font-variant-ligatures: none` on code, so `==` reads as two equals signs.
**No bold in diagram text.** Sibling labels all at the same size, as large as fits on one line.
Titles in CAPITALS.

### 2.3 The code window (`Main.py`) — the anchor of every video
- Vector SVG chrome + `assets/code-titlebar.webp` (traffic lights + "Main.py").
- Dashed outline: `#ffffff`, `stroke-width 3`, `stroke-dasharray "3 13"`, round caps, drawn
  17 px outside the body, radius 37. **Thin and airy — not a heavy dashed box.**
- Body `#101b2c` radius 20; title bar `#1b2536`; 1.5 px separator `#2a3649`;
  inner code panel at (8, 63) `#101b2c` with a 1.5 px `#26344b` stroke.
- Code text: **52 px on a 66 px line grid**, column width `CW = 31.2`, blank lines half height
  (33 px). Inner padding 20 px / 16 px.
- **Syntax colours (approved, do not change):**

  | Token | Colour |
  |---|---|
  | plain code, variables | `#ffffff` |
  | keywords (`for`, `in`, `if`, `else`, `def`, `class`) | `#c099ff` |
  | strings *(italic)* | `#e0c78b` |
  | numbers | `#f5a97f` |
  | built-ins (`print`, `len`, `zip`, `range`) | `#8fb3ff` |
  | comments | `#8c8c8c` |

- **Position:** top-left of the frame, anchored at **(49, 105)** — its top edge level with the
  index row of the list on the right. Never centred, never stacked above the lists.
- **Global size knob:** the composition's `#root` carries a static
  `transform: scale(0.66); transform-origin: 49px 105px`. Change that one number to resize the
  whole window everywhere at once, instead of re-tuning every section.
- **Per-section size:** `tl.fromTo("#cw-stage", {scale: a}, {scale: b}, t)`. Each section picks
  the largest scale that still clears the list labels on the right.

  > **Clearance formula:** `49 + (pose.bw + 17) × 0.66 × stageScale ≤ (leftmost label ink) − 20`.
  > Measure the label ink from a snapshot — do not guess.

- A highlight bar `.cw-hl` (fill `rgba(143,179,255,.24)`, 6 px left border `#a8c4ff`) marks the
  line a trace is standing on.

### 2.4 The tile lists (right of the frame) — the "memory view"
- My own artwork: `assets/tile.png` (glossy yellow tile) with black digit glyphs cut from
  `assets/dig-0.png` … `dig-9.png`.
- Geometry: **TW 84 × TH 83, GAP 11**, the row ending **32 px from the right edge**
  (`X0 = 1888 − (N·TW + (N−1)·GAP)`). Narrower rows are used for longer data (8 values: 78 px;
  11 characters: 68 px).
- **Index numbers** above each tile: white, 34 px / 42 px, centred, at `ty − 50`.
- **Variable label + arrow** to the left: white, right-aligned, 38 px / 48 px, 160 px box;
  the cyan arrow runs `X0 − 100 → X0 − 28`.
- **Digit sizing is uniform.** Every `buildRow`-style call passes `uniform = true` so a `1` is
  exactly as big as a `16`. When tiles shrink, raise the glyph scale `k` by the inverse factor so
  the printed digit size never changes (e.g. `0.73 × 0.62 × 103 ≡ 0.73 × 0.70 × 91`).
- **Two rows stacked** with only the space they need between them: source list on top, result
  below. No wasted gap.
- The variable label and arrow appear **only after its row is complete**, and hide when it clears.
  A result label must never point at a half-built row.

### 2.5 Rings (the traversal highlight)
- Cyan `.ab-ring` — `#4fd1ff`, 4 px, radius 22, glow
  `0 0 18px rgba(79,209,255,.75)` + `inset 0 0 12px rgba(79,209,255,.35)`.
- Orange `.ab-ring2` — `#ffae3d`, same construction. Used for the **outer** loop when two loops
  run at once.

### 2.6 Arrows
Solid cyan `#4fd1ff`, 4 px, round caps, with `drop-shadow(0 0 6px rgba(79,209,255,.65))`,
**drawn on by a mask reveal**, then the head polygon fades in. Same style everywhere.

### 2.7 Question cards (the practice question)
- Card **1560 × 600**, centred, then the composition root carries
  `transform: translateY(-120px) scale(0.8)` — sits a fifth smaller and higher on the frame.
- Fill `linear-gradient(145deg, #1a232c, #0d131a)`, border `#2a3642`, radius 44,
  shadow `0 34px 90px rgba(0,0,0,.62)`.
- **Badge + vertical rule**: an `a.` tile (`linear-gradient(145deg,#2e3843,#1b232c)`, radius 30,
  amber `#f3c896` text) and a 2 px `#2c3846` divider before the question text.
- **Question text is ALL WHITE**, 62 px / 80 px, weight 700, with a pronounced 3-D emboss:
  ```css
  text-shadow: 0 -1px 0 rgba(255,255,255,.38), 0 3px 0 #141d27, 0 6px 0 #0c141d,
               0 9px 0 #070d14, 0 16px 26px rgba(0,0,0,.68);
  ```
  No mixed colours inside the question. No amber phrases.
- **Sample rows:** an `Input` chip `linear-gradient(160deg,#2166b8,#16437a)` and an `Output` chip
  `linear-gradient(160deg,#1f8060,#11533f)`, a colon, then a slot that **hugs its value**
  (`width = chars × 27.6 + 72`). Input numbers violet `#b07cf5`, output numbers orange `#ff9f43`,
  strings `#e0c78b`.

### 2.8 Syntax card
- Same theme as the question cards, and it appears **below the coding window** at (49, 520) —
  never in a far corner.
- Panel radius 40 with a pronounced raised treatment:
  `inset 0 2px 0 rgba(255,255,255,.07), inset 0 -2px 0 rgba(0,0,0,.45), 0 10px 0 #070b10,
   0 40px 100px rgba(0,0,0,.7)`.
- A raised blue **"Syntax" pill** (`0 5px 0 #0d2a4c`), the syntax line in 50 px code with a
  stacked extrusion, and each named part in a tinted raised box with a hand-drawn brace and a
  label under it:
  expression **`#f43f6e`**, loop **`#10b981`**, condition **`#ffae3d`**.
- The panel is **pre-sized off screen** to the width the longest version needs
  (`tl.set(panel, {width: fit(n)}, t)`), so nothing jumps while it is visible. **No dead padding
  on the right.**

### 2.9 Output / trace board
- My brown-and-gold card art `assets/panel-brown.webp`, **nine-sliced**: `border: 34px solid
  transparent; border-image: url(...) 70 fill stretch`, plus
  `background: #6e3f1c; background-clip: padding-box` (padding-box is what stops the flat fill
  squaring off the rounded corners).
- Printed values: `.op-row` — `#e7d6c1` (latte), 54 px, with a 3-D stack
  `0 3px 0 #592f12, 0 5px 0 #431f09, 0 8px 12px rgba(0,0,0,.5)`. **Numbers must read as 3-D.**
- Trace tables are **row plates, not a grid**: a header strip
  (`linear-gradient(180deg,#9d6130,#7c4820)`) and one raised plate per step
  (`linear-gradient(180deg,#7d4923,#663818)`), 2 px light dividers between columns.
  Header/arrow text `#f0a830`, values `#f5e2c8`, 36 px, **not bold**.
- Inner margins: 14 px at the top, ~24 px at the bottom, row pitch 43, plate height 38 — so the
  frame never looks "cut" at the border.

---

## 3. Layout principles

1. **Code on the left, data on the right.** Always. Never stacked, never swapped.
2. **Fill the frame** (100 % monitor). No large empty bands.
3. When a line is too long, **scale the code window down** (a transform) — do not move elements,
   do not wrap the line, do not shrink the tiles' digits.
4. Conversely, when the data is narrow, **scale the window back up**. Re-check every section's
   scale after changing tile geometry; numbers chosen for 130 px tiles are wrong for 84 px tiles.
5. A result row must not drop lower on the frame to make room — tighten the tile instead.
6. Nothing overlaps: code window bottom must clear the syntax card top (520 px).
7. Rounded corners, generous radii, no hard rectangles anywhere.

---

## 4. Animations used

### 4.1 Entrances
| Element | Motion |
|---|---|
| Code window | pop: `scale 0.3 → 1`, `back.out(1.3)`, 0.7 s |
| Tiles | rain down with a squash-and-stretch landing (`transform-origin: 50% 100%`) |
| Digits | drop onto their tile after the tile lands |
| Index numbers | fade in above the tiles |
| Variable label | types on, then the arrow draws and the head pops |
| Question card | `opacity 0→1, scale 0.9→1`, `back.out(1.5)`; badge `back.out(2.4)`; rule `scaleY 0→1` |
| Chips / slots | slide in from `x: -26` |
| Syntax panel / boards | pop with `back.out`, header strip `scaleY 0.5 → 1` |

### 4.2 Typing
- **Per character, `CHAR = 0.075 s`, `NEWLINE = 0.25 s`. Never draw a caret (`|`).**
- Indentation appears at once; it is not typed.
- **Assignments type right-hand side first:** for `a = 10` show `10`, then `=`, then `a`.
  Everything else types left to right.
- **Insertion inside a line** (e.g. adding `or i%3==0` inside brackets): overlay a line of leading
  spaces + the new text, set the tail spans to `display: inline-block`, and translate them with
  `tl.set(el, {x: n * CW})` per character so the `)` and `]` are pushed along.
- **One-token swap** (`==` → `!=`): fade the old character out (`scale → 0.4`) and pop the new one
  in (`back.out(2.6)`) in the same column.
- **Collapsing lines**: fade the line that is being replaced, then `lift()` the lines below it up
  by whole line heights while the window resizes.
- Follow my dictated typing order when I give one.

### 4.3 The ring traversal — **one ring that glides**
This is the approved model; the old pop-in / pop-out per index is **retired**.

```js
walker(id, cls, x0, ty, w, h, extra)   // build ONE ring per row
ringOn(sel, x, at)                     // fade it in at slot x
ringTo(sel, from, to, at, dur)         // glide from slot to slot (power2.inOut)
ringOff(sel, at)                       // fade out AND set visibility:hidden afterwards
bump(sels, at)                         // the tile + its digit give 1.1× then elastic.out(1,0.45)
```
- The ring **travels left to right** so students see it coming from the previous index.
- The only "pop" left is the **bump** of the slot it arrives on.
- Every walker must be turned off with `ringOff` at the end of its section — a forgotten one
  leaves a frozen ring on screen for the rest of the video.
- Two loops at once: the **outer ring moves alone first** (a `LEAD` of ~0.6 s) before the inner
  ring restarts its run. They must never move in the same instant.

### 4.4 Flying values
Values that are "collected" fly from the source tile to the result tile — they are never typed
into the result row.

### 4.5 Window resizing
`resizeWin(from, to, at, PUSH_DUR)` with `PUSH_DUR = 0.4`, `power2.inOut`, tweening the SVG
attributes so body, outline, title bar and panel all reshape together. A section's stage scale
tween runs at the same moment (`at = sectionStart − 0.7`).

### 4.6 Transitions between parts
`#root` fades out (0.8 s `power1.inOut`), the frame is rebuilt, `#root` fades back in (0.7 s).

> **Trap:** when a root fades back in, every child that was faded out earlier comes back too.
> Explicitly `tl.set(el, {autoAlpha: 0})` while it is invisible, or old lines and old boards
> reappear.

---

## 5. Principal elements (the composition set)

`index.html` is the root (`data-duration` = the whole video) and mounts these, each full-frame,
each owning its own timeline:

| File | Role |
|---|---|
| `compositions/array-box.html` | **The lists** — tiles, digits, indices, labels, arrows, all ring traversals, flying values |
| `compositions/code-window.html` | **The `Main.py` window** — every line of code, all typing, all window poses and scales |
| `compositions/syntax-card.html` | **The syntax card** under the code window |
| `compositions/question.html` | **Practice question a.** |
| `compositions/question-b.html` | **Practice question b.** |
| `compositions/output-panel.html` | **The brown board** — printed pairs and the nested-loop / zip trace tables |

`output-window.html` (the old right-hand console) is **retired and unmounted** — the result is
shown on the tile lists instead, so a separate output window is redundant.

Assets: `tile.png`, `dig-0…9.png`, `digits.json`, `code-titlebar.webp`, `panel-brown.webp`.

---

## 6. Teaching / content rules

- **Code is typed in the order a teacher writes it**, not in file order.
- Code as I send it, but with PEP 8 spacing (`', '`, `a=2, b=4`, `{'a': 2}`).
- **Never split a printed line across two lines** — it confuses students. Widen or shrink instead.
- Show the *real* Python output.
- Errors: show only the traceback's last line.
- My `|` is a cursor, not code. Fix dictation typos silently and mention them in one line.
  Dictation garbles: "flower brackets" = `{}`, "decoding window" = coding window, "SDI" = s, d, i.
- Every section follows: **show the data → write the code → run the ring over it → collect the
  result → read it off the list.**

---

## 7. Workflow (how I want you to work)

1. **Build part by part.** Implement each instruction immediately; don't ask permission for
   routine judgement calls. Speed matters.
2. After each part:
   - `npm run check` → **0 errors** (the connector-orphan warnings on the arrows are known).
   - `npx hyperframes snapshot --at <t> --no-end --describe false -o s<t>.png`, then **look at the
     image yourself** before telling me it's done. Delete the snapshot folders afterwards.
   - Reply with `http://127.0.0.1:3002/#project/<name>`, the timestamps of the new beats, and any
     normalisation you applied.
3. **Never alter an approved part.** Append. If an approved frame must be proved unchanged,
   re-snapshot and hash-compare.
4. **Render only when I say so.** `npx hyperframes render -o renders/<kebab-name>.mp4`, run it in
   the background (a 10-minute video takes ~26 min on the RTX 3060), then copy to the Desktop
   `kiran` folder and `sha256sum` both copies.
5. Screenshots I send from Studio carry a timestamp — use it, don't guess which beat I mean.

---

## 8. Technical rules and gotchas (hard-won)

### GSAP / HyperFrames
- One **paused** root timeline per composition, registered on
  `window.__timelines["<composition-id>"]`. Child timelines added to it must **not** be paused.
- Everything must be **seek-safe**: any `fromTo` after the first on a target needs
  `immediateRender: false`, plus a `tl.set` baseline at 0 where lint asks for one.
- Never hide an element with a `tl.set` at time 0 — put the hidden state in CSS
  (`gsap_timeline_set_initial_hide`).
- GSAP `x` / `y` on an inline `<span>` needs `display: inline-block` first.
- Sub-compositions share one document → **unique ids and classes per file**. An id collision
  silently resurrects old elements (`ab-m1` vs `ab-lbl1` cost an hour).
- Lint `composition_file_too_large` counts lines outside `<style>` (limit 300); split into a new
  prefixed sub-composition rather than fighting it.
- Only deterministic logic — no `Date.now()`, no `Math.random()`, no fetches.

### Studio
- Studio **live-rewrites** the files: it stamps `data-hf-id`, lowercases `<clipPath>`, and turns
  `\u2192` escapes into a literal `→`. Re-read a file before writing it, anchor on attribute
  fragments or line ranges rather than exact long strings, and match the literal character.
- The preview process is not owned by the chat session — it can die; restart with
  `preview --background --no-open` and confirm with `--status`.
- Studio's player letterboxes in fullscreen; "gaps at the sides" is the player, not the
  composition. Prove it by sampling corner pixels.

### Windows
- Quoted bash heredocs break on content containing `'<svg id="'`-style quoting. **Write the Python
  patch file to the scratchpad with the Write tool and run it** — that path always works.
- Use anchor-checked patch scripts (`assert s.count(old) == 1`) so a silent mis-replace is
  impossible.
- PowerShell 5.1 drops empty-string args to native commands; the Desktop is OneDrive-redirected
  (`C:\Users\kiran\Desktop` does not exist).

### Diagnostics that actually worked
- Pixel-sample rendered snapshots with Pillow to measure a ring's bounds, count cyan pixels, or
  prove a board has faded.
- To find a stray element: temporarily `display: none` a class, then a single id, and re-snapshot.
- If a `tl.set(..., {autoAlpha: 0})` at time *T* does not stick but one at *T + n* does, something
  between them is re-showing it — find that call, don't patch over it.

---

## 9. Checklist for a new video in this style

- [ ] Copy the template project; set `data-duration` on `index.html` and every composition root.
- [ ] Background `#010101`; mount array-box, code-window, syntax-card, question(s), output-panel.
- [ ] Code window at (49, 105), root `scale(0.66)`; palette and 52 px / 66 px grid as §2.3.
- [ ] Tile rows right-aligned to 1888; uniform digit sizing; labels and arrows appear only after
      a row completes.
- [ ] One gliding ring per row; every walker has a matching `ringOff`.
- [ ] Assignments type RHS first; no caret; `CHAR = 0.075`.
- [ ] Per-section stage scale computed from the clearance formula against a real snapshot.
- [ ] Question cards all-white 3-D text, 0.8 scale, lifted 120 px.
- [ ] Syntax card below the code window, pre-sized, no right padding.
- [ ] Explicit `autoAlpha: 0` for anything that must stay hidden across a root fade.
- [ ] `npm run check` → 0 errors; snapshot and *look at* every new beat.
- [ ] Render only on request → `renders/` → copy to `kiran` → hash-check → `-vN` if it's a redo.
