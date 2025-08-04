---
title: Text to Speech
---

After [messing around with automated transcripts]({% post_url blog/random/2025-04-18-Transcriptions %}), I wanted to explore the reverse, creating audio from text.

And, similarly to the above, it turns out it is fairly straightforward with a couple of python libraries.

## How To

Install the required python libraries:

```bash
# direct install
pip install soundfile numpy kokoro
# or in a virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install soundfile numpy kokoro
# if you use a virtual environment, run this command
# before each invocation of the script
source .venv/bin/activate
```

Then, save the following python script to a file (called, say `tts.py`):

```python
import soundfile as sf
import numpy as np
from kokoro import KPipeline
import sys

filename = sys.argv[1]
out_name = ".".join(filename.split(".")[:-1]) + ".mp3"
print(f"Generating based on '{filename}', saving to '{out_name}'")
input_text = open(filename, "r").read()
print("Read input file, creating generator")
generator = KPipeline(lang_code="a")(input_text, voice="af_heart")
print("Generating audio")
audio_segments = []
for i, (gs, _ps, audio) in enumerate(generator):
    if i % 10 == 0:
        print(f"Segment {i}: {gs if len(gs) < 50 else gs[:50] + '...'}")
    audio_segments.append(audio)
print("Concatenating audio")
concatenated_audio = np.concatenate(audio_segments)
print("Saving audio")
sf.write(out_name, concatenated_audio, 24000)
print("Done")
```

Then, execute as follows:

```bash
python3 tts.py <your-input-file.txt>
```

The output will be saved to a file called `<your-input-file.mp3>`.