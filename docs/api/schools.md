# School
Create, retrieve, update and delete operations for School

## Get all schools information

**Request**:

`GET` `/api/v1/schools/`

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
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "created": "2020-03-27T07:04:39+0000",
            "modified": "2020-03-27T07:04:39+0000",
            "name": "Kirstenmouth",
            "max_student_count": 10
        },
        {
            "id": 2,
            "created": "2020-03-27T07:04:39+0000",
            "modified": "2020-03-27T07:04:39+0000",
            "name": "Hodgesberg",
            "max_student_count": 10
        }
    ]
}
```

## Get specific school data

**Request**:

`GET` `/api/v1/schools/:id/`

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
    "name": "Kirstenmouth",
    "max_student_count": 10
}
```

## Get all students in a specific school

**Request**:

`GET` `/api/v1/schools/:id/students/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 5,
            "school": {
                "id": 1,
                "created": "2020-03-27T07:04:39+0000",
                "modified": "2020-03-27T07:04:39+0000",
                "name": "Kirstenmouth",
                "max_student_count": 10
            },
            "created": "2020-03-27T07:04:39+0000",
            "modified": "2020-03-27T07:04:39+0000",
            "student_id": "a3c369fc-91c4-4429-b049-f4cf68c62880",
            "first_name": "Luis",
            "last_name": "Contreras"
        },
        {
            "id": 4,
            "school": {
                "id": 1,
                "created": "2020-03-27T07:04:39+0000",
                "modified": "2020-03-27T07:04:39+0000",
                "name": "Kirstenmouth",
                "max_student_count": 10
            },
            "created": "2020-03-27T07:04:39+0000",
            "modified": "2020-03-27T07:04:39+0000",
            "student_id": "e565ede0-8363-427b-9650-b5024b9c9f36",
            "first_name": "Matthew",
            "last_name": "Perez"
        }
    ]
}
```

## Add a student in a school

**Request**:

`POST` `/api/v1/schools/:id/students/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 39,
    "created": "2020-03-27T09:25:26+0000",
    "modified": "2020-03-27T09:25:26+0000",
    "student_id": "085a03d5-05e4-4110-877a-7c931c597599",
    "first_name": "Another",
    "last_name": "Student",
    "school": {
        "id": 1,
        "created": "2020-03-27T07:04:39+0000",
        "modified": "2020-03-27T07:04:39+0000",
        "name": "Kirstenmouth",
        "max_student_count": 10
    }
}
```
