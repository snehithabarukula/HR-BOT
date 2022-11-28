# HR-BOT
# Introduction 
Worked with a team of four to build a rule-based chatbot for the HR team to create job descriptions automatically using python docs. The chatbot involves two logical entities - The frontend and the Backend. The frontend involves a series of HTML and CSS web pages that displays products and basic design of the website. The backend involves the ML Model (NLP, CNN) and a database management system software where all the responses of the document are stored. 
# Table of Contents
1) Technologies Used
2) System Requirements
3) Set-up
4) Project Flow 

# Technologies Used 
1) Front-end: HR BOT web pages are built using html,css,javascript. 
2) Back-end : AWS, MySQL
 - Database is the heart of the technology platform, where all of the main data related to the website are stored. The Primary database is used to collect the details from the web pages and it's responsible for the data that are shown on UI (front-end). We used Mysql database software.

# System Requirements
1) The system should have Jupyter Notebook or Google Colab to run the ML model. 
2) The required python packages are as follows, (here I have only mentioned the packages that I have used for the developments)


      tensorflow==2.3.1
      nltk==3.5
      colorama==0.4.3
      numpy==1.18.5
      scikit_learn==0.23.2
      Flask==1.1.2
      PyMySQL==1.0.2
      docutils==0.19

# Set Up
you’ll need to know how to setup the following to run the project:

- Set up a anaconda 
- Install Jupyter Notebook
- Pin your project dependencies
- Set up Mysql 
- Start app.py 


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
1) The system should have a python and anaconda setup if you are using Jupyter Notebook.
2) In the next step you need to install a visual code studio or any ide that supports web development languages. 
3) Set up the database usibg MySQL workbench. 
4) Run the HTML pages to see how the bot works.

           
## Project Flow 
The chatbot involves two logical entities - The frontend and the Backend. The frontend involves a series of HTML and CSS web pages that displays products and basic design of the website. The backend involves the ML Model and a database management system software where all the responses of the document is stored. A word doc is created using python docs using the requirements filled using the webpages. 

### Defining Intents
A set of simple intents and bunch of messages that corresponds to those intents are created and also mapped to some responses according to each intent category. 

### Integrating with web application
Once, you train the model, you can integrate your trained chatbot model with any other chat application in order to make it more effective to deal with real world users using flask. we have already developed an application using flask and integrated this trained chatbot model with that application.

## Future Implementations
1) Use more data to train: The training dataset can be expanded. A robust chatbot solution may be created with a sizable dataset and a lot of different intents.
2) Apply different NLP techniques: In order to expand the functionalities of the chatbot, one  may incorporate more NLP solutions like NER (Named Entity Recognition). If the chatbot also has a NER model, you can quickly identify any entity that appears in user chat messages and use it in subsequent chats. Additionally, you may use a sentiment analysis model to detect various emotional undertones in user communications, which will precisely bring some extra hues to your chatbot.
3) Try different neural network architectures: Additionally, I want to experiment with various hyperparameters and different neural network topologies.
Add emojis: One can consider to add emojis while building the models.




