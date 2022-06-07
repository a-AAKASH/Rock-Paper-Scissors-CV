# A simple Computer Vision project for playing Rock, Paper and Scissors. 

## Creating the model 

The model for the project was created using the Teachable-Machine (https://teachablemachine.withgoogle.com) by Google.
The readme file has also been created to document the total flow of this project. 


## Installing the dependencies 

A new virtual environment was created for this project. The environment consists of tensorflow, ipykernel and opencv-python among the other simple python libraries that helps to work on this -- of which are listed and saved in the requirements.txt file in the project folder. 

Also, the model is run in the local machine using a snippet of code presented in the main.ipynb file. This code has been borrowed from Aicore. At the end of the file, a waitKey(1) has been added as without it the window does not seem to close after a key input (i.e. 'q' in this case). (The device I am working on is M1 mac). 


## Create a Rock-Paper-Scissors Game

The <manual_rps.py> file represents the code for the game which can be played without the camera. 
the 'random' module is imported to aid the computer to select between the three options within a function. Also, another function to take the input from the user is formulated. Again, another function that decides whether the computer or the user has won the game is created. Here, an if-elif-else loop is used to come to the decision. 