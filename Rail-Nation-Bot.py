py_name = "Rail-Nation-Bot" 
v = "0.0.1"
####################################################################################################
# #   Intro

f0 =  """ 


- """ + py_name + """
- created by Napo_II
- """ + v + """
- python 2.7
- https://github.com/NapoII/

"""
print(" \nProgramm wird gestartet ...")

####################################################################################################
#import

import os
import os, sys
import time
import pyautogui
from Imports import*

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"


Doku_Folder = Folder_gen (py_name, "Documents/")
Log_Folder = Folder_gen ("Log", ("Documents/"+str(py_name)))
Log_File_name = Datei_name_mit_Zeit ("LogFile-"+str(py_name))
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0 + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])
config_dir = file_path +"/config.ini"

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")

################################################################################################################################
# Load Config

#x = read_config(config_dir, section, option)

Bot_aktiv = str_to_bool(read_config(config_dir, "Telegram", "Bot_aktiv"))
CLINT_ID_imgur = read_config(config_dir, "Imgur", "CLINT_ID_imgur")
Telegram_token = read_config(config_dir, "Telegram", "Telegram_token")
chat_Id = read_config(config_dir, "Telegram", "chat_Id")
fullscrean = parse_int_tuple(read_config(config_dir, "Imgur", "fullscrean"))

Img_Video_dir = (file_path_Bilder + "Video.png")
Img_Play_dir = (file_path_Bilder + "Play.png")
Img_Video_ansehen_dir = (file_path_Bilder + "Video_ansehen.png")
Img_Einloesen_dir = (file_path_Bilder + "Einloesen.png")
Img_Blue_X_dir = (file_path_Bilder + "Blue_X.png")
Img_green_dir = (file_path_Bilder + "green.png")
Img_Nein_danke_dir = (file_path_Bilder + "Nein_danke.png")

Save_Pos = (10,10)

TaskBar_regio =  (3,133,265,906)
Play_regio =  (901,516,236,179)
Video_ansehen_regio =  (791,860,344,92)
Einloesen_regio =  (819,783,277,56)
Blue_X_regio =  (1462,235,46,46)
Nein_danke_regio =  (828,796,268,52)

Time_error_time_max = 200
################################################################################################################################
# Main Programm

Screanshot(TaskBar_regio, "TaskBar_regio_Test", file_path_Bilder)
Screanshot_dir = Screanshot(fullscrean, "Rust - Screen_Start", file_path_Bilder)
TeleBot_Say(f0 + "\n------------------------\n Rail-Nation-Bot wurde gestartet.", chat_Id, Telegram_token)
TeleBot_img("Rail-Nation-Bot", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )


Time_Stemp_A = time.time()
while True:

    green = if_green(Img_green_dir, TaskBar_regio, 0.99)
    Next_Video_pos = if_Video(Img_Video_dir, TaskBar_regio, 0.95)

    if green[0] == True:
        pyautogui.moveTo(green[1][0]+(TaskBar_regio[0]), green[1][1]+(TaskBar_regio[1]))
        pyautogui.click()
        Screanshot(TaskBar_regio, "TaskBar_regio", file_path_Bilder)
        print(">>>>>>> klick <<<<<<<<green")
        Zeit_pause(1)
        pyautogui.moveTo(Save_Pos[0],Save_Pos[1])
        Video_Nr = 0
        green = False
        Time_Stemp_A = time.time()
        continue
        
    if Next_Video_pos[0] == True:

        pyautogui.moveTo(Next_Video_pos[1][0]+(TaskBar_regio[0]), Next_Video_pos[1][1]+(TaskBar_regio[1]))
        pyautogui.click()
        print(">>>>>>> klick <<<<<<<<Next_Video_pos")
        Zeit_pause(0.5)
        pyautogui.moveTo(Save_Pos[0],Save_Pos[1])
        Time_Stemp_A = time.time()
        Video_Nr = 0

        while True:
            if Video_Nr == 2:
                break

            Play_pos = if_Play(Img_Play_dir, Play_regio, 0.85)
            Video_ansehen = if_Video_ansehen(Img_Video_ansehen_dir, Video_ansehen_regio, 0.7)
            Einloesen = if_Einloesen(Img_Einloesen_dir, Einloesen_regio, 0.7)
            Blue_X = if_Blue_X(Img_Blue_X_dir, Blue_X_regio, 0.7)
            Nein_danke = if_Nein_danke(Img_Nein_danke_dir, Nein_danke_regio, 0.7)
            print("Video_Nr: "+str(Video_Nr)+"\n")

            if Play_pos[0] == True:
                pyautogui.moveTo(Play_pos[1][0]+(Play_regio[0]), Play_pos[1][1]+(Play_regio[1]))
                pyautogui.click()
                print(">>>>>>> klick <<<<<<<<Play_pos")
                print(Play_pos)
                Zeit_pause(3)
                pyautogui.moveTo(Save_Pos[0],Save_Pos[1])


            if Video_ansehen[0] == True:
                pyautogui.moveTo(Video_ansehen[1][0]+(Video_ansehen_regio[0]), Video_ansehen[1][1]+(Video_ansehen_regio[1]))
                pyautogui.click()
                print(">>>>>>> klick <<<<<<<<Video_ansehen")
                pyautogui.moveTo(Save_Pos[0],Save_Pos[1])
                Video_Nr = Video_Nr + 1

            if Einloesen[0] == True:
                pyautogui.moveTo(Einloesen[1][0]+(Einloesen_regio[0]), Einloesen[1][1]+(Einloesen_regio[1]))
                pyautogui.click()
                print(">>>>>>> klick <<<<<<<<Einloesen")
                pyautogui.moveTo(Save_Pos[0],Save_Pos[1])
                Video_Nr = Video_Nr + 1

            if Blue_X[0] == True:
                pyautogui.moveTo(Blue_X[1][0]+(Blue_X_regio[0]), Blue_X[1][1]+(Blue_X_regio[1]))
                pyautogui.click()
                print(">>>>>>> klick <<<<<<<<Blue_X")
                pyautogui.moveTo(Save_Pos[0],Save_Pos[1])
                Video_Nr = Video_Nr + 1

            if Nein_danke[0] == True:
                pyautogui.moveTo(Nein_danke[1][0]+(Nein_danke_regio[0]), Nein_danke[1][1]+(Nein_danke_regio[1]))
                pyautogui.click()
                print(">>>>>>> klick <<<<<<<<Nein_danke")
                pyautogui.moveTo(Save_Pos[0],Save_Pos[1])
                Video_Nr = Video_Nr + 1

            Time_Stemp_B = time.time()
            Time_error_time = Time_Stemp_B - Time_Stemp_A
            print("Time_error_time: "+ str(Time_error_time)+"\n")
            if Time_error_time > Time_error_time_max:
                Screanshot_dir = Screanshot(fullscrean, "Rust - Screen_Start", file_path_Bilder)
                TeleBot_Say("\n------------------------\n Rail-Nation-Bot hat ein Problem", chat_Id, Telegram_token)
                TeleBot_img("Rail-Nation-Bot", Screanshot_dir, CLINT_ID_imgur, chat_Id, Telegram_token )

            Zeit_pause(1)