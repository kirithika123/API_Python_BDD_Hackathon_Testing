# LMS_Hackathon
Code base for the implementation of Users, Skills, UserSkills and UserSkillsMapping APis for LMS.

Pre-requisites - 

Python 3.10.x (3.9 should be ok) is installed

LMS Database has been restored to postgreSQL

Platform  - windows

***********************************************************************************************************************
Before starting the Flask API server, we need to create a virtual environment in the project folder. This is done to install 
the required packages within the project's environment only. In this way different Python projects can use their required 
versions of the same library/package and be isolated from each other.
***********************************************************************************************************************

#STEPS TO INSTALL AND RUN WITHOUT PYCHARM
-----------------------------------------
Please follow below remaining steps to set up local configurations, set up virtual environment, install packages and start Flask app.

STEPS
------
Note: Project Root is the folder that contains app.py. Please ensure you see this file using 'dir' command before proceeding

1. Download and extract code

2. Modify configuration.py (in project root folder) to set local DB path and API credentials. Steps are given at the top of configuration.py 

3. Execute below commands in windows command shell one by one for initial install and run :-

            cd <Path to Project root>
            
            py -3 -m venv venv

            venv\Scripts\activate.bat

            pip install -r requirements.txt

            set FLASK_APP=app

            flask run

The server will start and run within the Windows command prompt. 
We can start sending and receving data from it.
If this Windows command shell is closed,  the flask server will also stop running.

NOTE - After initial installation, execute below commands everytime you open Windows command prompt to start the app:-

            cd <Path to Project root>

            venv\Scripts\activate.bat

            set FLASK_APP=app

            flask run


To stop Flask API server, simply enter CTR+C or close the command prompt

#STEPS TO INSTALL AND RUN IN PYCHARM
-----------------------------------------
1. Close all projects, and select GetFromVCS from the initial screen
2. In the next screen, if you do not see Git as an option in the Version Control drop-down, select the install Git option to install Git.
   Once this is done, select the GitHub option on the left pane and follow the steps to login to Git on the browser window and give access to PyCharm to access Github.
3. Now, you should be seeing the repositories that you have been given access to, and you should see LMS_Hackathon project on the right pane. Select it and click on Clone.
4. This will load the project and open it up in PyCharm. The next step is to add the virtual environment and the interpreter. Click on the <No Interpreter> button on the bottom    right of the IDE.
5. Click on Add Interpreter.
6. In the window that comes up, leave the default options and click on OK.
7. Now you will be able to see the venv folder created in your project pane.
8. You will also see a banner on top that tells you that there are packages in the requirements.txt that are missing. You can click on “install requirements“ to install these. 
This does the same as <pip install -r requirements.txt>. Alternatively, you can select the PyCharm terminal and type <pip install -r requirements.txt>
9. Once everything is installed, you can verify by checking the site-packages under venv . You should see flask and all related packages here.
10. Now, open up Terminal from PyCharm and run the app using the following commands	
    Set FLASK_APP = app
    flask run
            
            
    This will start the application 

# API_Python_BDD_Hackathon_Testing
#API_Python_BDD_Hackathon_Testing
