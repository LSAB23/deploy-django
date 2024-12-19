import sys
from pathlib import Path
import os
import ast
import typing
from requirement import install_requirement


path :str = sys.argv[1]
project :str = sys.argv[2]

project_path :Path = Path.joinpath(Path(path), project)
if not Path.joinpath(project_path.absolute(), 'settings.py').exists():
    project_path :Path= Path.joinpath(project_path, project)

os.chdir(project_path)

get_settings :Path= Path.joinpath(project_path.absolute(), 'settings.py')


open_settings :typing.TextIO= open(get_settings, 'r')
parse = ast.parse(open_settings.read())


env = {}

python = 'py'
if os.name == 'posix':
    python = 'python3'

base_dir = Path(path)

try:
    from scripts import create_env, create_settings, configure_gunicorn, make_migrations, collectstatic, configure_nginx
    from change_settings import change_settings
except ImportError:
    install_requirement(path)
    from scripts import create_env, create_settings, configure_gunicorn, make_migrations, collectstatic, configure_nginx
    from change_settings import change_settings

os.chdir(project_path)
# create settings
settings = change_settings(parse, env)
create_settings(settings)

# create env
create_env(env)

# make_migrations
make_migrations(project_path, path, project, python)

# collectstatic
collectstatic(project_path, path, project,python)

# configure gunicorn
configure_gunicorn(path, project)

# configure nginx

configure_nginx(base_dir)