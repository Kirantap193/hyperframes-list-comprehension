# Python list comprehension — HyperFrames lesson

Teaching videos for TAP Academy, built with [HyperFrames](https://hyperframes.heygen.com).
1920×1080, 30 fps, no audio.

| Project | Lesson | State |
|---|---|---|
| `video-7` | List comprehension, part 1 | Finished — 659 s, rendered |
| `video-7-part2` | List comprehension, part 2 | In progress — 170 s so far |
| `tools/split-render-deck` | Turns a rendered lesson into a click-through PowerPoint | Working |

## Carrying on from another machine

```bash
git clone <this repo>
cd hyperframes/video-7-part2
npx hyperframes preview --background --no-open --port 3003
```

Then open **http://localhost:3003/#project/video-7-part2**. Part 1 runs the same way on
port 3002. Nothing else is needed — the CLI is pulled by `npx` at the pinned version in
each project's `package.json`, and the artwork each project uses is in its own `assets/`.

Check before and after any change:

```bash
npm run check          # lint + runtime + layout + motion + contrast
npm run render         # only when the preview has been approved
```

## What part 2 contains

1. **0 – 13 s** — the three syntax cards from part 1, side by side, one per click.
2. **14 – 27 s** — question a: join two lists position by position into one sentence.
3. **28 – 100 s** — the `zip` program, written the way it is taught: `[ for i in lst1 ]`
   → `zip` → `zip(lst1, lst2)` → `i,j` → `(i,j)` → `res =` → `print`, then the loop runs
   with the lists on tiles, and `' '.join(res)` turns the words into one string.
4. **101 – 113 s** — question b: upper case each word under 5 letters, lower case the rest.
5. **114 – 170 s** — `s.split()`, then the comprehension built from a skeleton with blanks
   (`[ __ if __ else __ for i in lst ]`) down to
   `res = [ i.lower() if len(i)>=5 else i.upper() for i in lst ]`, and the run that fills `res`.

## Style

`video-7/STYLE.md` is the approved design spec — colours, the code window, the tile lists,
the gliding ring, the question and syntax cards, the typing rules, and the workflow. Read it
before changing anything visual. The same file is in `video-7-part2/`.

## Not in this repository

Rendered `.mp4` files and the `.pptx` decks built from them. They are large and can be
rebuilt from the source with `npm run render` and `tools/split-render-deck`.
