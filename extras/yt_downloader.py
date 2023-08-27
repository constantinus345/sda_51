#pip install pytube

import pytube
import ffmpeg

def conversie_audio(input_path, output_path):
    ffmpeg.input(input_path).output(output_path, format='mp3').run()
    print("Conversia finalizata")
def descarca_video(link_youtube, folder):

    yt = pytube.YouTube(link_youtube)
    title = yt.title
    print(title)

    audio_streams = yt.streams.filter(only_audio=True).order_by("abr").desc()
    #am scos cel mai calitativ audio stream
    audio_highest = audio_streams.first()

    fisier_path = f"{title}.webm"
    audio_highest.download(filename=fisier_path,output_path=folder)
    print(f"Done downloading {title}")

    #pentru conversia de fisiere media-audio poti folosi ffmpeg
    #command-line poate fi facut si in script de python
    #https://pypi.org/project/ffmpeg-python/
    #pip install ffmpeg-python
    input = f"{folder}/{title}.webm"
    output = f"{folder}/{title}_out_1.mp3"
    conversie_audio(input, output)

folder_path = "B:/pyx/SDA/sda_51"
link_y = "https://www.youtube.com/watch?v=nzlTtE5wBds&ab_channel=%C8%98tirilePROTV"
descarca_video(link_youtube=link_y, folder=folder_path)


