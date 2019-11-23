from pytube import YouTube
import os

class Youtube_Downloader():
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/storage'

    def download(self, link, quality = '', type = ''):
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path = self.path)