from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import urllib.request
import time

#This code gets the stats for all Heroes in Overwatch Quickplay
counter = 0

def Search(region, platform, battletag):
    url = "https://playoverwatch.com/{}/career/{}/{}".format(region, platform, battletag)
    header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    page = requests.get(url, headers=header)
    soup = bs(page.content, "html.parser")
    # soup2 = bs(soup.prettify(),"html.parser")
    
    if(counter == 0):
        OverwatchData = open(r"C:\Users\Benny Lin\Desktop\Overwatch_Project\OverwatchMetricsApplication\OverwatchData.txt", "w+")
    else:
        OverwatchData = open(r"C:\Users\Benny Lin\Desktop\Overwatch_Project\OverwatchMetricsApplication\OverwatchData.txt", "a+")
    
    header = True
    Heroes = {'Ana' : '0x02E000000000013B',
              'Ashe' : '0x02E0000000000200', 
              'Baptiste' : '0x02E0000000000221',
              'Bastion' : '0x02E0000000000015',
              'Brigitte' : '0x02E0000000000195',
              'D.Va' : '0x02E000000000007A',
              'Doomfist' : '0x02E000000000012F',
              'Genji' : '0x02E0000000000029',
              'Hanzo' : '0x02E0000000000005',
              'Junkrat' : '0x02E0000000000065',
              'Lucio' : '0x02E0000000000079',
              'McCree' : '0x02E0000000000042',
              'Mei' : '0x02E00000000000DD',
              'Mercy' : '0x02E0000000000004',
              'Moira' : '0x02E00000000001A2',
              'Orisa' : '0x02E000000000013E',
              'Pharah' : '0x02E0000000000008',
              'Reaper' : '0x02E0000000000002',
              'Reinhardt' : '0x02E0000000000007',
              'Roadhog' : '0x02E0000000000040',
              'Sigma' : '0x02E000000000023B',
              'Soldier:76' : '0x02E000000000006E',
              'Sombra' : '0x02E000000000012E',
              'Symmetra' : '0x02E0000000000016',
              'Torbjorn' : '0x02E0000000000006',
              'Tracer' : '0x02E0000000000003',
              'Widowmaker' : '0x02E000000000000A',
              'Winston' : '0x02E0000000000009',
              'Wrecking Ball' : '0x02E00000000001CA',
              'Zarya' : '0x02E0000000000068',
              'Zenyatta' : '0x02E0000000000020'}
                
    for characterName, characterID in Heroes.items():
#    OverwatchData.write(characterName +" Data"+ "\n")
       example = soup.findAll("div",{"data-category-id":characterID})
       for e in example:
          data = e.findAll("td",{"class":"DataTable-tableColumn"})
          for d in data:
             if header == True:
                title = d.get_text()
#                 print(d.get_text()+ ", ", end = "")
                OverwatchData.write(characterName + ","+ title + "," + url.split("/")[6].split("-")[0] + ",")
                header = False
             else:
                stats = d.get_text()
#                 print(stats +"\n")
                header = True
                OverwatchData.write(stats + "\n")
       OverwatchData.write("\n")

    OverwatchData.close()

Search("en-us", "pc", "takaharimi-1252")
counter+=1
Search("en-us", "pc", "blin1343-1104")
Search("en-us", "pc", "Imacougar-1290")
Search("en-us", "pc", "dafran-21192")

Overwatch_Stats = pd.read_csv("C:/Users/Benny Lin/Desktop/Overwatch_Project/OverwatchMetricsApplication/OverwatchData.txt", encoding ='unicode_escape', names=["Hero", "Stat", "Player", "Value"])

Heroes_Class = {'Ana' : 'Support',
                'Ashe' : 'Damage', 
                'Baptiste' : 'Support',
                'Bastion' : 'Damage',
                'Brigitte' : 'Support',
                'D.Va' : 'Tank',
                'Doomfist' : 'Damage',
                'Genji' : 'Damage',
                'Hanzo' : 'Damage',
                'Junkrat' : 'Damage',
                'Lucio' : 'Support',
                'McCree' : 'Damage',
                'Mei' : 'Damage',
                'Mercy' : 'Support',
                'Moira' : 'Support',
                'Orisa' : 'Tank',
                'Pharah' : 'Damage',
                'Reaper' : 'Damage',
                'Reinhardt' : 'Tank',
                'Roadhog' : 'Tank',
                'Sigma' : 'Tank',
                'Soldier:76' : 'Damage',
                'Sombra' : 'Damage',
                'Symmetra' : 'Damage',
                'Torbjorn' : 'Damage',
                'Tracer' : 'Damage',
                'Widowmaker' : 'Damage',
                'Winston' : 'Tank',
                'Wrecking Ball' : 'Tank',
                'Zarya' : 'Tank',
                'Zenyatta' : 'Support'}

Overwatch_Stats["Hero Class"] = Overwatch_Stats["Hero"].map(Heroes_Class)

Overwatch_Stats.to_excel("C:/Users/Benny Lin/Desktop/output.xlsx",sheet_name='Overwatch Stats', index=False)
print("Task Completed")