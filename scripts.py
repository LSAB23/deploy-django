import os
from pathlib import Path
import getpass

def _make_migrations(python :str)->None:
    os.system(f'{python} manage.py makemigrations')
    os.system(f'{python} manage.py migrate')
    return 

def _collectstatic(python :str) -> None:
    os.system(f'{python} manage.py collectstatic')
    return 

# make migrations
def make_migrations(project_path: Path, path: str, project: str, python:str) -> None:
    _path : Path= Path.joinpath(Path(project_path), 'manage.py')
    
    if _path.exists():
        _make_migrations(python)
    else:
        project_path = Path.joinpath(Path(path), project)
        if Path.joinpath(project_path, 'manage.py').exists():
            os.chdir(project_path)
            _make_migrations(python)

        else:
            if Path.joinpath(Path(path), 'manage.py').exists():
                os.chdir(Path(path))
                _make_migrations(python)

                
# collect static
def collectstatic(project_path: Path, path: str, project: str, python :str):
    _path : Path= Path.joinpath(Path(project_path), 'manage.py')
    
    if _path.exists():
        _collectstatic(python)
    else:
        project_path = Path.joinpath(Path(path), project)
        if Path.joinpath(project_path, 'manage.py').exists():
            os.chdir(project_path)
            _collectstatic(python)

        else:
            if Path.joinpath(Path(path), 'manage.py').exists():
                os.chdir(Path(path))
                _collectstatic(python)
# create .env file
def create_env(env: dict) -> None:
    with open('.env', 'w') as env_setting:
        data = ''
        for key,value in env.items():
            data += f"{key} = '{value}'\n"
        env_setting.write(data)

# override the settings file
def create_settings(settings :str) ->None:
    with open('settings.py', 'w') as new_setting:
        new_setting.seek(0)
        new_setting.write(settings)
        new_setting.truncate()

# start gunicorn
def configure_gunicorn(path: str, project: str) -> None:
    print('starting gunicorn')
    os.system(f'gunicorn --workers=2 {project}.wsgi &')
    # add systemctl
    
    print('gunicorn started')

# configure nginx
def configure_nginx(base_dir :Path) -> None:
    
    static_root = Path.joinpath(base_dir, 'static')
    media_root = Path.joinpath(base_dir, 'media')
    user = getpass.getuser()
   
    conf = ''' 
user www-data;
worker_processes  2;

events {
    worker_connections  1024;
}

 http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    server {
        listen 80;

        location /static/ {
            alias  %s;
        }
        location /media/ {
            alias %s;
        }

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
'''

    new_nginx_config = conf%(static_root, media_root)
    # change nginx config
    with open('nginx.conf', 'w') as new_config:
        new_config.seek(0)
        new_config.write(new_nginx_config)
    os.system('sudo mv nginx.conf /etc/nginx/nginx.conf')
    os.chdir('..')
    os.system(f'sudo chown -R {user}:www-data .')
    print(os.system('sudo systemctl restart nginx'), 'starting nginx')

    pass
