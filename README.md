# school-management-api

[![Build Status](https://travis-ci.org/nikkomidoy/school-management-api.svg?branch=master)](https://travis-ci.org/nikkomidoy/school-management-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

API for handling records for schools and students. Check out the project's [documentation](http://nikkomidoy.github.io/school-management-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Initial build of Docker
```bash
docker-compose up --build
```

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

API available at this link: `http://127.0.0.1:8000/api/v1/`

# Admin access

After running series of setup which includes migrations, you will have a default admin access as follows:
```
username: admin
email: admin@admin.com
password: adminpassword
```
