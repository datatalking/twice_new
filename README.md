# Welcome
To start this project, you must have the python environment activated and configured.

If you haven't installed Python yet, please download it from this link: https://www.python.org/downloads/

after installation and configuration, follow these instructions:

# Creating virtual environments

Creation of virtual environments is done by executing the command venv:

python3 -m venv /path/to/new/virtual/environment

after creating the environment navigate to the root to execute this command:

cd pah/ to go to the root
then source bin/activate to activate the environment; once finished you will see

(environment name) $

then navigate to the root of the project, in this frame

(environment name) $ cd /twice_new

Once done, type the following command to install the prerequisites:

pip install -r > req.txt

req.txt is located in the root of the project

once the installations are complete:

type python manage.py collectstatic
then type django runserve to launch the project.
the address will be generated in the terminal like: http://127.0.0.1:8000/
