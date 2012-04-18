
from fabric.api import env, local
import os

env.hosts = ['localhost']
#env.user = 'deploy'
#env.keyfile = ['$HOME/.ssh/deploy_rsa']
#env.directory = '/path/to/virtualenvs/project'
#env.activate = 'source /path/to/virtualenvs/project/bin/activate'

def clean():
    '''
        Clean the *.pyc files from the working tree. Additionally, remove all
        the __pycache__ directories
    '''
    local('find . -type d -name "*__pycache__*" -exec rm -rv {} \;')
    local('find . -iname "*.pyc" -exec rm -v {} \;')
