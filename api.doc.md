# courses 
## Creating a course

### Edidting a course 
endpoint: "/course"
method: PUT
expected_body:
<br>
        {
            "id": 4,
            "name": "Algorithms | updated - 1",
            "description": "This is one of the most important concepts in the computer and in life in general.",
            "course_content": [1]
        }

    course_content constains the ids of the content of the courses