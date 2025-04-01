import os
import yt_dlp

class SongProcessor:
    @staticmethod
    def download_song(audio_url, title):
        temp_webm = f"{title}.webm"
        temp_mp3 = f"{title}.mp3"

        try:
            # Download audio only
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": temp_webm,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
                "ffmpeg_location": "ffmpeg/bin"
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([audio_url])

            return temp_mp3.replace("|", "#")  # returns the mp3 extension
        except Exception as e:
            print(f"Error downloading {title}: {e}")
            return None
