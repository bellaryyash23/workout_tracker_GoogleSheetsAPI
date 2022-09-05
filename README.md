# 🏋️‍♂️Workout Tracking App using Requests API of Python

🌟A very useful program which makes use of Natural Language Processing, API Requests methods to GET and POST data and use of Google sheets to track this workout data.

👉In the 'main.py' file, first the physical details of user are added. Next, the input from user is asked which the user can enter in normal english language.This input
is then passes as a query along with the body stature details to the Nurition API endpoint(https://trackapi.nutritionix.com/v2/natural/exercise). 

👉The Nurition API converts this natural language input to a more useful json data and passes it back as a response to the POST request made by user. It provides 
very accurate data which contains the fields like the Workout Name, Duration of Workout, Calories burnt, etc.

![NLP input](https://github.com/bellaryyash23/workout_tracker_GoogleSheetsAPI/blob/master/input.JPG?raw=true)

👆Input from user in Natural Language👆

👉Next, the received data is updated into the Google Sheet using the Sheety API endpoint (https://sheety.co/). The Sheety API makes it possisible for 
editing and updating google sheets using API requests POST method. 

👉The data is formated according to the column values of the google sheet. Once, the user enters his input workout consecutively the data is updated into the google sheet.
This makes tracking workouts and calories easy and hassle-free.

![Google Sheet with data updated](https://github.com/bellaryyash23/workout_tracker_GoogleSheetsAPI/blob/master/sheet.JPG?raw=true)

👆Google Sheet with updated NLP converted data👆 
