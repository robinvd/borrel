# Target Practice Setup
This is a practice project, the base is identical to (most of) the projects
running at Target Holding.

## Requirements
To start you'll need the following software installed on your computer:

 * Docker (>= 1.12)
 * Docker-compose (>= 1.16)
 * An internet connection

## Setup and Start-up
Make sure you can start and build a docker container.
After that you can run the following command from this directory:

```
$ ./> docker-compose up --build
```

A docker container will be started with python 3.4 and it will install dockerize
and the requirements requirements into the new container.

When started, the project is available on [http://127.0.0.1:8000]. The django admin is found at http://127.0.0.1:8000/admin/. There are 2 users pre-defined:

 * admin : admin123456
 * user :  user123456

The admin user is a superuser that can login to the admin site, the "user" user is
a regular user that can not login to the admin.

If you need to get into the running container you can use the following command:

```
$ ./> docker exec -it target_web_1 /bin/bash
```

The application code lives in /code, pip is available to install extra modules.
But be aware that changes made by hand will be discarded every rebuild. To be sure
that extra installed models will be installed with the next build, it is adviced
to add these to the requirements file at target/requirements/base.txt

## Project structure
You don't have to worry about the "docker" folder, this one exists for docker-compose
to run and start a few things to make it work.
The project itself runs from the "web" folder. Within this folder a data folder exists,
this is where the database (sqlite) lives. A media folder is where all uploads are
stored. A requirements folder where the requirements files live. A static folder
where all the static files will be placed after a collectstatic management command
(so nothing should be placed here by hand) and last but definitely not least, the
target folder, where all the code lives.

### Development (target/)
The target folder is the main folder where (most of) the development code lives.
Within this folder you can find a settings folder, a frontend folder, an urls.py
and a wsgi.py file. The Django settings are to be found at target/settings/default.py.
The urls.py is the base urls file, here is where your django app entry points should
be added. You'll find the admin urls and the error urls already added to this file.

The frontend folder is a Django app that will contain all the templates needed to display
the application. Your app(s) should live next to the frontend app, templates and static
files should live in the frontend app.
