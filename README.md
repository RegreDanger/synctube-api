# SyncTube API 🎵
An API to synchronize Dropbox storage music with a YouTube playlist and return the artist, title, and link for frontend playback.

## Features 🔥
- Integrated with Dropbox for cloud sotrage

- Extract songs from a YouTube Playlist, then download, convert, and upload each to Dropbox as MP3
- Once the upload is complete, it returns all the data (Dropbox link as RAW for music player, along with the title and the artist to display metadata in the player)

## Installation
- Requirements
    - Python 3.x

- Steps
    - Clone the repository
	`git clone https://github.com/RegreDanger/synctube-api.git`
	
	- Navigate to the folder
	`cd synctube-api.git`
	
	- Install the dependencies
	`pip install -r requirements.txt`
	
	- Set the .env file
	First, create a .env file
	Go to [Dropbox Devs](https://www.dropbox.com/developers) and create a web app to get your OAuth API KEY, APP KEY and SECRET KEY
	Now, write in your .env file: `DROPBOX_API_KEY=API_KEY APP_KEY=API_KEY APP_SECRET_KEY` (replace API_KEY's for your API KEY's)
                 And finally, add your path folder for storage: `DROPBOX_PATH=PATH` (replace PATH for your path).

## Running
Execute: `python index.py`
The API will run at: http://127.0.0.1:5000