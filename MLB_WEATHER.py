import schedule
import time
import csv
from csv import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# ALL URLS OF STADIUMS WEATHER FROM MSN
stadiums_urls = {
                  "angels": "https://www.msn.com/en-us/weather/forecast/in-Anaheim,CA?ocid=winp2fptaskbar&loc=eyJhIjoiQW5nZWwgU3RhZGl1bSBvZiBBbmFoZWltIiwibCI6IkFuYWhlaW0iLCJyIjoiQ2FsaWZvcm5pYSIsInIyIjoiT3JhbmdlIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTExNy44ODMiLCJ5IjoiMzMuODAwMiJ9&weadegreetype=C",

                  "astros": "https://www.msn.com/en-us/weather/forecast/in-Houston,TX?ocid=winp2fptaskbar&loc=eyJhIjoiTWludXRlIE1haWQgUGFyayIsImwiOiJIb3VzdG9uIiwiciI6IlRYIiwicjIiOiJIYXJyaXMgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItOTUuMzU1MiIsInkiOiIyOS43NTcyIn0%3D&weadegreetype=C",

                  "athletics": "https://www.msn.com/en-us/weather/forecast/in-Oakland,CA?ocid=winp2fptaskbar&loc=eyJhIjoiT2FrbGFuZOKAk0FsYW1lZGEgQ291bnR5IENvbGlzZXVtIiwibCI6Ik9ha2xhbmQiLCJyIjoiQ0EiLCJyMiI6IkFsYW1lZGEgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItMTIyLjIwMiIsInkiOiIzNy43NTEyIn0%3D&weadegreetype=C",

                  "blue jays": "https://www.msn.com/en-us/weather/forecast/in-Toronto,Ontario?ocid=winp2fptaskbar&loc=eyJhIjoiUm9nZXJzIENlbnRyZSIsImwiOiJUb3JvbnRvIiwiciI6Ik9udGFyaW8iLCJjIjoiQ2FuYWRhIiwiaSI6IkNBIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTc5LjM4OTMiLCJ5IjoiNDMuNjQxNSJ9&weadegreetype=C",

                  "braves": "https://www.msn.com/en-us/weather/forecast/in-Northeast-Cobb,GA?ocid=winp2fptaskbar&loc=eyJhIjoiVHJ1aXN0IFBhcmsiLCJsIjoiTm9ydGhlYXN0IENvYmIiLCJyIjoiR0EiLCJyMiI6IkNvYmIgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItODQuNDY3MSIsInkiOiIzMy44OTEifQ%3D%3D&weadegreetype=C",

                  "brewers": "https://www.msn.com/en-us/weather/forecast/in-Milwaukee,WI?ocid=winp2fptaskbar&loc=eyJhIjoiQW1lcmljYW4gRmFtaWx5IEZpZWxkIiwibCI6Ik1pbHdhdWtlZSIsInIiOiJXSSIsInIyIjoiTWlsd2F1a2VlIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg3Ljk3MDEiLCJ5IjoiNDMuMDI4NiJ9&weadegreetype=C",

                  "cardinals": "https://www.msn.com/en-us/weather/forecast/in-St-Louis,MO?ocid=winp2fptaskbar&loc=eyJhIjoiQnVzY2ggU3RhZGl1bSIsImwiOiJTdCBMb3VpcyIsInIiOiJNTyIsInIyIjoiU3QuIExvdWlzIENpdHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii05MC4xOTI5IiwieSI6IjM4LjYyMjUifQ%3D%3D&weadegreetype=C",

                  "cubs": "https://www.msn.com/en-us/weather/forecast/in-Chicago,IL?ocid=winp2fptaskbar&loc=eyJhIjoiV3JpZ2xleSBGaWVsZCIsImwiOiJDaGljYWdvIiwiciI6IklsbGlub2lzIiwicjIiOiJDb29rIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg3LjY1NjIiLCJ5IjoiNDEuOTQ3NiJ9&weadegreetype=C",

                  "diamondbacks": "https://www.msn.com/en-us/weather/forecast/in-Phoenix,AZ?ocid=winp2fptaskbar&loc=eyJhIjoiQ2hhc2UgRmllbGQiLCJsIjoiUGhvZW5peCIsInIiOiJBWiIsInIyIjoiTWFyaWNvcGEgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItMTEyLjA2NyIsInkiOiIzMy40NDU1In0%3D&weadegreetype=C",

                  "dodgers": "https://www.msn.com/en-us/weather/forecast/in-Los-Angeles,CA?ocid=winp2fptaskbar&loc=eyJhIjoiRG9kZ2VyIFN0YWRpdW0iLCJsIjoiTG9zIEFuZ2VsZXMiLCJyIjoiQ0EiLCJyMiI6IkxvcyBBbmdlbGVzIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTExOC4yNDIiLCJ5IjoiMzQuMDc1MSJ9&weadegreetype=C",

                  "giants": "https://www.msn.com/en-us/weather/forecast/in-San-Francisco,CA?ocid=winp2fptaskbar&loc=eyJhIjoiT3JhY2xlIFBhcmsiLCJsIjoiU2FuIEZyYW5jaXNjbyIsInIiOiJDQSIsInIyIjoiU2FuIEZyYW5jaXNjbyBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii0xMjIuMzkiLCJ5IjoiMzcuNzc4NSJ9&weadegreetype=C",

                  "guardians": "https://www.msn.com/en-us/weather/forecast/in-Progressive-Field?ocid=winp2fptaskbar&loc=eyJsIjoiUHJvZ3Jlc3NpdmUgRmllbGQiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItODEuNjg1MyIsInkiOiI0MS40OTU4In0%3D&weadegreetype=C",

                  "mariners": "https://www.msn.com/en-us/weather/forecast/in-Seattle,WA?ocid=winp2fptaskbar&loc=eyJhIjoiVC1Nb2JpbGUgUGFyayIsImwiOiJTZWF0dGxlIiwiciI6Ildhc2hpbmd0b24iLCJyMiI6IktpbmcgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItMTIyLjMzMSIsInkiOiI0Ny41OTIifQ%3D%3D&weadegreetype=C",

                  "marlins": "https://www.msn.com/en-us/weather/forecast/in-Marlins-Park?ocid=winp2fptaskbar&loc=eyJsIjoiTWFybGlucyBQYXJrIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTgwLjIxOTciLCJ5IjoiMjUuNzc4MSJ9&weadegreetype=C",

                  "mets": "https://www.msn.com/en-us/weather/forecast/in-Queens,NY?ocid=winp2fptaskbar&loc=eyJhIjoiQ2l0aSBGaWVsZCIsImwiOiJRdWVlbnMiLCJyIjoiTlkiLCJyMiI6IlF1ZWVucyBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii03My44NDc3IiwieSI6IjQwLjc1NjMifQ%3D%3D&weadegreetype=C",

                  "nationals": "https://www.msn.com/en-us/weather/forecast/in-Nationals-Park?ocid=winp2fptaskbar&loc=eyJsIjoiTmF0aW9uYWxzIFBhcmsiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItNzcuMDA3NSIsInkiOiIzOC44NzI4In0%3D&weadegreetype=C",

                  "orioles": "https://www.msn.com/en-us/weather/forecast/in-Baltimore,MD?ocid=winp2fptaskbar&loc=eyJhIjoiT3Jpb2xlIFBhcmsgYXQgQ2FtZGVuIFlhcmRzIiwibCI6IkJhbHRpbW9yZSIsInIiOiJNRCIsInIyIjoiQmFsdGltb3JlIENpdHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii03Ni42MjEzIiwieSI6IjM5LjI4MyJ9&weadegreetype=C",

                  "padres": "https://www.msn.com/en-us/weather/forecast/in-San-Diego,CA?ocid=winp2fptaskbar&loc=eyJhIjoiUGV0Y28gUGFyayIsImwiOiJTYW4gRGllZ28iLCJyIjoiQ0EiLCJyMiI6IlNhbiBEaWVnbyBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii0xMTcuMTU3IiwieSI6IjMyLjcwNzUifQ%3D%3D&weadegreetype=C",

                  "phillies": "https://www.msn.com/en-us/weather/forecast/in-Philadelphia,PA?ocid=winp2fptaskbar&loc=eyJhIjoiQ2l0aXplbnMgQmFuayBQYXJrIiwibCI6IlBoaWxhZGVscGhpYSIsInIiOiJQZW5uc3lsdmFuaWEiLCJyMiI6IlBoaWxhZGVscGhpYSBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii03NS4xNjY2IiwieSI6IjM5LjkwNTgifQ%3D%3D&weadegreetype=C",

                  "pirates": "https://www.msn.com/en-us/weather/forecast/in-Pittsburgh,PA?ocid=winp2fptaskbar&loc=eyJhIjoiUE5DIFBhcmsiLCJsIjoiUGl0dHNidXJnaCIsInIiOiJQQSIsInIyIjoiQWxsZWdoZW55IENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTgwLjAwNzEiLCJ5IjoiNDAuNDQ3MSJ9&weadegreetype=C",

                  "rangers": "https://www.msn.com/en-us/weather/forecast/in-Arlington,TX?ocid=winp2fptaskbar&loc=eyJhIjoiR2xvYmUgTGlmZSBGaWVsZCIsImwiOiJBcmxpbmd0b24iLCJyIjoiVFgiLCJyMiI6IlRhcnJhbnQgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItOTcuMDg0NSIsInkiOiIzMi43NDY4In0%3D&weadegreetype=C",

                  "rays": "https://www.msn.com/en-us/weather/forecast/in-St-Petersburg,FL?ocid=winp2fptaskbar&loc=eyJhIjoiVHJvcGljYW5hIEZpZWxkIiwibCI6IlN0IFBldGVyc2J1cmciLCJyIjoiRkwiLCJyMiI6IlBpbmVsbGFzIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTgyLjY1MjIiLCJ5IjoiMjcuNzY4NCJ9&weadegreetype=C",

                  "reds": "https://www.msn.com/en-us/weather/forecast/in-Cincinnati,OH?ocid=winp2fptaskbar&loc=eyJhIjoiR3JlYXQgQW1lcmljYW4gQmFsbCBQYXJrIiwibCI6IkNpbmNpbm5hdGkiLCJyIjoiT2hpbyIsInIyIjoiSGFtaWx0b24gQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItODQuNTA3NCIsInkiOiIzOS4wOTc2In0%3D&weadegreetype=C",

                  "red sox": "https://www.msn.com/en-us/weather/forecast/in-Boston,MA?ocid=winp2fptaskbar&loc=eyJhIjoiRmVud2F5IFBhcmsiLCJsIjoiQm9zdG9uIiwiciI6Ik1hc3NhY2h1c2V0dHMiLCJyMiI6IlN1ZmZvbGsgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItNzEuMDk4OCIsInkiOiI0Mi4zNDU5In0%3D&weadegreetype=C",

                  "rockies": "https://www.msn.com/en-us/weather/forecast/in-Denver,CO?ocid=winp2fptaskbar&loc=eyJhIjoiQ29vcnMgRmllbGQiLCJsIjoiRGVudmVyIiwiciI6IkNPIiwicjIiOiJEZW52ZXIgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItMTA0Ljk5NCIsInkiOiIzOS43NTYxIn0%3D&weadegreetype=C",

                  "royals": "https://www.msn.com/en-us/weather/forecast/in-Kauffman-Stadium?ocid=winp2fptaskbar&loc=eyJsIjoiS2F1ZmZtYW4gU3RhZGl1bSIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii05NC40ODA2IiwieSI6IjM5LjA1MTQifQ%3D%3D&weadegreetype=C",

                  "tigers": "https://www.msn.com/en-us/weather/forecast/in-Detroit,MI?ocid=winp2fptaskbar&loc=eyJhIjoiQ29tZXJpY2EgUGFyayIsImwiOiJEZXRyb2l0IiwiciI6Ik1pY2hpZ2FuIiwicjIiOiJXYXluZSBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii04My4wNDc0IiwieSI6IjQyLjMzODkifQ%3D%3D&weadegreetype=C",

                  "twins": "https://www.msn.com/en-us/weather/forecast/in-Target-Field?ocid=winp2fptaskbar&loc=eyJsIjoiVGFyZ2V0IEZpZWxkIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTkzLjI3ODMiLCJ5IjoiNDQuOTgxNyJ9&weadegreetype=C",

                  "white sox": "https://www.msn.com/en-us/weather/forecast/in-Chicago,IL?ocid=winp2fptaskbar&loc=eyJhIjoiVS5TLiBDZWxsdWxhciBGaWVsZCIsImwiOiJDaGljYWdvIiwiciI6IklMIiwicjIiOiJDb29rIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg3LjYzNSIsInkiOiI0MS44MzAxIn0%3D&weadegreetype=C",

                  "yankees": "https://www.msn.com/en-us/weather/forecast/in-New-York,NY?ocid=winp2fptaskbar&loc=eyJhIjoiWWFua2VlIFN0YWRpdW0iLCJsIjoiTmV3IFlvcmsiLCJyIjoiTlkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii03My45MjY1IiwieSI6IjQwLjgyOTUifQ%3D%3D&weadegreetype=C"
                  
                  }


# EXTRACTOR WEATHER FUNCTION 
def extract_weather():
    
    # SEARCH YOUR TEAM
    print("\n")
    print("Glad to you're here, how could i help you?")
    print("\n")
    search  = input("Choose your team name: ")
    print("\n")
    
    # NAVIGATOR
    driver = webdriver.Chrome("chromedriver.exe")
        
    # GET INFO
    driver.get(stadiums_urls[search])
    
    # 2 SEC DELAY TIME 
    time.sleep(2)
    
    
    # EXTRACT INFORMATION FROM
    city = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/div/a").text
        
    current_weather = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/a").text
        
    feel_weather = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div").text
        
    wind_data = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div[2]").text
        
    comments = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/p").text
        
    # DATA CLEANING
    current_weather = current_weather.replace("\n", " ").strip()
    feel_weather = feel_weather.replace("\n", " ").strip()
    wind_data = wind_data.replace("\n", ": ").strip()
    
    # CREATE A CSV FILE
    file = open("nfl_weather.csv", "a")
    file.write(f"{city},{current_weather},{feel_weather},{wind_data},{comments}\n")
    file.close()
        
    # SHOW DATA IN CONSOLE
    print("\n")
    print("Your advanced weather report has been cooked successfully ;)")
    print("\n")
    print(city)
    print(current_weather)
    print(feel_weather)
    print(wind_data)
    print(comments)
    print("\n")
    
    # CLOSE DRIVER      
    driver.close()
    

# EXTRACT DATA AUTOMATICALLY EVERY 3 HOURS
#schedule.every(3).hours.do(extract_weather)

# CLOSE FUNCTION
extract_weather()


#while True:
    #schedule.run_pending()
    #time.sleep(2)