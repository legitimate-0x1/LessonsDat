# Made by Sovf!

import os
import json
import urllib.request
import time
import datetime

Lessons = "[]"

if not os.path.exists("Dat"):
    os.mkdir("Dat")

try:
    Lessons = urllib.request.urlopen("https://raw.githubusercontent.com/legitimate-0x1/LessonsDat/refs/heads/main/LessonsDat.json").read().decode("utf-8")
except:
     print("Unable to reach Lessons Info!")

if Lessons != "[]":
    if not os.path.exists("Dat/Lessons.json"):
        with open("Dat/Lessons.json", "w") as LessonsFile:
            LessonsFile.write(Lessons)
elif os.path.exists("Dat/Lessons.json"):
    with open("Dat/Lessons.json", "r") as LessonsFile:
        Lessons = LessonsFile.read()

Lessons = json.loads(Lessons)

DayNamesTbl = {"Monday": "Pazartesi", "Tuesday": "Salı", "Wednesday": "Çarşamba", "Thursday": "Perşembe", "Friday": "Cuma"}
DayNamesTbl2 = {"pazartesi": "Monday", "salı": "Tuesday", "çarşamba": "Wednesday", "perşembe": "Thursday", "cuma": "Friday"}

LocalTime = time.localtime()

TodayName = datetime.date(LocalTime.tm_year, LocalTime.tm_mon, LocalTime.tm_mday).strftime("%A")
TodayNameInTurkish = DayNamesTbl[TodayName]
TodayNameInTurkishLowered = TodayNameInTurkish.lower()

DayNamesTblKeys = list(DayNamesTbl.keys())
TodayNameIndex = DayNamesTblKeys.index(TodayName)

TomorrowName = DayNamesTblKeys[TodayNameIndex + 1]
TomorrowNameInTurkish = DayNamesTbl[TomorrowName]
TomorrowNameInTurkishLowered = TomorrowNameInTurkish.lower()

YesterdayName = DayNamesTblKeys[TodayNameIndex - 1]
YesterdayNameInTurkish = DayNamesTbl[YesterdayName]
YesterdayNameInTurkishLowered = YesterdayNameInTurkish.lower()

print("Ders programı görüntüleyicisine hoş geldiniz! (Örnek: 9/A, bugün / yarın / gün)\n")

if isinstance(Lessons, (list, dict)) and Lessons:
    while True:
        Input = input("Sınıf: ")
        Input2 = input("Gün: ").lower()
        Input2 = Input2 == "bugün" and TodayNameInTurkishLowered or Input2 == "yarın" and TomorrowNameInTurkishLowered or Input2 == "dün" and YesterdayNameInTurkishLowered or Input2

        print(Input2.capitalize(), "günü için", Input, "dersleri:", ", ".join(Lessons[Input][DayNamesTbl2[Input2]]), "\n")
