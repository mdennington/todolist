from fabric.api import run, task, local


@task
def gitlog():
    local('git log --oneline')


# @task
# def deploy(c):
#     run('pip freeze > requirements.txt')
#     run('git add .')
#     print("enter your git commit comment: ")
#     comment = input()
#     run('git commit -m "%s"' % comment)
#     run('git push -u origin master')
#     run('')
#     with settings(host_string=f'mdennington@ssh.pythonanywhere.com'):
#         with prefix('workon todolist-venv'):
#             run(f'python --version')
