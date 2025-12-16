# autoclip
This is a automatic video clip program.
MVP: Plan to make a program which can input a video to clip different shots
预计功能 Input a video -> Output slicers
Day 1: New File folder
### Setup (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

RUN(Generate Timeline)

source .venv/bin/activate
python -m autoclip.main --input examples/input_videos/sample.mp4 --out clips.json

RUN(Export clips)

source .venv/bin/activate
python -m autoclip.main --input examples/input_videos/sample.mp4 --out clips.json --export



Parameters

--threshold: higher = fewer cuts (try 20–45)

--sample-fps: higher = more sensitive but slower (try 2–5)

--min-clip-sec: filter very short clips (try 1–2)