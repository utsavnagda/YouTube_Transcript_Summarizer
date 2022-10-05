from cgitb import text
from traceback import print_tb
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

link = "https://www.youtube.com/watch?v=Cgxsv1riJhI"
video_id = link.split("=")[1]
transcript = YouTubeTranscriptApi.get_transcript(video_id)

full_transcript = ""
for x in transcript:
    full_transcript += " " + x['text']

print(len(full_transcript))

summerizar = pipeline("summarization")

itr = int(len(full_transcript)/400)
summary_text = []
for i in range(0, itr+1):
    start = 0
    start = i*400
    end = (i+1)*400
    out = summerizar(full_transcript[start:end], max_length=57)
    out = out[0]
    out = out["summary_text"]
    summary_text.append(out)

print(summary_text)