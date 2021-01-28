import requests
import os
from bs4 import BeautifulSoup

nowChapterId = 0
lastChapterId = 0
chapterCnt = 0
mhName = ""
try:
    os.makedirs("./result/" + mhName)
except FileExistsError:
    pass
while nowChapterId <= lastChapterId:
    chapterCnt += 1
    comicPage = requests.get("https://www.kanmeizi.cc/chapter/" + str(nowChapterId))
    soup1 = BeautifulSoup(comicPage.text, "lxml")
    imglist = soup1.select(".lazy")
    for i in range(1, len(imglist) + 1):
        soup2 = BeautifulSoup(str(imglist[i - 1]), "lxml")
        with open("./result/" + mhName + "/第" + str(chapterCnt) + "话.html", "a") as docWriter:
            docWriter.write("<img src=\"" + soup2.img["data-original"] + "\">")
    nowChapterId += 1
