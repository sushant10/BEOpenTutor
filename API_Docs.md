# API Documentation Primitive for OpenTutor

**Show all majors (/find/allmajor)**
----
  Returns json data about all users.

* **URL**

  `//find/allmajor`

* **Method:**

  `GET`
  
*  **URL Params**

    N/A

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
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
                  ]`
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ error : "Input not found" }`


**Show Users (/allusers)**
----
  Returns json data about all users.

* **URL**

  `/allusers`

* **Method:**

  `GET`
  
*  **URL Params**

    N/A

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
                      "username":"john.apple@gmail.com",  
                      "FirstName":"John",
                      "LastName":"Appleseed",
                      "major":"Applepie engineer",
                      "requested":true,
                      "requestedAs":["xyz@gmail.com","lkia@gmail.com"],
                      "requestedTo":[],
                      "InProgress":[]
                  }`
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ error : "Input not found" }`

