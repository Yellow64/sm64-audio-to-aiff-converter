import ffmpeg
import os

with open('supported-audio-types.txt') as f:
    lines = f.read().split(", ")

audiofile = input("Insert audio file directory here: ")

print("")

if not ".aiff" in os.path.splitext(audiofile):
    if any(line in audiofile for line in lines):
        try:
            stream = ffmpeg.input(audiofile)
            stream = ffmpeg.output(stream, os.path.splitext(audiofile)[0] + ".aiff", ac="1", ar="32000", loglevel="quiet")
            ffmpeg.run(stream)
            print("File successfully converted with no errors.")
        except:
            print("Error: the file or directory was not found.")
    else:
        if not "/" in os.path.splitext(audiofile):
            print("Error: the file or directory was not found.")
        else:
            print("The file is not an audio file!")
else:
    print("The file is already an aiff file!")