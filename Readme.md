# How to use it
1. cd path/to/your/project folder containing your apps (There should be requirements.txt in the folder for pip to install)

2. `` sudo apt update -y && sudo apt upgrade -y && sudo apt install python3-venv -y && python3 -m venv venv && source venv/bin/activate && pip install deploy-django ``
* note venv should be created in the path above 

3. ``python3 -m deploy --path=path/to/your/project folder containing your apps (There should be requirements.txt in the folder for pip to install) --project=Project Name``


# Requirements
You dont need to install it, it's installed automatically when the script runs

python-dotenv -> For the .env files
gunicorn -> for running a wsgi server infront of django 

requirements.txt (for your Application) 

# How Does It Work
This works by first changeing the settings file to meet Django's deployment standard, set's up gunicorn and nginx.
A service file is created with yourprojectname.service
