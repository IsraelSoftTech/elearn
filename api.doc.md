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