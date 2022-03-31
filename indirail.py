# Internet connection required to run program
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language,slow=True)
    myobj.save(filename)

def textToSpeechs(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language,slow=True)
    myobj.save(filename)

#this function return pydub audio segments
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    # put your audio file here for extraction
    audio = AudioSegment.from_mp3('railway.mp3')
    # 1- Generate kripiya dheyan dijiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindienglish.mp3", format = "mp3")

    # 2 is from city

    # 3 - Generate se chalker
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindienglish.mp3",format="mp3")

    # 4 is via
    
    # 5 se raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindienglish.mp3",format="mp3")

    # 6 is to city

    # 7 ko janne wali gaadi sankhiya
    start= 96000
    finish= 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindienglish.mp3",format="mp3")

    # 8  train number and name

    # 9 kuchi samay me platform sankhiya
    start= 105500
    finish= 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindienglish.mp3",format="mp3")

    # 10 platform number

    # 11 par aa rahi he
    start= 109000
    finish =112150
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindienglish.mp3",format="mp3")



    # # ENGLISH ANNOUNCEMENTS
    # 12 - Generate may i have your attension please train number
    start = 112000
    finish = 116200
    audioProcessed = audio[start:finish]
    audioProcessed.export("12_hindienglish.mp3",format="mp3")
    
    # 13 - train number and train name 
    # 14 - from 
    start = 122600
    finish = 123480
    audioProcessed = audio[start:finish]
    audioProcessed.export("14_hindienglish.mp3",format="mp3")
    
    # 15 - from station 
    # 16 - to 
    start = 123900
    finish = 124600
    audioProcessed = audio[start:finish]
    audioProcessed.export("16_hindienglish.mp3",format="mp3")
    
    # 17 - to station
    # 18 - via 
    start = 127600
    finish = 128480
    audioProcessed = audio[start:finish]
    audioProcessed.export("18_hindienglish.mp3",format="mp3")
    
    # 19 - via station
    # 20 - is arriving shortly on platform number
    start = 128900
    finish = 132750
    audioProcessed = audio[start:finish]
    audioProcessed.export("20_hindienglish.mp3",format="mp3")
    
    # 21 - platform
    #22 - end
    start = 133400
    finish = 134500
    audioProcessed = audio[start:finish]
    audioProcessed.export("22_hindienglish.mp3",format="mp3")
    
def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindienglish.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindienglish.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindienglish.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindienglish.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindienglish.mp3')
    # audios = [f"{i}_hindienglish.mp3" for i in range(1,12)]      ## for only (hindi announcement 137-140)

    # announcement = mergeAudios(audios)
    # announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")

    # # english 
    # for index, item in df.iterrows():
        # 13 - Generate train no and name
        textToSpeechs(item['train_no'] + " " + item['train_name'], '13_hindienglish.mp3')

        # 15 - Generate from-city
        textToSpeechs(item['from'], '15_hindienglish.mp3')

        # 17 - Generate to-city
        textToSpeechs(item['to'], '17_hindienglish.mp3')

        # 19 - Generate via-city
        textToSpeechs(item['via'], '19_hindienglish.mp3')

        # 21 - Generate platform number
        textToSpeechs(item['platform'], '21_hindienglish.mp3')
        audios = [f"{i}_hindienglish.mp3" for i in range(1,23)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton..")
    generateSkeleton()
    print("Now Generating Announcemenets")
    generateAnnouncement("announce_train.xlsx")    # Enter your Excel file path here
    print("Announcement file has been successfully created in your folder")
     
