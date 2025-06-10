## NRIDS Hackathon 2024 Backend

- [Getting started](#gettingstarted)
- [Post setup](#postsetup)
  - [Starting Django](#postsetup-starting-django)
  - [Create Django Superuser](#postsetup-create-superuser)
  - [Load Django Fixtures](#postsetup-load-fixtures)
  - [Make migrations](#postsetup-make-migrations)
  - [Apply migrations](#postsetup-apply-migrations)
  - [Managing dependencies using Poetry](#postsetup-dependencies)
  - [Recreate database](#postsetup-recreate-database)
  - [Unit tests](#postsetup-unit-tests)
  - [Recreate database](#postsetup-recreate-database)

---

## <a name="gettingstarted"></a>Getting started

When you open the folder, Visual Studio Code will present a notification

```
Folder contains a Dev Container configuration file. Reopen folder to develop in a container (learn more).
```

Dismiss the notification until the initial setup is complete

### <a name="gettingstarted-create-envfile"></a>Create an env file

Create a local copy of the example env file. This file is used to store secrets used by the
app.

*Note:* You will need to update the `OPENAI_API_KEY` value from 1Password

```
# Copy the file and populate .env
cp .env.example .env
```

### <a name="gettingstarted-reopen-in-container"></a>Reopen folder in container

Reopen the `backend` folder in a container by either

- Ensure you have the VSCode extension `Dev Containers` by Microsoft installed
- Clicking the green `><` button in the bottom left of the window and selecting `Remote-Containers: Reopen in Container`, or
- Opening the Command Palette and selecting `Remote-Containers: Reopen in Container`

Visual Studio Code will start the database and Django containers. Any terminal windows opened within Visual Studio Code will be done inside the container.

### <a name="gettingstarted-run-migrations"></a>Run the database migrations

In a Terminal window, enter the following to run the database migrations:

```
python manage.py migrate
```
---

## <a name="postsetup"></a>Post setup

### <a name="postsetup-starting-django"></a>Starting Django

Reopen the `backend` folder in a container by either

- Clicking the green `><` button in the bottom left of the window and selecting `Remote-Containers: Reopen in Container`, or
- Opening the Command Palette and selecting `Remote-Containers: Reopen in Container`

Visual Studio Code will start the database and Django containers and start the development server. Any terminal windows opened within Visual Studio Code will be done inside the container.

If the backend doesn't start on it's own
- click in the top menu `terminal` > `Run Task...` > `backend server`

### <a name="postsetup-create-superuser"></a>Create a superuser to access Django admin

Open a new terminal window in VS Code and run the following command
```
python manage.py createsuperuser
```
You can log into Django admin from http://localhost:8000/admin

### <a name="postsetup-load-fixtures"></a>Load the sample data

Run this command in your terminal window to load the Django fixtures into the database
```
python manage.py import_fixtures
```

### <a name="postsetup-make-migrations"></a>Make migrations

To create any pending database migrations, enter the following

```
python manage.py makemigrations
```

### <a name="postsetup-apply-migrations"></a>Apply migrations

To apply any pending database migrations, enter the following

```
python manage.py migrate
```

### <a name="postsetup-dependencies"></a>Managing dependencies using Poetry

[Poetry](https://python-poetry.org) is used to manage dependencies. Refer to the documentation for a full list of options when [adding](https://python-poetry.org/docs/cli/#add) or [removing](https://python-poetry.org/docs/cli/#remove) packages.

To add or remove a package, enter the following

```
poetry add PACKAGENAME
poetry remove PACKAGENAME
```

To add or remove a package as a development dependency, enter the following

```
poetry add PACKAGENAME -D
poetry remove PACKAGENAME -D
```

### <a name="postsetup-unit-tests"></a>Unit tests

In a Terminal window, enter the following

```
python manage.py runtests
```

### <a name="postsetup-recreate-database"></a>Recreate the MSSQL database

In a Terminal window, enter the following:

```
export PGPASSWORD='django'; dropdb -h nrids_hackathon_database -U django django; createdb -h nrids_hackathon_database -U django django

```

After recreating the database, you will need to [run the migrations](#gettingstarted-run-migrations)


## <a name="postsetup-django-debug-toolbar"></a>Django Debug Toolbar

The [Debug toolbar](https://github.com/jazzband/django-debug-toolbar/) is turned off by default
for performance reasons. To enable it, set `USE_DJANGO_DEBUG_TOOLBAR=true` in your .env file.

Once enabled, the debug toolbar is visible on the side of the browsable API.

---

## <a name="postsetup-swagger"></a>Swagger API documentation

Swagger documentation is available in the local development environment at [http://localhost:8000/api/swagger](http://localhost:8000/api/swagger).

---
