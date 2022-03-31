# Announcement Generator ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

![python License](https://img.shields.io/badge/MADE%20WITH-Pandas-blue.svg)

This application reads a pre-recorded audio file and extract the needed parts for the announcement from it, this is the one time process. 

After extracting the audio it reads an excel sheet which contains the information about the trains(like train number, train name , platform on which it will arrive, traveling from , traveling to etc.) and generates an announcement for that particular train in Hindi and English language to help passengers.

This Program uses text to speech technology and then merges all the audio files to generate a perfect announcement audio file for all the trains in the sheet.
## Instructions

This script is intended to be used with a Google Sheet file.

* Its a Tool for creating announcement sound files from an excel file and an exported audio track.
* It required internet connection to run the text to speech commands

### Module used
python modules
```
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
```

### How to enter excel file name 
```
# Enter your Excel file path here    (LINE 167)
generateAnnouncement("announce_train.xlsx")    
```

### DEMO
https://user-images.githubusercontent.com/91308138/161117320-7de26072-d8bd-44f6-bf14-5ed4672deccd.mp4

Excel sheet
![sheet](https://user-images.githubusercontent.com/91308138/161117399-870e4192-1d0a-4e26-9779-83d5d5b33c24.PNG)

## PRE-REQUISITES
Your laptop with 3.6.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

* Make sure you have **pandas** installed in python otherwise code may fail, to install pygame in your machine > open python in your terminal then type `pip install pandas` to install. :warning:
* Make sure you have **pydub** installed in python otherwise code may fail, to install pygame in your machine > open python in your terminal then type `pip install pydub` to install. :warning:
* Make sure you have **gTTS** installed in python otherwise code may fail, to install pygame in your machine > open python in your terminal then type `pip install gTTS` to install. :warning:
* os are built-in module so no need to worry about them.

---

Don't Delete any Files or IT MAY CRASH THE PROGRAM!

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/Announcement-Generator.git
2. In source folder, run `python3 'indirail.py'` to start program, optionally, run with `--help` argument to see other runtime options.

### ThankYou!
