import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ALL URLS OF STADIUMS WEATHER FROM MSN
stadiums_urls = {
                  "bears":"https://www.msn.com/en-us/weather/forecast/in-Chicago,IL?ocid=winp2fptaskbar&   loc=eyJhIjoiU29sZGllciBGaWVsZCIsImwiOiJDaGljYWdvIiwiciI6IklMIiwicjIiOiJDb29rIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg3LjYxNjQiLCJ5IjoiNDEuODYyNyJ9&weadegreetype=C", 
                  
                  "bengals":"https://www.msn.com/en-us/weather/forecast/in-Cincinnati,OH?ocid=winp2fptaskbar&loc=eyJhIjoiUGF1bCBCcm93biBTdGFkaXVtIiwibCI6IkNpbmNpbm5hdGkiLCJyIjoiT0giLCJyMiI6IkhhbWlsdG9uIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg0LjUxNTk5ODg0MDMzMjAzIiwieSI6IjM5LjA5NTQwMTc2MzkxNjAxNiJ9&weadegreetype=C",
                  
                  "bills":"https://www.msn.com/en-us/weather/forecast/in-Orchard-Park,Nueva-York?ocid=winp2fptaskbar&loc=eyJhIjoiSGlnaG1hcmsgU3RhZGl1bSIsImwiOiJPcmNoYXJkIFBhcmsiLCJyIjoiTnVldmEgWW9yayIsInIyIjoiQ29uZGFkbyBkZSBFcmllIiwiYyI6IkVzdGFkb3MgVW5pZG9zIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZXMtbXgiLCJ4IjoiLTc4Ljc4ODUiLCJ5IjoiNDIuNzczMiJ9&weadegreetype=C",
                  
                  "broncos":"https://www.msn.com/en-us/weather/forecast/in-Denver,CO?ocid=winp2fptaskbar&loc=eyJhIjoiRW1wb3dlciBGaWVsZCBhdCBNaWxlIEhpZ2giLCJsIjoiRGVudmVyIiwiciI6IkNPIiwicjIiOiJEZW52ZXIgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItMTA1LjAyMSIsInkiOiIzOS43NDQxIn0%3D&weadegreetype=C",
                  
                  "browns":"https://www.msn.com/en-us/weather/forecast/in-Cleveland,OH?ocid=winp2fptaskbar&loc=eyJhIjoiRmlyc3RFbmVyZ3kgU3RhZGl1bSIsImwiOiJDbGV2ZWxhbmQiLCJyIjoiT2hpbyIsInIyIjoiQ3V5YWhvZ2EgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItODEuNjk5NCIsInkiOiI0MS41MDQ4In0%3D&weadegreetype=C",
                  
                  "buccaneers":"https://www.msn.com/en-us/weather/forecast/in-Tampa,FL?ocid=winp2fptaskbar&loc=eyJhIjoiUmF5bW9uZCBKYW1lcyBTdGFkaXVtIiwibCI6IlRhbXBhIiwiciI6IkZsb3JpZGEiLCJyMiI6IkhpbGxzYm9yb3VnaCBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii04Mi41MDMyIiwieSI6IjI3Ljk3NjgifQ%3D%3D&weadegreetype=C",
                  
                  #"cardinals":"domed stadium",
                  #"chargers":"edomed stadium",
                  
                  "chiefs":"https://www.msn.com/en-us/weather/forecast/in-Arrowhead-Stadium?ocid=winp2fptaskbar&loc=eyJsIjoiQXJyb3doZWFkIFN0YWRpdW0iLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItOTQuNDgzOSIsInkiOiIzOS4wNDg5In0%3D&weadegreetype=C",
                  
                  #"colts":"domed stadium",
                  
                  "commanders":"https://www.msn.com/en-us/weather/forecast/in-Hyattsville,MD?ocid=winp2fptaskbar&loc=eyJhIjoiRmVkRXhGaWVsZCIsImwiOiJIeWF0dHN2aWxsZSIsInIiOiJNRCIsInIyIjoiUHJpbmNlIEdlb3JnZSdzIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTc2Ljg2MzgwMDA0ODgyODEyIiwieSI6IjM4LjkwNjc5OTMxNjQwNjI1In0%3D&weadegreetype=C",
                  
                  #"cowboys":"domed stadium",
                  
                  "dolphins":"https://www.msn.com/en-us/weather/forecast/in-Miami-Gardens,FL?ocid=winp2fptaskbar&loc=eyJhIjoiSGFyZCBSb2NrIFN0YWRpdW0iLCJsIjoiTWlhbWkgR2FyZGVucyIsInIiOiJGTCIsInIyIjoiTWlhbWktRGFkZSBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii04MC4yMzcyOTcwNTgxMDU0NyIsInkiOiIyNS45NTcwOTk5MTQ1NTA3OCJ9&weadegreetype=C",
                  
                  "eagles":"https://www.msn.com/en-us/weather/forecast/in-Philadelphia,PA?ocid=winp2fptaskbar&loc=eyJhIjoiTGluY29sbiBGaW5hbmNpYWwgRmllbGQiLCJsIjoiUGhpbGFkZWxwaGlhIiwiciI6IlBBIiwicjIiOiJQaGlsYWRlbHBoaWEgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItNzUuMTY3Mzk2NTQ1NDEwMTYiLCJ5IjoiMzkuOTAwOTAxNzk0NDMzNTk0In0%3D&weadegreetype=C",
                  
                  #"falcons":"domed stadium",
                  
                  "49ers":"https://www.msn.com/en-us/weather/forecast/in-Levi's-Stadium,CA?ocid=winp2fptaskbar&loc=eyJsIjoiTGV2aSdzIFN0YWRpdW0iLCJyIjoiQ0EiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii0xMjEuOTciLCJ5IjoiMzcuNDAzMSJ9&weadegreetype=C",
                  
                  "giants":"https://www.msn.com/en-us/weather/forecast/in-East-Rutherford,NJ?ocid=winp2fptaskbar&loc=eyJhIjoiTWV0TGlmZSBTdGFkaXVtIiwibCI6IkVhc3QgUnV0aGVyZm9yZCIsInIiOiJOSiIsInIyIjoiQmVyZ2VuIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTc0LjA3NzAwMzQ3OTAwMzkiLCJ5IjoiNDAuODEyNjk4MzY0MjU3ODEifQ%3D%3D&weadegreetype=C",
                  
                  "jaguars":"https://www.msn.com/en-us/weather/forecast/in-Jacksonville,FL?ocid=winp2fptaskbar&loc=eyJhIjoiRXZlcmJhbmsgRmllbGQgRHIiLCJsIjoiSmFja3NvbnZpbGxlIiwiciI6IkZMIiwicjIiOiJEdXZhbCBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii04MS42Mzk2MzA0NDkyMTA2IiwieSI6IjMwLjMyMzY0ODcwMTE5MjUifQ%3D%3D&weadegreetype=C",
                  
                  "jets":"https://www.msn.com/en-us/weather/forecast/in-East-Rutherford,NJ?ocid=winp2fptaskbar&loc=eyJhIjoiTWV0TGlmZSBTdGFkaXVtIiwibCI6IkVhc3QgUnV0aGVyZm9yZCIsInIiOiJOSiIsInIyIjoiQmVyZ2VuIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTc0LjA3NzAwMzQ3OTAwMzkiLCJ5IjoiNDAuODEyNjk4MzY0MjU3ODEifQ%3D%3D&weadegreetype=C",
                  
                  #"lions":"domed stadium",
                  
                  "packers":"https://www.msn.com/en-us/weather/forecast/in-Green-Bay,WI?ocid=winp2fptaskbar&loc=eyJhIjoiTGFtYmVhdSBGaWVsZCIsImwiOiJHcmVlbiBCYXkiLCJyIjoiV0kiLCJyMiI6IkJyb3duIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg4LjA2MTMiLCJ5IjoiNDQuNTAxMSJ9&weadegreetype=C",
                  
                  "panthers":"https://www.msn.com/en-us/weather/forecast/in-Charlotte,NC?ocid=winp2fptaskbar&loc=eyJhIjoiQmFuayBvZiBBbWVyaWNhIFN0YWRpdW0iLCJsIjoiQ2hhcmxvdHRlIiwiciI6Ik5DIiwicjIiOiJNZWNrbGVuYnVyZyBDb3VudHkiLCJjIjoiVW5pdGVkIFN0YXRlcyIsImkiOiJVUyIsInQiOjEwMiwiZyI6ImVuLXVzIiwieCI6Ii04MC44NTI3IiwieSI6IjM1LjIyNjEifQ%3D%3D&weadegreetype=C",
                  
                  "patriots":"https://www.msn.com/en-us/weather/forecast/in-Foxborough-(Foxboro),MA?ocid=winp2fptaskbar&loc=eyJhIjoiR2lsbGV0dGUgU3RhZGl1bSBBY2Nlc3MgUmQiLCJsIjoiRm94Ym9yb3VnaCAoRm94Ym9ybykiLCJyIjoiTUEiLCJyMiI6Ik5vcmZvbGsgQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItNzEuMjU4MzU0MTg3MDExNzIiLCJ5IjoiNDIuMDg1OTgzMjc2MzY3MTkifQ%3D%3D&weadegreetype=C",
                  
                  #"raiders":"domed stadium",
                  #"rams":"domed stadium",
                  
                  "ravens":"https://www.msn.com/en-us/weather/forecast/in-Cincinnati,OH?ocid=winp2fptaskbar&loc=eyJhIjoiUGF1bCBCcm93biBTdGFkaXVtIiwibCI6IkNpbmNpbm5hdGkiLCJyIjoiT0giLCJyMiI6IkhhbWlsdG9uIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTg0LjUxNTk5ODg0MDMzMjAzIiwieSI6IjM5LjA5NTQwMTc2MzkxNjAxNiJ9&weadegreetype=C",
                  
                  #"saints":"domed stadium",
                  
                  "seahawks":"https://www.msn.com/en-us/weather/forecast/in-Seattle,WA?ocid=winp2fptaskbar&loc=eyJhIjoiTHVtZW4gRmllbGQiLCJsIjoiU2VhdHRsZSIsInIiOiJXYXNoaW5ndG9uIiwicjIiOiJLaW5nIENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTEyMi4zMzIiLCJ5IjoiNDcuNTkzMiJ9&weadegreetype=C",
                  
                  "steelers":"https://www.msn.com/en-us/weather/forecast/in-Pittsburgh,PA?ocid=winp2fptaskbar&loc=eyJhIjoiSGVpbnogRmllbGQiLCJsIjoiUGl0dHNidXJnaCIsInIiOiJQQSIsInIyIjoiQWxsZWdoZW55IENvdW50eSIsImMiOiJVbml0ZWQgU3RhdGVzIiwiaSI6IlVTIiwidCI6MTAyLCJnIjoiZW4tdXMiLCJ4IjoiLTgwLjAxNTciLCJ5IjoiNDAuNDQ2NyJ9&weadegreetype=C",
                  
                  #"texans":"domed stadium",
                  
                  "titans":"https://www.msn.com/en-us/weather/forecast/in-Nashville,TN?ocid=winp2fptaskbar&loc=eyJhIjoiTmlzc2FuIFN0YWRpdW0iLCJsIjoiTmFzaHZpbGxlIiwiciI6IlRlbm5lc3NlZSIsInIyIjoiRGF2aWRzb24gQ291bnR5IiwiYyI6IlVuaXRlZCBTdGF0ZXMiLCJpIjoiVVMiLCJ0IjoxMDIsImciOiJlbi11cyIsIngiOiItODYuNzczNiIsInkiOiIzNi4xNjY0In0%3D&weadegreetype=C",
                  
                  #"vikings":"domed stadium"
                  }


# EXTRACTOR WEATHER FUNCTION 
def extract_weather():
    
    # SEARCH YOUR TEAM
    print("\n")
    print("Glad to you're here, how could i help you?")
    print("Please, be sure don't write teams with domed stadiums (weather isn't fundamental factor in these cases)")
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

# LOOP WHILE FOR TURN ON AUTOMATIC SCRAPER FUNCTION
#while True:
    #schedule.run_pending()
    #time.sleep(2)