from pytube import YouTube
import os

class Youtube_Downloader():
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/storage'

    def download(self, link, quality = '', extension = ''):
        yt = YouTube(link)
        if extension == '':
            extension = 'mp4'
        try:
            if quality == '':
                res = yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first().download(output_path = self.path)
            else:
                res = yt.streams.filter(progressive=True, file_extension=extension, resolution=quality).first().download(output_path = self.path)
            return True, res
        except Exception as e:
            return False, str(e)

    def get_resolution(self, link):
        yt = YouTube(link)
        try:
            resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True).all()]
            return True, resolutions
        except Exception as e:
            return False, str(e)

    def get_type(self, link):
        yt = YouTube(link)
        try:
            types = [stream.mime_type for stream in yt.streams.filter(progressive=True).all()]
            return True, types
        except Exception as e:
            return False, str(e)


if __name__ == "__main__":
    youtube = Youtube_Downloader()
    # r, re = youtube.download(link='https://www.youtube.com/watch?v=Xfw0qJ0Ercc', quality='360p')
    # print(r, re)
    yt = YouTube("https://www.youtube.com/watch?v=Xfw0qJ0Ercc")
    print([stream.mime_type for stream in yt.streams.filter(progressive=True).all()])