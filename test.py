from unittest import TestCase
import subprocess
import os
from main import deploy
from urllib import request

from pathlib import Path

class CheckIfEverythingIsWorking(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.path = Path('simple_auth').absolute()
        cls.tmp = Path('./tmp').absolute()
        # create a temp file and move the the folder to for the teardown
        os.system(f'cp -r {cls.path} {cls.tmp}')


        deploy.test = False
        deploy.main(f'{cls.path}', 'sAuth')

    def test_django_check(self) -> None:
        os.chdir(self.path)
        subprocess.run('python3 manage.py check'.split(), check=True)
    
    def test_check_static_path(self):
        req = request.Request('http://127.0.0.1/static/htmx.min.js')
        make_request = request.urlopen(req).status
        self.assertEqual(make_request, 200)

    def test_check_auth_path(self):
        req = request.Request('http://127.0.0.1/auth/login/')
        make_request = request.urlopen(req).status
        self.assertEqual(make_request, 200)

    def test_check_servicefile_working(self):
        check = subprocess.call('sudo systemctl is-active --quiet sAuth'.split())
        self.assertEqual(check, 0)

    @classmethod
    def tearDownClass(cls) -> None:
        # replace folder with temp and delete temp
        os.system(f'sudo rm -rf -r {cls.path}')
        os.system(f'cp -r {cls.tmp} {cls.path}')
        os.system(f'sudo rm -rf -r {cls.tmp}')
        
        # remove service file for app

        os.system('sudo systemctl stop sAuth')
        os.system('sudo rm -rf /etc/systemd/system/sAuth.service')
        # delete nginx
        os.system('sudo apt remove nginx -y')
        return 
if __name__ == '__main__':
    main = CheckIfEverythingIsWorking()
    main.run()