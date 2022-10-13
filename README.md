# HR-BOT
# Introduction 
 Worked with a team of four at wavelabs technologies, to build a rule-based chatbot for the HR team using Convolution Neural Network and databases. 
# Table of Contents
1) Technologies Used
2) System Requirements
3) Set-up
4) Project Flow 

# Technologies Used 
1) Front-end: HR BOT web pages are built using html,css,javascript. 
2) Back-end : Database is the heart of the technology platform, where all of the main data related to the website are stored. The Primary database is used to collect the details from the web pages and it's responsible for the data that are shown on UI (front-end). We used Mysql database software.

# System Requirements
1) The system should have Jupyter Notebook or Google Colab to run the ML model. 
2)The required python packages are as follows, (here I have only mentioned the packages that I have used for the developments)


# Set Up
you’ll need to know how to setup the following to run the project:

- Set up a virtual environment
- Install Django
- Pin your project dependencies
- Set up a Django project
- Start a Django app


## Installing Python 
[Python](https://www.python.org/downloads/)

### UBUNTU
Ubuntu Linux 20.04 LTS includes Python 3.8.5 by default. You can confirm this by running the following command in the bash terminal:
 

      python3 -V
      Python 3.8.5
You can install pip3 in the bash terminal using:
 
      
      sudo apt install python3-pip
### MAC
macOS "El Capitan" and other more recent versions do not include Python 3. You can confirm this by running the following commands in the zsh or bash terminal to check upon installation:
 
      
      python3 -V
      Python 3.9.0
      
You can similarly check that pip3 is installed by listing the available packages:
 
 
      pip3 list
      
### Windows 
You can then verify that Python 3 was installed by entering the following text into the command prompt:


      py -3 -V
      Python 3.8.6
    
The Windows installer incorporates pip3 (the Python package manager) by default. You can list installed packages as shown:

  
      pip3 list

    

## Project Set Up 
1) The system should have a python setup before setting up django. Installing a latest version of python ide is must.

3) In the next step you need to install a virtualwrapper which is a virtual environment specifically to run this project. 
In cmd create: 


       pip install virtualenwrapper -win
       
Once you've created a virtual environment, and called workon to enter it, you can use pip3 to install Django :
  
  
  
       pip3 install django~=3.1
  

4) Create the virtual environment:
  
  
       mkvirtualenv environment_name
       
6) Install Django :
  
  
       pip install django
       
8) mkdir projects -> cd projects -> django-admin startproject projectname (Here projects is the name of the folder I created on my desktop)
9) To run  the server :
  
  
       python manage.py runserver
       
       
## Project Flow 
The chatbot involves two logical entities - The frontend and the Backend. The frontend involves a series of HTML and CSS web pages that displays products and basic design of the website. The backend involves the ML Model and a database management system software where all the responses of the document is stored. A word doc is created using python docs using the requirements filled using the webpages. 

