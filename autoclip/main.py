import argparse
import json
from pathlib import Path

from autoclip.cutters.scene_cut import detect_scene_cuts
from autoclip.utils.ffmpeg_export import export_clips


def main():
    parser = argparse.ArgumentParser(description="autoclip - scene cut MVP")
    parser.add_argument("--input", required=True, help="Path to input video")
    parser.add_argument("--out", default="clips.json", help="Output timeline json")
    parser.add_argument("--threshold", type=float, default=30.0, help="Scene cut threshold (higher = fewer cuts)")
    parser.add_argument("--min-clip-sec", type=float, default=1.0, help="Minimum clip length in seconds")
    parser.add_argument("--sample-fps", type=float, default=3.0, help="Sampling fps for detection")
    parser.add_argument("--export", action="store_true", help="Export clips to mp4 files")
    parser.add_argument("--outdir", default="examples/outputs", help="Output directory for exported clips")
    parser.add_argument("--prefix", default="clip", help="Exported clip filename prefix")

    args = parser.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        raise FileNotFoundError(f"Input not found: {inp}")

    clips = detect_scene_cuts(
        str(inp),
        threshold=args.threshold,
        min_clip_sec=args.min_clip_sec,
        sample_fps=args.sample_fps,
    )

   
    out_path = Path(args.out)
    out_path.write_text(json.dumps(clips, indent=2), encoding="utf-8")
    print(f"✅ Wrote {out_path} with {len(clips)} clip(s).")

    
    if args.export:
        outdir = export_clips(str(inp), clips, args.outdir, prefix=args.prefix)
        print(f"🎬 Exported clips to: {outdir}")


if __name__ == "__main__":
    main()
