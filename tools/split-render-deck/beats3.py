"""Beat finder, final: quiet-then-moving detection plus recursive splitting of long runs."""
import json
import sys

import numpy as np

act = np.load("activity.npy")
n = len(act)
FPS = 30.0


def split(a, b, M, G, out):
    """Cut [a, b) at its stillest interior frame until no piece is longer than M."""
    if b - a <= M:
        return
    lo, hi = int((a + G) * FPS), int((b - G) * FPS)
    if hi <= lo:
        return
    span = act[lo:hi]
    mid = (lo + hi) / 2
    cut = lo + int(np.argmin(span + 0.004 * np.abs(np.arange(lo, hi) - mid)))
    t = round(cut / FPS, 3)
    out.append(t)
    split(a, t, M, G, out)
    split(t, b, M, G, out)


def find(T, QUIET, MIN_GAP, MAX_LEN):
    moving = act > T
    beats = [0.0]
    quiet = QUIET
    for i in range(1, n):
        if moving[i]:
            if quiet >= QUIET:
                t = i / FPS
                if t - beats[-1] >= MIN_GAP:
                    beats.append(round(t, 3))
            quiet = 0
        else:
            quiet += 1
    extra = []
    for a, b in zip(beats, beats[1:] + [n / FPS]):
        split(a, b, MAX_LEN, MIN_GAP, extra)
    beats = sorted(set(beats + extra))
    gaps = np.diff(np.array(beats + [n / FPS]))
    return beats, gaps


if len(sys.argv) > 1:
    T, Q, G, M = float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    b, g = find(T, Q, G, M)
    json.dump({"fps": FPS, "duration": n / FPS, "beats": b}, open("beats.json", "w"), indent=1)
    print(f"wrote beats.json: {len(b)} clips  median {np.median(g):.2f}s  "
          f"mean {g.mean():.2f}s  min {g.min():.2f}s  max {g.max():.2f}s")
else:
    for T, Q, G, M in [(0.03, 4, 0.60, 6.0), (0.03, 4, 0.60, 5.0), (0.04, 5, 0.65, 5.0)]:
        b, g = find(T, Q, G, M)
        print(f"T={T} Q={Q} gap={G} max={M}: {len(b):4d} clips  median {np.median(g):5.2f}s  "
              f"mean {g.mean():5.2f}s  min {g.min():4.2f}s  max {g.max():5.2f}s")
