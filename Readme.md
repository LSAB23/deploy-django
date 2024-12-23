# How to use it
1. cd path/to/your/folder containing your project (There should be requirements.txt in the folder for pip to install)

2. `` sudo apt update -y && sudo apt upgrade -y && sudo apt install python3-venv -y && python3 -m venv venv && source venv/bin/activate && pip install deploy-django ``

4. python3 -m deploy --path=path/to/your/folder containing your project --project=Project Name


# Requirements
You dont need to install it, it's installed automatically when the script runs

python-dotenv -> For the .env files
gunicorn -> for running a wsgi server infront of django 

requirements.txt (for your Application) 

# How Does It Work
This works by first changeing the settings file to meet Django's deployment standard, set's up gunicorn and nginx.
A service file is created with yourprojectname.service
