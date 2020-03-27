# School Management API

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

API is available at this link: `http://127.0.0.1:8000/api/v1/`

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Admin access

After running series of setup which includes migrations, you will have a default admin access as follows:
```
username: admin
email: admin@admin.com
password: adminpassword
```

# Time References
Step 1 - Building and structuring the models: 25 minutes

Step 2 - Setup viewsets, serializers and urls: 45 minutes

Step 3 - Implement Django Nested Routers: 30 minutes

Bonus Part - Implement filters, add fake data, add simple documentations: 30 minutes


# Final Notes
Feel free to add comments and other things that might be necessary in implementation
