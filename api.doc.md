# Take Note of 
1. * indicates required and not * indicates optional. 
- if required and no data is passed, that request is going to fail

# courses 
### Creating a course
- endpoint: "/course"
- method: POST
- expected_body:

        ```
            {
                "name": "Algorithms | updated - 1",
                "description": "This is one of the most important concepts in the computer and in life in general.",
            }
        ```

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


# Content
- A content cannot exist without a corresponding course 

### Get all Content
- endpoint "/course/content/list"
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
- endpoint "/course/content/id"
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
- endpoint "/course/content/list"
- method: POST
- expected body: 

```
    {
        "title": "Looping in Algorithms", *
        "description": "this is the text that has to be displyed to the user showing more stuff", *
        "course": 4 *
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
- endpoint "/assignment/mcq-question/list"
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
- endpoint "/assignment/mcq-question/list"
- method: POST
- expected body: 

``` 
{

       "question": "Which loop is infinite",
       "assignment": id

}

```


### Viewing a signle MCQ Question 
- endpoint "/assignment/mcq-question/id"
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
- endpoint "/assignment/mcq-question/choice/list"
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
- endpoint "/assignment/mcq-question/choice/list"
- method: POST
- expected body: 
```
{
            "answer": "all of the above",
            "is_correct": false,
            "mcq-question": 4
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
- endpoint "/assignment/mcq-question/choice/id"
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
- endpoint "/assignment/mcq-question/choice/id"
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
- endpoint "/assignment/mcq-question/choice/id"
- method: DELETE
- expected body: None
- expected result if successfull: 
```
{
    "message": "MCQ Choice successfully deleted"
}

```


# Structural question 

- endpoint "/assignment/strut-question/list"
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

- endpoint "/assignment/strut-question/list"
- method: POST
- expected body: 

```

 {

        "question": "Write an algorithm to add two numbers",
        "answer": "",
        "question": 1
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
