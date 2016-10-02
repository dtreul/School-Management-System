#School Management System
###Created by Derrick Treul
###7-22-16

A school management system made using Google App Engine (GAE) and Python. Utilizes RESTful API's to handle requests and stores data in GAE's datastore.

##How to Use:

###To add a student

Send a PUT request to localhost:8080/api/student in body, put student information in JSON format.  
ex -
```
{
    "firstName": "First", 
     "lastName": "Last",
     "idNumber": 12345,
     "department": 14,
     "phone": "123-123-1234",
     "address": 
     {
        "street": "1234 Street rd.",
        "city": "Los Angeles",
        "state": "CA",
        "zipcode": "92807"
     },
     "courses": [1, 2, 3, 1234, 302, 400],
     "units": 100
}
```

###To view a student

Send a GET request to localhost:8080/api/student with a request string of the student's id.  
ex - 

localhost:8080/api/student?idNumber=1234

###To edit a student

Send a POST request to localhost:8080/api/student with a request string of the student's id.  
ex - 
localhost:8080/api/student?idNumber=1234  

in body, put information to be overwritten in JSON format  
ex - 
```
{
  "department": 15,
  "units": 110
}
```


###To delete a student

Send a DELETE request to localhost:8080/api/student with a request string of the student's id.  
ex -  
localhost:8080/api/student?idNumber=1234



---------------------------


adding, editing, and deleting instructors, courses, quarters, and departments are done in the same way.

###Example instructor JSON

```
{
    "firstName": "First", 
     "lastName": "Last",
     "idNumber": 12345,
     "department": 14,
     "phone": "123-123-1234",
     "address": 
     {
        "street": "1234 Street rd.",
        "city": "Los Angeles",
        "state": "CA",
        "zipcode": "92807"
     },
     "courses": [1, 2, 3, 1234, 302, 400]
}
```

###Example department JSON

```
{
    "departmentName": "Math",
    "courses": [1234124, 5324326, 65466],
    "idNumber": 40914
}
```


###Example course JSON

```
{
  "idNumber": 1234,
  "department": 14,
  "courseName": "Calculus",
  "time": "MWF 10:00 - 11:00",
  "place":
  {
    "building": "Smith Hall",
    "roomNumber": 123
  },
  "students": [14214, 244, 3521, 1234, 302, 400],
  "units": 4
}
```

###Example quarter JSON

```
{
  "term": 1, #fall = 1, winter = 2, spring = 3, summer = 4
  "year": 2016,
  "courses": [1242, 4245, 5331, 5353]
}
```

-------------------

###How to drop a student from a course

Send a PUT request to localhost:8080/dropstudent with a request string of courseID and studentID  
example:  
localhost:8080/dropstudent?courseID=1234&studentID=12345


###How to enroll a student to a course

Same as dropping a student, but use url localhost:8080/enrollstudent



------------------


###How to list students enrolled in a course

Send a GET request to localhost:8080/course/students with a request string of idNumber  
example:  
localhost:8080/course/students?idNumber=1234
  
Will return a JSON list of student ID's


-----------------


How to list courses at student is enrolled in 

Send a GET request to localhost:8080/student/courses with a request string of idNumber  
example:  
localhost:8080/student/courses?idNumber=1234

Will return a JSON list of course ID's



-----------------


###How list courses a department offers in a specific quarter  

Send a GET request to localhost:8080/quarter/courses with a request string with year, quarter, and departmentID  
example:  
localhost:8080/api.quarter/courses?year=2016&quarter=3&departmentID=1234

Will return a JSON list of course ID's


------------------

##FRONT END INFORMATION:

###Editing/Adding entities:

   In order to edit any information, please use the method described earlier by directly interacting with the API. Front end does not work correctly.  
   Adding works through the front end.



