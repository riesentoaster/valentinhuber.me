---
title: Using Transcripts
---

I much prefer listening to reading in general. It's just easier for me to follow and learn that way. However, if you are working with dense material, such as nonfiction books, audio is not always the easiest to work with. I find myself seeking back a couple of seconds or manually transcribing a sentence or paragraph for my notes fairly often. This is annoying. However, there is a better way, using modern transcription engines and players. So here is my workflow:

## Create Transcript

There are many ways of doing this, but the easiest (at least for me) is by creating the transcripts locally, using OpenAI's whisper model, which thankfully is open-weights and thus free to use for everyone. On macOS, this is fairly easy to do using [`mlx_whisper`](https://pypi.org/project/mlx-whisper/) – I'll refer to their documentation for the installation steps. To use it, I've added this line to my `~/.zshrc`:

```bash
alias transcribe='mlx_whisper --model mlx-community/whisper-large-v3-turbo --output-format vtt'
```

Then, create transcripts as follows (running it the first time requires downloading the model first, after that I'm getting approximately 25x real-time transcription speed on a M1 MacBook Pro):

```bash
transcribe "<your-audio-file.mp3>"
```

This will leave you with `your-audio-file.vtt`, which contains the transcript along with timestamps.

## Consume Transcript

For this, I wrote a little static webpage: [riesentoaster.github.io/local-podlove-player/](https://riesentoaster.github.io/local-podlove-player/). First, you add your audio file and your `.vtt` transcription file. Everything happens in your browser, no data leaves your computer. After clicking `Load Player`, you can start your audio. A few notes on the player:
- You can jump to a timestamp in the audio by clicking on the text in the transcript
- You can set the transcript to follow the audio by clicking `Follow Text`
- You can change playback speed by clicking on the speed button in the main player controls