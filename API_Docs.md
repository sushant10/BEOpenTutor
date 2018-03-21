# API Documentation Primitive for OpenTutor

## Table of contents
* [Show all majors](#show-all-majors)
* [Show all users](#show-all-users)
* [Find a tutor](#find-a-tutor)


**Show all majors**
----
  Returns array of json objects with all majors along with classes.

* **URL**

  *`/allmajors`*

* **Method:**

  `GET`
  
*  **URL Params**

    N/A

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ```[
                        {
                            "Classes": [
                                "121",
                                "187",
                                "220",
                                ...
                            ],
                            "Major": "Computer Science"
                        },
                        {
                            "Classes": [
                                "131",
                                "132",
                                ....
                            ],
                            "Major": "Mathematics"
                        },...
                  ]```
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ error : "Input not found" }`


**Show all Users**
----
  Returns array of json objects about all users.

* **URL**

  *`/allusers`*

* **Method:**

  `GET`
  
*  **URL Params**

    N/A

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ```{
                      "username":"john.apple@gmail.com",  
                      "FirstName":"John",
                      "LastName":"Appleseed",
                      "major":"Applepie engineer",
                      "requested":true,
                      "requestedAs":["xyz@gmail.com","lkia@gmail.com"],
                      "requestedTo":[],
                      "InProgress":[]
                  }```
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ error : "Input not found" }`


**Find a Tutor**
----
  Returns array of json objects about possible tutors.

* **URL**

  *`/find/<string:major>&<string:classreq>`*

* **Method:**

  `GET`
  
*  **URL Params**

    `major : string` <br />
    `classreq : string`
    
    *major and class the student wants a tutor for*

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ```[
                        {
                            "First Name": "xyz",
                            "Last Name": "abc",
                            "Major": "Computer Science",
                            "Username": "xyzabc@gmail.com"
                        },
                        {
                            "First Name": "dfg",
                            "Last Name": "qwes",
                            "Major": "Computer Science",
                            "Username": "dfg532@gmail.com"
                        }
                ]```
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ error : "Input not found" }`<br />
    **Meaning:** *class not found or major not found*


