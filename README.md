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

RUN

source .venv/bin/activate
python -m autoclip.main --input "examples/input_videos/sample.mp4" --out "clips.json"
