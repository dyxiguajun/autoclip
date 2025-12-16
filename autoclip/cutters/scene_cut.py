from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict

import cv2
import numpy as np

@dataclass
class Clip:
    start: float
    end: float
    score: float = 1.0

def detect_scene_cuts(
    video_path: str,
    threshold: float = 30.0,
    min_clip_sec: float = 1.0,
    sample_fps: float = 3.0,
) -> List[Dict]:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Failed to open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration = frame_count / fps if frame_count > 0 else 0.0

    step = max(1, int(round(fps / sample_fps)))

    prev_gray = None
    cuts = [0.0]

    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        if idx % step != 0:
            idx += 1
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (320, 180))  # 降采样提速

        if prev_gray is not None:
            diff = cv2.absdiff(gray, prev_gray)
            score = float(np.mean(diff))
            t = idx / fps
            if score >= threshold:
                cuts.append(t)

        prev_gray = gray
        idx += 1

    cap.release()

    # 生成 clip 列表
    cuts = sorted(set([c for c in cuts if 0.0 <= c <= duration]))
    if duration > 0:
        cuts.append(duration)

    clips: List[Clip] = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        if (b - a) >= min_clip_sec:
            clips.append(Clip(start=round(a, 2), end=round(b, 2)))

    return [c.__dict__ for c in clips]
