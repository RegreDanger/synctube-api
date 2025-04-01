import yt_dlp

class YoutubeHandler:
    def __init__(self, playlist_url):
        self.playlist_url = playlist_url

    def get_playlist_videos(self):
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,  # Only metadata
        }

        playlist_data = []
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(self.playlist_url, download=False)
            if 'entries' in result:
                for entry in result['entries']:
                    playlist_data.append({
                        "title": entry.get('title'),
                        "url": entry.get('url')
                    })
        return playlist_data

    def get_video_metadata(self, video_url):
        ydl_opts = {
            'quiet': True,
            'default_search': 'ytsearch',
            'nocheckcertificate': True,
            'skip_download': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)

        title = info.get("title", "Unknown Title")
        artist = info.get("artist") or info.get("uploader", "Unknown Artist")

        if "NCS - Copyright Free Music" in title:
            artist = "NCS"

        title = title.split(" |")[0]
        title = title.split(" - ")[1]

        return {"title": title, "artist": artist}
