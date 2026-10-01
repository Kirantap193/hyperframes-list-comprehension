"""Stage 0 - the per-frame activity curve the beat finder walks.

One value per frame: the mean absolute grayscale difference from the frame before
it, on a 160x90 downscale, as a 0..1 fraction. The downscale is the point - at full
resolution h264 mosquito noise around static text never settles, and a still slide
reads as continuous motion, which would erase every resting state the deck cuts on.
Averaging 12x12 blocks of pixels throws that away.

act[0] is 0 (nothing precedes the first frame), and len(act) is the frame count, which
beats3.py uses as the duration.

    python activity.py <source.mp4>
"""
import subprocess
import sys

import numpy as np

W, H = 160, 90
src = sys.argv[1]

p = subprocess.Popen(
    ["ffmpeg", "-v", "error", "-i", src, "-vf", f"scale={W}:{H}:flags=area",
     "-pix_fmt", "gray", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)

sz = W * H
act = [0.0]
prev = None
while True:
    b = p.stdout.read(sz)
    if len(b) < sz:
        break
    cur = np.frombuffer(b, np.uint8).reshape(H, W).astype(np.int16)
    if prev is not None:
        act.append(float(np.abs(cur - prev).mean()) / 255.0)
    prev = cur
p.stdout.close()
p.wait()

a = np.array(act, dtype=np.float32)
np.save("activity.npy", a)
print(f"activity.npy: {len(a)} frames ({len(a) / 30.0:.2f}s at 30fps), "
      f"mean {a.mean():.4f}, max {a.max():.4f}, {(a > 0.03).sum()} frames moving")
