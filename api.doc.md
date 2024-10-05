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
                "id": 4,
                "name": "Algorithms | updated - 1",
                "description": "This is one of the most important concepts in the computer and in life in general.",
                "course_content": [1]
            }
        ```

    course_content constains the ids of the content of the courses


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