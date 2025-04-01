# SyncTube API 🎵
An API to synchornize Dropbox storage music with a YouTube playlist and return the artist, title, and link for frontend playback.

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
	Go to [Dropbox Devs](https://www.dropbox.com/developers) and create a web app to get your OAuth API KEY
	Now, write in your .env file: `DROPBOX_API_KEY=API_KEY` (replace API_KEY for you API KEY)

## Running
- For local
	Execute: `python index.py`
	The API will run at: http://127.0.0.1:5000

- Running/Deploying on Vercel
    - Before you start, make sure you have the following:
	 - [Node.js](https://nodejs.org) installed
	 - Vercel CLI installed. You can install it by running the following command in your terminal:
	 `npm i -global vercel`

	 - if you haven't logged in to Vercel yet, run the following command to log in:
	 `vercel login`
	 Follow the prompts to log in with your Vercel account.
		 
	 - Once you logged in, run:
	 `vercel .`
	 And follow the prompts to set up the API in your server.