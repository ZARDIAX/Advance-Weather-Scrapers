# Advance-Weather-Scrapers


Hi everyone my name is Jesus (Jess for the buddies), I'm professional mexican bettor 
with 4 years experience in sports events, who's triying to reach the next level becoming a data analyst.

I decided to create these technological useful tools which extract all scential weather 
data from NFL and MLB teams stadiums. Then I analyze and study this information to make 
a right decision if I feel atracted from some sport event. 

The main functionality of these web scrapers is extract fundamental data like stadium location, 
celsius degrees, current temperatures, real feel, wind, and weather expectations (I use them in my analysis). 
It also has incorpored automatic data extraction by hours, you just need to turn it on removing the "#" in 
code below the comments "Extract Data Automatically" and "Loop While For Turn On Automatic Scraper Function" 
(They're in last part of python code).

Weather is just one more piece from other ones in sports betting analysis, it's an influence 
factor but not absolute when you're in decision-making process and deep analysis. I don't recommend
get into industries that you don't know how them works or you haven't enough information about teams, 
players, etc. This is just a performance about what data I see scential and how I complement with 
technology for make predictive decitions.



### POWERED BY: ZARDIAX & NEXTGNR
This technology is focusing on extract all scential weather data that Sports Bettor will be need for studying a sport event.

Let's import all necessary sources that we gonna use in this web scraper.

     import schedule
     import time
     from selenium import webdriver
     from selenium.webdriver.common.by import By
    
### DATA WEBSITES
We put all stadiums locations links in dictionaries values and team names as keys, this do more practical and easy get info when we'll need to know the weather from some specific location. In my opinion "MSN" website has all info that I could be need.
Is important to say that python comments inside dictionary represents domed stadiums, where weather doesn't influence. So, It wouldn't necessary to get any data.
Please, for correct functionality of this technology don't enter team names with domed stadiums (comment names).


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

### PYTHON CODE
Here's where magic happens, this is the python scraper code.
It starts creating a function (WEATHER EXTRACTOR FUNCTION) which will allow us to extract all information from websites are available inside our dictionary.
                  
                  # WEATHER EXTRACTOR FUNCTION 
                  def extract_weather():

Let's jump to next part (SEARCH YOUR TEAM) which starts with welcome and warning messages, we've an input where we gonna enter a team name for extract their stadium weather information, is necessary to enter a valid key name that's inside dictionary, if information isn't valid our code will stop. So, If we'd like to know weather data from some location, we'll need to write by their key.

                  # SEARCH YOUR TEAM
                  print("\n")
                  print("Glad to you're here, how could i help you?")
                  print("Please, be sure don't write teams with domed stadiums (weather isn't fundamental factor in these cases)")
                  print("\n")
                  search  = input("Choose your team name: ")
                  print("\n")
 
Continuing next part (NAVIGATOR) we've our driver that connect us with every websites which are regristred inside dictionary, next one we've (GET INFO) a driver variable that for each iteration it'll be accessed to dictionary. It's necessary to get a delay of 2 seconds for information can be loaded and processed successfully, so I included it (2 SEC DELAY TIME).
                  
                  # NAVIGATOR
                  driver = webdriver.Chrome("chromedriver.exe")
                  # GET INFO
                  driver.get(stadiums_urls[search])
                  # 2 SEC DELAY TIME
                  time.sleep(2)

Next part we've the places name as a variable and HTML code where our scraper will extract the data and become them in text (EXTRACT INFORMATION FROM).
                  
                  # EXTRACT INFORMATION FROM
                  city = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[1]/div/a").text
        
                  current_weather = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/a").text
        
                  feel_weather = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[1]/div").text
        
                  wind_data = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/div/div[2]").text
        
                  comments = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/p").text
                  
After that we've a little data cleaning, where scraper will replace all "new lines" for empty spaces (DATA CLEANING).

                  # DATA CLEANING
                  current_weather = current_weather.replace("\n", " ").strip()
                  feel_weather = feel_weather.replace("\n", " ").strip()
                  wind_data = wind_data.replace("\n", ": ").strip()
    
We create a csv file with all the data extracted from "city, current_weather, feel_weather, wind_data, comments" variables. 
                  
                  # CREATE A CSV FILE
                  file = open("nfl_weather.csv", "a")
                  file.write(f"{city},{current_weather},{feel_weather},{wind_data},{comments}\n")
                  file.close()  
                
Keeping following the code, the next part will show us extracted and cleaned data in the console (SHOW DATA IN CONSOLE).
  
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
                  
On the other hand, we've close navigator and we've the code which extract automatically every 3 hours the data from team we picked before, next one we close function, last part we've a LOOP WHILE, this turn on the automatic webscraper function.   
    
                  # CLOSE NAVIGATOR    
                  driver.close()
    

                  # EXTRACT DATA AUTOMATICALLY EVERY 3 HOURS
                  schedule.every(3).hours.do(extract_weather)

                  # CLOSE FUNCTION
                  extract_weather()

                  # LOOP WHILE FOR TURN ON AUTOMATIC SCRAPER FUNCTION
                  #while True:
                      schedule.run_pending()
                      time.sleep(2)       
    
We're in the last part of this project, I promise keep y'all updating with new ideas and technologies that I'll create.   
I appreciate your time and interest in reading me, keep walking to the future.

Best regards.
- Jess ;)
    
    
    
    
    
    
    
    
    
    
    
    
    
                  
                  
                  
                  
                  
                  
                  
  
