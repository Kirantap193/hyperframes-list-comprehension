# Split-render deck

Turns a rendered lesson MP4 into a click-through PowerPoint: one slide per teaching beat,
each holding that beat's clip, which autoplays when the slide arrives and then holds.
The trainer clicks once per step, exactly like normal slides.

Built for `python-list-comprehension-v2.mp4` (659 s → 285 clips, 287 slides, 27 MB) and
matching the earlier `python-class-variables-part2-v4.pptx` the user approved.

## Run it

Work in a scratch directory; these write `activity.npy`, `beats.json` and `split/`.

```bash
# 1. the activity curve
python activity.py <source.mp4>       # writes activity.npy
# 2. beats - SWEEP THE THRESHOLD, it is per-video (see below)
python beats3.py 0.0010 4 0.6 5.0     # threshold, quiet frames, min gap, max clip length
# 3. cut into clips + poster frames
python split.py <source.mp4>
# 4. build the deck
python build_pptx.py <out>.pptx "<Title>"
```

Then copy the `.pptx` to `C:\Users\kiran\OneDrive\Desktop\kiran\` and hash-check it.

## How the beats are found

The lesson holds still between steps, so a beat is **the first moving frame after a quiet
stretch**. `beats3.py` walks a 160×90 grayscale mean-absolute-difference curve:

**The threshold is per-video, not a constant.** It is a fraction of the *whole frame*, so it
scales with how much of the frame each step paints. A code-and-memory lesson moves whole window
panels and wants `T = 0.03`; a lesson that is small elements on black (video-8 type-casting:
tiles, digits, a 150px literal) never gets near that — its curve peaks at 0.072 and only **three
frames** in 93 s clear 0.03. Sweep it, and check the clips per *part*, not just the median: at
T = 0.0015 the median looked right (2.20 s) while the two bit-working boards were being time-split
at 3.5-4.3 s a clip rather than cut on their steps. T = 0.0010 gave 2.1 s and 3.3 s there.

- `T` — above this, the frame is moving
- `QUIET = 4` frames (~0.13 s) of stillness must come first
- `MIN_GAP = 0.6 s` — anything closer is the same beat
- `MAX_LEN = 5 s` — a longer run (a continuous ring scan, a long typed line) is cut
  **recursively** at its stillest interior frame until every piece fits

Those settings gave 286 beats, median 2.42 s — the same feel as the approved deck
(291 clips, ~2.1 s mean). Detected beats land on the authored ones (10.07 ≈ `POP_AT` 10.0,
148.5 = `OR_AT`), which is the check that the detector is honest.

### Settings that have worked

| Video | What a step paints | `T` | `MIN_GAP` | Result |
|---|---|---|---|---|
| video-7 list comprehension | whole code windows, big tile rows | `0.03` | `0.6` | 285 clips |
| video-8 type casting | small elements on black | `0.0010` | `0.6` | 51 clips |
| video-7-part2 | small elements on black, with ring runs | `0.00015` | `0.9` | 74 clips |

**`MIN_GAP` is the second knob, and it matters for traversals.** One step of a ring run is
two movements - the ring glides, then a value drops into a slot - about 0.6 s apart. At
`MIN_GAP 0.6` each step becomes two clicks; at `0.9` the pair merges and one step is one
click, while steps 1.4 s apart stay separate. Check a run explicitly: count the beats
between its first and last step and compare with the number of indices.

**Sanity check before trusting a sweep:** compare the peak activity of a step against `T`.
If the peaks are *below* `T`, nothing registers as motion at all and what look like beats
are really `MAX_LEN` cutting on a timer. The giveaway is a run of clips all exactly
`MAX_LEN` seconds long, and `beats3.py` reporting a max equal to `MAX_LEN`.

```python
import numpy as np; a = np.load("activity.npy")
a[int(73.6*30):int(75.0*30)].max()   # one step's peak, against T
```

## How the cutting works

Two ffmpeg passes, so every clip starts on a clean frame:

1. re-encode with `-force_key_frames` at every beat (libx264, crf 23, yuv420p, no audio)
2. `-f segment -segment_times … -c copy` to cut without another re-encode

Pass 2 must be given the keyframes the keyed file **actually has**, each nudged 0.010 s early —
not the beat times. `-force_key_frames` snaps each request to a frame boundary, and the segment
muxer takes the first keyframe *at or after* the time it is handed, so a pts that prints as
`5.200` but is really `5.19999` gets walked past. That silently merges two clips and shifts every
clip after it by one — the durations still sum to the source, so only the clip *count* catches it.

Then one poster JPEG (`-frames:v 1 -q:v 3`) per clip — PowerPoint shows it before the clip
plays, so a slide never flashes black.

Verify the clip durations sum to the source duration exactly.

## How the deck is built

The shell — slide master, 11 layouts, themes, tags, notes master, presProps/viewProps — is
lifted verbatim from the approved deck, so the new one opens identically. Only slides,
media and package metadata are generated.

Each clip slide carries:

- a `p:pic` with `a:videoFile r:link` **and** `p14:media r:embed` pointing at the same mp4
  (PowerPoint needs both), poster via `blipFill`, full-bleed 12192000 × 6858000 EMU
- a **click-catcher**: a white rectangle at `alpha 1000` (1 %) over the whole slide, so a
  click anywhere advances instead of pausing the video
- a timing block issuing `playFrom(0.0)` at `delay="0"`, `nodeType="withEffect"` — the clip
  starts on arrival; `nextCondLst onNext` keeps the slide waiting for the click
- background `#010101` on every slide, matching the video

Slide 1 and the last slide are blank openers/enders.

## Gotchas

- Strip the reference deck's `docProps/thumbnail.jpeg` **and** the `_rels/.rels` entry that
  points at it, or the package has a dangling relationship.
- Regenerate `docProps/core.xml` and `app.xml`; the originals carry the old deck's title.
- Slide layouts reference `ppt/tags/*`, so those parts must be copied too.
- Every part needs a content type and every relationship target must exist — validate both
  before shipping (the build script's check is worth re-running).
