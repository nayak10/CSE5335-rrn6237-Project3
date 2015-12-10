# CSE 5335 - Project 3
##### - Rajesh R Nayak (rrn6237)



### Ajax calls on the client side to display the records one-by-one fetched from MongoDB on the server side (Python/Flask)

The data source has been taken from the following website
```sh
https://datahub.io/dataset/fifa-world-cup-2014-all-players
```
- This data is for all the soccer player from 2014 FIFA world cup. Only some data has been selected and used, since only 100 tuples were required for the project.
- MongoDB is used as the NOSQL database. MongoLab was used on Heroku to implement MongoDB

### Heroku toolbelt commands to execute the scripts

The commands have been run from the GIT CMD command line interface.
- Commands used to upload to GitHub
     - **git init**
     - **heroku git:remote -a CSE5335-rrn6237-2**
     - **git remote -v**
     - **git add .**
     - **git commit -m "Version Name"**
     - **git push heroku master**
     - **heroku run bash**

- In some cases, packages have to be installed under bash before running the python program. For example,
    - pip install pymongo

### Important Information to execute the program
        The code works on Mozilla Firefox but does not work on Google Chrome. This may be because of the compatibility issues in JavaScript functions.
        Also, the implementation of server side was done on Flask. The URLs used for executing the program are as follows - 
        https://cse5335-rrn6237-3.herokuapp.com
        https://cse5335-rrn6237-3.herokuapp.com/user/<username>
        https://cse5335-rrn6237-3.herokuapp.com/lotsofdata
        
### Aspects of implementation which were easy 

- Python supports inbuilt packages for MongoDB (pymongo) which made it easy to configure the application.
- Querying the database was done earlier, hence it was not very difficult to fetch the required data

### Aspects of implementation which were hard

- Coding the client side of the project and understanding Ajax/Jquery was the biggest challenge. It took me some time to get thorough with Jquery and to fetch the data from the server as needed.
- The documentation for Heroku MongoLabs to integrate with Python is very limited. Hence, a lot of research had to be done to understand the flow of the application
- Since I had less experience working on Heroku, I had to spend lot of time configuring it to work with Github and to access it.
