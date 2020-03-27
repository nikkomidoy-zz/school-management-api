# Students
Create, retrieve, update and delete operations for Student

## Get all students information

**Request**:

`GET` `/api/v1/students/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": "http://127.0.0.1:8000/api/v1/students/?page=2",
    "previous": null,
    "results": [
        {
            "id": 38,
            "created": "2020-03-27T08:57:11+0000",
            "modified": "2020-03-27T08:57:11+0000",
            "student_id": "07626942-fb29-4214-9c25-9db2ed7adbd1",
            "first_name": "pang eight",
            "last_name": "pang eight",
            "school": {
                "id": 5,
                "created": "2020-03-27T07:04:39+0000",
                "modified": "2020-03-27T08:56:36+0000",
                "name": "West Sharon",
                "max_student_count": 8
            }
        },
        {
            "id": 30,
            "created": "2020-03-27T08:37:49+0000",
            "modified": "2020-03-27T08:37:49+0000",
            "student_id": "8a1718cf-a481-4b21-9575-4d9cb76c4625",
            "first_name": "asd",
            "last_name": "asd",
            "school": {
                "id": 5,
                "created": "2020-03-27T07:04:39+0000",
                "modified": "2020-03-27T08:56:36+0000",
                "name": "West Sharon",
                "max_student_count": 8
            }
        }
    ]
}
```

## Get specific student data

**Request**:

`GET` `/api/v1/students/:id/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "created": "2020-03-27T07:04:39+0000",
    "modified": "2020-03-27T07:04:39+0000",
    "student_id": "bc2f3a3d-9880-4c6c-8c1c-412e6d6f890d",
    "first_name": "William",
    "last_name": "Marshall",
    "school": {
        "id": 1,
        "created": "2020-03-27T07:04:39+0000",
        "modified": "2020-03-27T07:04:39+0000",
        "name": "Kirstenmouth",
        "max_student_count": 10
    }
}
```
