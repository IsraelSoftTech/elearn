# Take Note of 
1. * indicates required and not * indicates optional. 
- if required and no data is passed, that request is going to fail



# Authentication 
### Login 
- endpoint: "/authentication/login"
- method: POST
- expected_body:

        ```
             {
                "username": "",
                "password": ""
            }
        ```

- expected success result 
 ``` 
   {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTE1NTIxMCwiaWF0IjoxNzI5OTQ1NjEwLCJqdGkiOiI2ZTIzZWQzMWQ1NmQ0OTFjODRlZThkYTAzMWVmOWMwYSIsInVzZXJfaWQiOjF9.AFp7yJy3kgENf67oiNsI6EIH84iLycRkgGiq2UuX7DI",

    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMDMyMDEwLCJpYXQiOjE3Mjk5NDU2MTAsImp0aSI6IjdkYzkxYmFiZWVlMzQwMjQ4YzQ0MGQ0NDM5NjgxYmIyIiwidXNlcl9pZCI6MX0.21ud6_BZBYQyh5TZQyeLNXXfUueezgopof9Mcpwuad8"
}


 ```

 - save the access token and add it into the headers of all the request that you are going to making. the header should look like that below 

 Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMDMyMDEwLCJpYXQiOjE3Mjk5NDU2MTAsImp0aSI6IjdkYzkxYmFiZWVlMzQwMjQ4YzQ0MGQ0NDM5NjgxYmIyIiwidXNlcl9pZCI6MX0.21ud6_BZBYQyh5TZQyeLNXXfUueezgopof9Mcpwuad8'

 that is how the header should look exactly like that for it to work. 

 ### Logout 
 - No request is needed to logout, just delete the authentication token, and when that is done, the user should be considered logout. 

 

# courses 
### Creating a course
- endpoint: "/course"
- method: POST
- expected_body:

        ```
             {
                "name": "Algorithms | updated - 1",
                "description": "This is one of the most important concepts in the computer and in life in general.",
                "teachers": [3]
            }
        ```
- an empty array should be passed if no teacher exist. 

### Edidting a course 
- endpoint: "/course"
- method: PUT
- expected_body:

        ```
            {
                "name": "Algorithms | updated - 1",
                "description": "This is one of the most important concepts in the computer and in life in general.",
                "course_content": [1]
            }
        ```

    course_content constains the ids of the content of the courses and it is optional too, 

### Assigning a teacher to a course
- endpoint: "/course/assign-tutor"
- method: POST
- expected_body:

        ```
           {
            "course": 1 // course id, 
            "teachers": [3,] // teachers id is passed inside of an array.
           }
        ```
### Unassigning a teacher to a course
- endpoint: "/course/unassign-tutor"
- method: POST
- expected_body:

        ```
           {
            "course": 1 // course id, 
            "teachers": [3,] // teachers id is passed inside of an array.
           }
        ```



### Deleting a course 
- endpoint: "/course/id"
- method: DELETE
- expected_body: None

- success result
  ```
    {
        "message": "Course deleted successfully"
    }
  ```


### viewing all assignments for a course 
- endpoint: "/course/id/assignment/list"
- e.g. :"/course/4/assignment/list"
- method: GET
- expected_body: None
- success result
``` 
  {
    "data": [
        {
            "id": 4,
            "title": "Algorithms",
            "enrolled_students": 0,
            "teachers": 1,
            "completion": 0
        }
    ]
}

```

### creating an assignment for a particular course 
- endpoint: "/course/id/assignment/list"
- e.g. :"/course/4/assignment/list"
- method: POST
- expected_body: 

``` 

{
        "title": "Design principles for algorithms",
        "description": "At the end of this assignment, the student will better understand how systems are been designed and many more, helping them to know how to get around things for development",
        "reference_link": null,
        "media_content": null,

}

```

# Content
- A content cannot exist without a corresponding course 

### Get all Content for a course
- endpoint "/course/course-id/content/list"
- method: GET

- expected result if successful: 
```
    [
        {
            "id": 1,
            "title": "Looping in Algorithms",
            "description": "this is the text that has to be displyed to the user showing more stuff",
            "media": "/media/files/degree.pdf",
            "created_by": []
        },
        {
            "id": 3,
            "title": "Algorithm design",
            "description": "this is the text that has to be displyed to the user showing more stuff",
            "media": null,
            "created_by": []
        },
        {
            "id": 7,
            "title": "Looping in Algorithms",
            "description": "this is the text that has to be displyed to the user showing more stuff",
            "media": null,
            "created_by": []
        }
    ]
```


### Get single Content
- endpoint "/course/course-id/content/id"
- method: GET

- expected result if successfull: 
  ```
    {
        "id": 1,
        "title": "Looping in Algorithms",
        "description": "this is the text that has to be displyed to the user showing more stuff",
        "media": "/media/files/degree.pdf",
        "created_by": []
    }
  ```

### Creating content
- endpoint "/course/course-id/content/list"
- method: POST
- expected body: 

```
    {
        "title": "Looping in Algorithms", *
        "description": "this is the text that has to be displyed to the user showing more stuff", *
        "media": ""
    }
```

### Updating Content
- endpoint "/course/content/id"
- method: PUT
- expected body: 

```
    {
        "title": "Looping in Algorithms", *
        "description": "this is the text that has to be displyed to the user showing more stuff", *
        "media": ""
        "is_complete": false
    }
```

- expected result if successfull: 
``` 
    {
        "id": 1,
        "title": "Looping in Algorithms | updated",
        "description": "this is the text that has to be displyed to the user showing more stuff",
        "media": "/media/files/degree.pdf",
        "created_by": []
    }

```

### Deleting a Content
- endpoint "/course/content/id"
- method: DELETE
- expected body: None

- expected result if successfull: 
``` 
    {
        "message": "Content deleted successfully."
    }

```



# Assignement 
### View all Assignments 
- endpoint "/assignment/list"
- method: GET
- expected body: None 
- expected result if successfull: 
``` 

    {
        "data":[

            {
                    "id": 2,
                    "title": "Introduction to Algorithm",
                    "description": "This assignment is going to help you understand alot of things about algorithms",
                    "reference_link": null,
                    "media_content": null,
                    "created_by": null,
                    "assigned_students": [],
                    "mcq_questions": [],
                    "struct_questions": []
                
            }
        ]
    
    }

```

### Creating an Assignment 
- endpoint "/assignment/list"
- method: POST
- expected body: 
```
{
        "title": "Introduction to Algorithm",
        "description": "This assignment is going to help you understand alot of things about algorithms",
      
}

```

- expected result if successfull: 
``` 
    {
        "message": "Assignment created successfully.", 
        
    "data": {
                "id": 2,
                "title": "Introduction to Algorithm",
                "description": "This assignment is going to help you understand alot of things about algorithms",
                "reference_link": null,
                "media_content": null,
                "created_by": null,
                "assigned_students": [],
                "mcq_questions": [],
                "struct_questions": []
                }
            }
    

```

### View single Assignment 
- endpoint "/assignment/id"
- method: GET
- expected body: None 

- expected result if successfull:  
```
{
    "data": {
        "id": 1,
        "title": "Introduction to Algorithm",
        "description": "This assignment is going to help you understand alot of things about algorithms",
        "reference_link": null,
        "media_content": null,
        "created_by": 1,
        "assigned_students": [],
        "mcq_questions": [
            1
        ],
        "struct_questions": [
            1,
            2
        ]
    }
}

```


### Updating an Assignment 
- endpoint "/assignment/id"
- method: PUT
- expected body: 
```
     "data": {
        "title": "Introduction to Algorithm | updated",
        "description": "This assignment is going to help you understand alot of things about algorithms",
        "reference_link": null,
        "media_content": null,
        
    }

```


- expected result if successfull:  
```
{
    "success": "Assignment successfully Updated",
    "data": {
        "id": 2,
        "title": "Introduction to Algorithm | updated",
        "description": "This assignment is going to help you understand alot of things about algorithms",
        "reference_link": null,
        "media_content": null,
        "created_by": null,
        "assigned_students": [],
        "mcq_questions": [],
        "struct_questions": []
    }
}
```

### Deleting an Assignment 
- endpoint "/assignment/id"
- method: DELETE
- expected body: None

- expected result if successfull:  
```
{
    "message", "Assignment successfully delete"
}

```


# MCQ Questions 

### View MCQ Question list 
- endpoint "/assignment/assignment_id/mcq-question/list"
- method: GET
- expected body: None

- expected result if successfull:  
```
{
    "data": [
        {
            "id": 1,
            "choices": [
                {
                    "id": 1,
                    "answer": "While",
                    "is_correct": true
                },
                {
                    "id": 2,
                    "answer": "for",
                    "is_correct": false
                },
                {
                    "id": 3,
                    "answer": "do while",
                    "is_correct": false
                }
            ],
            "question": "Which loop is infinite",
            "question_type": "MCQ"
        }
    ]
}

```

### Creating a MCQ Question  
- endpoint "/assignment/assignment_id/mcq-question/list"
- method: POST
- expected body: 

``` 
{

       "question": "Which loop is infinite",

}

```


### Viewing a signle MCQ Question 
- endpoint "/assignment/assignment_id/mcq-question/id"
- method: GET
- expected body: 

``` 
{
    "data": {
        "id": 1,
        "choices": [
            {
                "id": 1,
                "answer": "While",
                "is_correct": true
            },
            {
                "id": 2,
                "answer": "for",
                "is_correct": false
            },
            {
                "id": 3,
                "answer": "do while",
                "is_correct": false
            }
        ],
        "question": "Which loop is infinite",
        "question_type": "MCQ"
    }
}

```


### Updating a MCQ Question 
- endpoint "/assignment/mcq-question/id"
- method: PUT
- expected body: 
```
{
    "question": "Which loop is infinite"
}

```

### Deleting a MCQ Question 
- endpoint "/assignment/mcq-question/id"
- method: DELETE
- expected body: None

- expected result if successfull: 

```
{
       
        "question": "Which loop is infinite",
        "question_type": "MCQ"
}
```

# MCQ Choices 

### Getting MCQ List
- endpoint "/assignment/assignment_id/mcq-question/mcq_id/choice/list"
- method: GET
- expected body: None 

- expected result if successfull: 

```
{
    "data": [
        {
            "id": 1,
            "answer": "While",
            "is_correct": true
        },
        {
            "id": 2,
            "answer": "for",
            "is_correct": false
        },
        {
            "id": 3,
            "answer": "do while",
            "is_correct": false
        },
        {
            "id": 6,
            "answer": "all of the above",
            "is_correct": false
        }
    ]
}

```

### Creating an MCQ Choice
- endpoint "/assignment/assignment_id/mcq-question/mcq_id/choice/list"
- method: POST
- expected body: 
```
{
            "answer": "all of the above",
            "is_correct": false,
}
- mcq-question is the id of the question
```

- expected result if successfull: 
```
{
    "message": "MCQ choice created successfully",
    "data": {
        "id": 6,
        "answer": "all of the above",
        "is_correct": false
    }
}

```


### viewing a single MCQ Choice 
- endpoint "/assignment/assignment_id/mcq-question/mcq_id/choice/choice_id"
- method: GET
- expected body: None
- expected result if successfull: 

```
{
    "data": {
        "id": 1,
        "answer": "While",
        "is_correct": true
    }
}

```


### updating an MCQ Choice 
- endpoint "/assignment/assignment_id/mcq-question/mcq_id/choice/choice_id"
- method: PUT
- expected body: 

```
{
        "answer": "While  | updated",
        "is_correct": true
}

```

- expected result if successfull: 
```
{
    "success": "MCQ Choice successfully Updated",
    "data": {
        "id": 1,
        "answer": "While  | updated",
        "is_correct": true
    }
}

```


### Deleting an MCQ choice 
- endpoint "/assignment/assignment_id/mcq-question/mcq_id/choice/choice_id"
- method: DELETE
- expected body: None
- expected result if successfull: 
```
{
    "message": "MCQ Choice successfully deleted"
}

```


# Structural question 

### Viewing a structural
- endpoint "/assignment/assignment_id/strut-question/list"
- method: GET
- expected body: None

- expected result if successfull: 
```
{
    "data": [
        {
            "id": 1,
            "question": "What is an Algorithm",
            "answer": "",
            "question_type": "STRUCT"
        },
        {
            "id": 2,
            "question": "How important are aglorithms",
            "answer": "",
            "question_type": "STRUCT"
        },
        {
            "id": 4,
            "question": "1",
            "answer": "",
            "question_type": "STRUCT"
        }
    ]
}
```




### Creating a structural question 

- endpoint "/assignment/assignment_id/strut-question/list"
- method: POST
- expected body: 

```

 {

        "question": "Write an algorithm to add two numbers",
        "answer": ""
}


```
- expected result if successfull: 
```
{
    "message": "Structural Question created successfully",
    "data": {
        "id": 4,
        "question": "1",
        "answer": "",
        "question_type": "STRUCT"
    }
}

```
### Updating a Structural question 
- endpoint "/assignment/assignment_id/strut-question/struct_question_id"
- method: PUT
- expected body: None 

- expected result if successfull: 
```
{
    "data": {
        "id": 1,
        "question": "What is an Algorithm",
        "answer": "This is a finite step that is used to solve a problem",
        "question_type": "STRUCT"
    }
}

```


### Updating a Structural question 
- endpoint "/assignment/assignment_id/strut-question/struct_question_id"
- method: PUT
- expected body: 

```
{
    "question": "What is an Algorithm",
    "answer": "This is a finite step that is used to solve a problem"
}

```

- expected result if successfull: 

```
{
    "success": "Structural question successfully Updated",
    "data": {
        "id": 1,
        "question": "What is an Algorithm",
        "answer": "This is a finite step that is used to solve a problem",
        "question_type": "STRUCT"
    }
}

```



