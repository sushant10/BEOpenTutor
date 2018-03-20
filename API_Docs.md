* API Documentation Primitive for OpenTutor

**Show Users**
----
  Returns json data about all users.

* **URL**

  /allusers

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

