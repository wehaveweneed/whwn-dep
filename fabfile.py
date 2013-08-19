from fabric.api import *
import os

env.output_prefix = False
env.hosts = ["vagrant@127.0.0.1:2222"]
env.password = "vagrant"
env.user = "vagrant"
env.app_root = "whwn"
env.mode = "settings.development"
env.activate = "source ~/.env/bin/activate"
env.environment = "development"
env.f = sudo

def prod():
    env.environment = "production"
    env.f = local

def virtualenv(command):
    """ Run within a VirtualEnv"""
    if env.environment == "production":
        local(command)
    else:
        with prefix('export DJANGO_SETTINGS_MODULE=%s' % env.mode):
            sudo(env.activate + " && " + command)

def bootstrap():
    local('vagrant up && vagrant provision')
    bootstrap_server()

def bootstrap_server():
    gems()
    pips()
    manage("syncdb")
    manage("migrate")

def gems():
    if env.environment is not "production":
        sudo('gem install bundler --no-ri --no-rdoc')
        with cd(env.app_root):
            run('bundle install')

def pips():
    if env.environment is not "production":
        with cd(env.app_root):
            virtualenv('pip install -r requirements.txt')

def serve():
    if env.environment is not "production":
        virtualenv(manage('runserver_plus 0.0.0.0:8000'))

def manage(command):
    if env.environment is "production":
        runner = "heroku"
    else:
        runner = "foreman"
    with cd(env.app_root):
        virtualenv('%s run python app/manage.py %s' % (runner, command))

def coverage_report():
    """ This generates a coverage report in htmlcov """
    manage('jtest --coverage=html-report=htmlcov')

