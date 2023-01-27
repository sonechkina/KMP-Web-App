# KMP Web App 

## 1. Aim of the project

The project was developed as part of the exam for the Scientific Programming course (A.A. 2021-2022) of the Bioinformatics for Computational Genomics Master's degree. <br>
The main aim of the project was to develop a Python script of an algorithm that is used in string computation, the Knuth-Morris-Pratt algorithm, for pattern matching on a genome. Then, the algorithm should be implemented into a web application in such a way that the user could type a certain nucleotide sequence and the application would retrieve the number of times the sequence was found in the genome.<br><br>
The main expected outcomes of the application were the following:<br>
1. the Python script should open a web service on a localhost IP and let the port be configurable by the user.
2. The web service should store internally as a file the genome on which the KMP algorithm is run. In this case the genome used was the one of SARS-CoV-2, coming from the NCBI Database ([NCBI Reference Sequence: NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?report=fasta)).
3. The web service should expose an API that allows the user to insert a short nucleotide sequence, which will be in input for the KMP algorithm.
4. As a results, the web server should return the number of occurrences of the small input sequence in the genome of SARS-CoV-2.
5. The application should be implemented as REST (Representational State Transfer) web service, which provides communication between devices and the internet for API-based
tasks. <br><br>

## 2. What does the repository store?
The REST web service can be implemented using a Python-based micro-framework called Flask, which allows to build web applications and to develop RESTful APIs to perform operations using HTTP methods.<br>
In order to meet the project requirements, the scripts and files are stored in the repository in a standardized way for Flask to store all the necessary elements of the web app.<br>
- <b>static</b> folder contains the CSS file
- <b>templates</b> folder contains the HTML page
- <b>venv</b> folder contains the virtual environment that manages all the dependencies of the project, in such a way that the Python libraries are independent from the software's ones.
- <b>api.py</b> file contains the route to HTML page and Python script.
- <b>sequence.txt</b> file contains the SARS-CoV-2 complete genome sequence in form of a text file. Compliant with the requirement, in this way the sequence is internally stored in the web app.

Since the app is quite basic, the CSS and HTML codes could be written internally into the main Python script, but the allocation of these files to the respective folders guarantees a better interoperability: if something has to be modified it can be done in the respective files without compromising the main code on which the app runs.<br> <br>

## 3. Requirements to run the app
These are the programs required (or eventually in need of an update) in order to run the web app:
- Python, from version 3.7 and newer.
- Flask, which will install automatically the Werkzeug distribution that implements WSGI, the standard Python interface between applications and servers.

This web application has been developed in:
- Python 3.9.13
- Flask 2.2.2
- Werkzeug 2.2.2

The OS on which it has been developed and tested is:
- Windows 10.0.22621
<br><br>

## 4. How to execute the app 
In the terminal, go to the location where the KMP Web App is found and change the directory to enter the project folder. <br>
```
> cd .\KMP Web App\ 
```

Before activating the project, activate the corresponding virtual environment. For Windows it will be the following command:<br>
```
> venv/Scripts/activate
```
The shell prompt will change to show the name of the activated environment. <br>

To run the application, it can be used either the ```flask``` command: <br>
```
> flask --app api run 
```
Or it can be used the ```python``` command:<br>
```
> python api.py 
```
In both cases the shell prompt will display the local host URL where the web app is executed. <br>

If you head over to http://127.0.0.1:5000/, and you should see the web application interface.<br>

This is the default IP which represents the machine's ```localhost```, but the user can configure any desired port from the terminal. <br> 
For example, instead of the default ```:5000``` port, the user can change with the ```flask``` command into the ```:8080``` port:
```
> flask --app api run --port 8080
```
<br><br>

## 5. Main steps of development
### a. Development of a basic Flask app
The most basic Flask app has a structure of these 5 main elements:
1. the import of a Flask class in which an instance of this class will be the WSGI application.
    ``` 
    from flask import Flask
    ```
2. The creation of an instance of this class, with the first argument being the name of the application’s module. ```__name__``` is a shortcut for this and it is needed so that Flask knows where to look for resources such as templates and static files.
    ```
    app = Flask(__name__)
    ```
3. A ```route()``` decorator that tells Flask what URL should trigger a function.
     ```
    @app.route("/")
    ```
4. A function that can be defined and returns an output on the user's browser.

5. A command that allows to execute the code when the file runs as a script.
     ```
    if __name__ == "__main__":
        app.run()
    ```

In this application there is just one route, which means that the user can only browse one single URL, and to this route it is bound the main function ```home()``` that basically renders the HTML code of the homepage of the application. <br>
An important feature that must be added to the route decorator is the ```methods``` parameter that enables the Flask route to handle the HTTP requests.<br>
By default, the Flask route responds to ```GET``` requests, but since the main goal of the app is data transmission through an HTML form, the ```POST``` method needs to be added to the URL route in order to send form data that can be further be processed. <br>
In fact the way the ```POST``` request is handled is by the ```request``` object, which contains all the data sent from the client to server. <br><br>
 
### b. Insertion of a Python code into a Flask app
The KMP algorithm has been implemented in Python language following [this tutorial](https://www.youtube.com/watch?v=qgfGXVq7PEQ&t=4322s). <br>
The main characteristic of the KMP algorithm for pattern matching is that it identifies the repeating sub-pattern. In this way it speeds up the computational time compared to a naive algorithm for pattern matching in which in case of a partial mis-match of the string, it has to backtrack completely and start the matching process from the beginning of the pattern.<br>
In fact, the KMP algorithm analyses the pattern to match and keeps track of the history of the pattern, by memorizing the indices of each element of the pattern, avoiding backtracking. <br>
For the implementation of the algorithm, it required two functions:
1. a function for the KMP algorithm that takes the string and the pattern as parameters;
2. a function for the so-called prefix table that stores the indices of the elements of the pattern and is called by the KMP function when there is a mismatch to "remember" at which point the searched pattern did not match the sequence.<br>

In order to insert the KMP algorithm in the Flask app script, these two functions were kept out of the main function of the route. In such a way, the main KMP function was called inside the ```home()``` function.<br><br>

### c. Web interface development with HTML and CSS
The web interface has been developed in HTML and a way to render it in Flask is through the ```render_template``` function in the route. It automatically retrieves the file in the ```templates``` folder and renders it on the user's browser.<br>
The most intuitive way for a user to insert a nucleotide sequence to search would be by means of an HTML form that stores the input data and passes it to the KMP function to retrieve the number of times it has matched on the genome sequence.<br>
The design of the interface has been implemented with a CSS file that is called by the HTML, which automatically retrieves it from its static folder.<br><br>

## 6. How to quit the app
Once you finished working on the project and you want to close the Flask app, first you need to quit the connection to the server by typing ```CTRL+C``` on the terminal.<br>
Then, you can deactivate the ```venv``` by typing on the terminal ```deactivate```. In this way, you are leaving the virtual environment so whatever Python code you will execute, it will not run on your virtual environment.