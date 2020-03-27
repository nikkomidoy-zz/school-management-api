# School Management API

API for handling records for schools and students. Check out the project's [documentation](http://nikkomidoy.github.io/school-management-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

API available at this link: `http://127.0.0.1:8000/api/v1/`

# Admin access

After running series of setup which includes migrations, you will have a default admin access as follows:
```
username: admin
email: admin@admin.com
password: adminpassword
```
