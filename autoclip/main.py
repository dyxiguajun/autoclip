import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="autoclip - minimal MVP")
    parser.add_argument("--input", required=True, help="Path to input video")
    parser.add_argument("--out", default="clips.json", help="Output timeline json")
    args = parser.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        raise FileNotFoundError(f"Input not found: {inp}")

    # MVP: placeholder clip (we'll replace with real detection next)
    clips = [
        {"start": 0.0, "end": 5.0, "score": 1.0}
    ]

    out_path = Path(args.out)
    out_path.write_text(json.dumps(clips, indent=2), encoding="utf-8")
    print(f"✅ Wrote {out_path} with {len(clips)} clip(s).")

if __name__ == "__main__":
    main()
