from config import DROPBOX_API_KEY, DROPBOX_PATH, USE_MOCK_DATA
from dropbox_handler import DropboxHandler
from youtube_handler import YoutubeHandler
from song_processor import SongProcessor

dropbox_handler = DropboxHandler(DROPBOX_API_KEY, DROPBOX_PATH)

def sync_playlist(playlist_url):
    youtube_handler = YoutubeHandler(playlist_url)
    playlist_songs = youtube_handler.get_playlist_videos()
    downloaded_songs = dropbox_handler.get_files_in_folder()

    new_songs = {}

    for item in playlist_songs:
        title = item["title"]
        audio_url = item["url"]

        if title not in downloaded_songs:
            new_songs[title] = audio_url
    
    if new_songs:
        print(f"Found {len(new_songs)} to download:")
        print(",\n".join(map(str, list(new_songs.keys()))))
    
    for title, audio_url in new_songs.items():
        print(f"Downloading: {title} - {audio_url}")
        temp_path = SongProcessor.download_song(audio_url, title)
        if temp_path:
            song_metadata = youtube_handler.get_video_metadata(audio_url)
            dropbox_handler.upload_metadata(song_metadata, title)
            dropbox_handler.upload_file(temp_path)
    return  dropbox_handler.get_data_refined()
