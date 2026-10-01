"""Cut the rendered lesson into one clip per beat, plus a poster frame for each.

Pass 1 re-encodes with a keyframe forced at every beat, so pass 2 can cut on copy
and every clip starts on a clean frame.
"""
import json
import os
import shutil
import subprocess

import sys
SRC = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\kiran\OneDrive\Desktop\kiran\python-list-comprehension-v2.mp4"
WORK = "split"
KEYED = os.path.join(WORK, "keyed.mp4")
CLIPS = os.path.join(WORK, "clips")

beats = json.load(open("beats.json"))["beats"]
times = [f"{t:.3f}" for t in beats[1:]]
os.makedirs(WORK, exist_ok=True)
if os.path.exists(CLIPS):
    shutil.rmtree(CLIPS)
os.makedirs(CLIPS)

if not os.path.exists(KEYED):
    print(f"pass 1: re-encoding with {len(beats)} forced keyframes ...", flush=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                    "-pix_fmt", "yuv420p", "-force_key_frames", ",".join(times),
                    "-an", KEYED], check=True)
# Cut on the keyframes the file ACTUALLY has, not on the times that were asked for.
# -force_key_frames lands each one on the nearest frame boundary, so a requested 21.900
# becomes 21.900 or 21.933; feeding the requested time back to the segmenter leaves it
# looking for a keyframe that is a frame away, and it silently drops that boundary -
# which merges two clips and shifts every clip after it by one.
probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-skip_frame", "nokey",
                        "-show_entries", "frame=pts_time", "-of", "csv=p=0", KEYED],
                       capture_output=True, text=True, check=True).stdout.split()
kf = sorted({float(x.rstrip(",")) for x in probe if x.strip(",")})
if len(kf) != len(beats):
    print(f"  warning: {len(kf)} keyframes for {len(beats)} beats")
# ...and ask for each one a hair EARLY. The segmenter takes the first keyframe at or after
# the time it is given, and a pts that prints as 5.200 can really be 5.19999, so asking for
# 5.200 walks past it to the next keyframe and that boundary is lost. Half a frame is 0.017s,
# so 0.010 cannot reach back to the keyframe before.
cuts = [f"{t - 0.010:.3f}" for t in kf[1:]]
print(f"pass 2: cutting on {len(cuts)} keyframes ...", flush=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", KEYED, "-c", "copy",
                "-f", "segment", "-segment_times", ",".join(cuts),
                "-reset_timestamps", "1", "-segment_format", "mp4",
                os.path.join(CLIPS, "clip-%03d.mp4")], check=True)

names = sorted(os.listdir(CLIPS))
print(f"{len(names)} clips (expected {len(beats)})", flush=True)

print("posters ...", flush=True)
for i, nm in enumerate(names):
    src = os.path.join(CLIPS, nm)
    dst = os.path.join(CLIPS, nm.replace(".mp4", ".jpg"))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-frames:v", "1",
                    "-q:v", "3", dst], check=True)
    if i % 50 == 0:
        print(f"  {i}/{len(names)}", flush=True)

total = sum(os.path.getsize(os.path.join(CLIPS, f)) for f in os.listdir(CLIPS))
print(f"done: {total / 1e6:.1f} MB of clips + posters")
