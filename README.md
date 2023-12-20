# Playlistpilot Backend

## Introduction

This is the backend for the react app Playlistpilot. The backend hanldes the database fot the information collected from the front end when a user puts in information about a playlist or the songs in those playlists

## Set up

Since this is an unhosted app at the moment there are several steps needed to get the servers up and running

They include:-

1. After cloning the app from github the user should open the folder in vscode
2. In the terminal they should type the command " source .venv/bin/activate" to enter the virtual environment
3. After getting into the virtual environment which will be indicated by seeing (.venv) in the terminal they should then type in "uvicorn main:app --reload" to get the server going
4. After getting the server up they should see the database information start to display on the webpage in the react app
5. To shut down the server use CTRL + C and to leave the virtual environment type deactivate

## Requirements

1. Code editor(Vscode)
2. Github account
3. FastApi installation ("pip install fastapi")
4. Uvicorn installation ("pip install "uvicorn[standard]")

## Troubleshooting

If the server fails unexpectedly shut it down and leave the virtual environment and restart VsCode

## Author: Miriam Wahito Maina

## License: MIT
