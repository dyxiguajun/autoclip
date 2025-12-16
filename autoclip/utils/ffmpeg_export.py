from __future__ import annotations
import subprocess
from pathlib import Path
from shutil import which


def require_ffmpeg():
    if which("ffmpeg") is None:
        raise RuntimeError("ffmpeg not found. Install it first (e.g., brew install ffmpeg).")


def export_clips(video_path: str, clips: list[dict], outdir: str, prefix: str = "clip"):
    """
    Export clips using ffmpeg by re-encoding (more accurate cut points).
    Each clip dict should have: start, end (seconds).
    """
    require_ffmpeg()

    src = Path(video_path)
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)

    for i, c in enumerate(clips):
        start = float(c["start"])
        end = float(c["end"])
        if end <= start:
            continue

        out_file = out / f"{prefix}_{i:03d}_{start:.2f}-{end:.2f}.mp4"

        cmd = [
            "ffmpeg",
            "-y",
            "-ss", f"{start}",
            "-to", f"{end}",
            "-i", str(src),
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "128k",
            str(out_file),
        ]

        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return str(out)
