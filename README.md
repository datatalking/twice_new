# Welcome
To start this project, you must have the python environment activated and configured.

If you haven't installed Python yet, please download it from this link: https://www.python.org/downloads/

Once python installation and configuration are complete, follow these instructions:

### Creating virtual environments

1. Creation of virtual environments is done by executing the command venv:

2. `python3 -m venv /path/to/new/virtual/environment`

3. Then after you have created the environment navigate to the root to execute this command:
4. `cd path/twice_new` to go to the root
5. Then `source bin/activate` to activate the environment; once finished you will see

`(environment name) $`

6. Next step navigate to the root of the project, in this frame

`(environment name) $ cd /twice_new`

7. Once done, type the following command to install the prerequisites:

8. `pip install -r > requirements.txt`

9. `requirements.txt` is located in the root of the project

### Once the installations are complete:

10. Type `python manage.py collectstatic` or `python manage.py makemigrations` depending upon your setup
11. Then type `python manage.py runserver` to launch the project.
12. The address will be generated in the terminal like: `http://127.0.0.1:8000/`


### Project Scope Requirements
1. Github docs list - received
2. README.md - received
3. Installation instructions - in process
4. Virtual Machine venv setup - received
5. Requirements or Setup - in process
6. To add page do this - in process
7. To edit document do this three types - in process
8. To setup database do this - in process
9. Graphic fancy options 1, 2, 3  - in process 


### ERRATA
1. `django runserve` - spelling error and non pythonic, replaced with python manage.py runserver as pythonic
2. `pip install -r > req.txt` non pythonic changed `req.txt` to pythonic `requirements.txt`
3. `cd path/ to go to the root` spelling error changed `pah` to `path`
4. `django==4.1` created errors so i removed the versioning so its now `django`
5. `/andrew` folder needs to be refactored to something pythonic or explicit. `client`
6. `README.md` reformatted for ease of reading to be pythonic.

### Needs
1. 012723 - created issue `admin access`
2. 012723 - Items 3, 5, 6, 7, 8, and 9 were added to `README.md` and need tobe completed
3. 012723 - provide approximate schedule for delivery and schedule zoom call day of delivery for review together
4. 