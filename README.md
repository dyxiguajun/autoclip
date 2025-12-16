## Quick Start

```bash
# 1) Setup (recommended)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# (Optional) check ffmpeg (required for --export)
ffmpeg -version

# 2) Run (Generate timeline)
python -m autoclip.main --input examples/input_videos/sample.mp4 --out clips.json

# 3) Run (Export clips)
python -m autoclip.main --input examples/input_videos/sample.mp4 --out clips.json --export

# 4) Example with parameters
python -m autoclip.main \
  --input examples/input_videos/sample.mp4 \
  --out clips.json \
  --export \
  --threshold 35 \
  --sample-fps 3 \
  --min-clip-sec 1.5
