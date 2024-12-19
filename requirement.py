import subprocess
import os
def install_requirement(path):
    os.chdir(path)
    try:
        # install requirement.txt
        subprocess.run('pip install -r requirements.txt'.split(), check=True)

        # install python-dotenv
        subprocess.run('pip install python-dotenv'.split(), check=True)
        # install gunicorn
        subprocess.run('pip install gunicorn'.split(), check=True)

        # install nginx
        subprocess.run('sudo apt install nginx'.split(), check=True)
    except subprocess.CalledProcessError as e:
        raise (e, 'check and fix error with pip  this stackoverflow link could help https://stackoverflow.com/questions/75089137/error-failed-building-wheel-for-twisted-iocpsupport') # type: ignore

    return 