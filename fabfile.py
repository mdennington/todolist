from fabric.api import run, task, local
from fabric.context_managers import settings, cd, prefix


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
        with cd('todolist'):
            run(f'git pull')
            with prefix('workon todolist-venv') :
                run(f'python manage.py collectstatic --noinput')
                run(f'python manage.py migrate')
