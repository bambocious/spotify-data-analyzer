# Spotify Data Analyzer
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A program which takes your entire listening history on Spotify (requested through spotify manually) and processes it to provide valuable insights.

## Usage
This program is still very much under development. Not in a usable state. However, you can still prepare your data:
1. Navigate to https://www.spotify.com/us/account/privacy. Log in if necessary.
2. Scroll down to the heading which says **Download your data**. There are three checkboxes, one for Account data, one for Technical log information, and one for Extending streaming history. I've only ever selected the Extended streaming history option, so I can only provide steps for that.
3. Select that checkbox and hit the big **Request data** button. This should begin the process, and they will send you a link to your email in a few days for a download.
4. Download the file. It should be a zip archive, containing your JSON files and a README document. Extract the files somewhere. You can delete if the README if you like, the program does not require it.
5. When running the program, direct it to the folder that contains your data. The program searches recursively for files that match Spotify's naming scheme + the JSON format, so you can also point it to a folder containing that folder.

