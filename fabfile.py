from fabric.api import run, task, local
from fabric.context_managers import settings


@task
def gitlog():
    local('git log --oneline')


@task
def deploy():
    local('git add .')
    print("enter your git commit comment: ")
    comment = input()
    local('git commit -m "%s"' % comment)
    local('git push -u origin master')
    with settings(host_string=f'mdennington@ssh.pythonanywhere.com'):
        run('cd todolist')
        run('ls -l')
        # run(f'git pull')
        # run(f'python manage.py collectstatic')
        # run(f'python manage.py migrate')
