import ast
from utils import check_for_secrets, debug, secrets, allowed_hosts, template, add_some_required, database

def change_settings(parse, env: dict) -> str:
    for line in parse.body:
        if type(line) == ast.Assign:
            for object in line.targets:
                var_name :str = object.id # type: ignore

                if check_for_secrets(var_name):
                    secrets(line, var_name, env)
                if var_name == 'DEBUG':
                    debug(line)
                if var_name == 'ALLOWED_HOSTS':
                    allowed_hosts(line)
                if var_name == 'TEMPLATES':
                    template(line)
                if var_name == 'DATABASES':
                    database(line, env)

    add_some_required(parse)
    return ast.unparse(parse)
