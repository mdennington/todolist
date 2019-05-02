from invoke import task, Context
from fabric import Connection, config

import warnings

warnings.filterwarnings(
        action='ignore',
        module=r'.*paramiko*'
)

@task
def gitlog(c):
    local_ctx = Context()
    local_ctx.run('git log --oneline')

@task
def deploy(c):
    local_ctx = Context()
    local_ctx.run('pip freeze > requirements.txt')
    local_ctx.run('git add .')
    print("enter your git commit comment: ")
    comment = input()
    local_ctx.run('git commit -m "%s"' % comment)
    local_ctx.run('git push -u origin master')
    local_ctx.run('heroku maintenance:on')
    local_ctx.run('git push heroku master')
    local_ctx.run('heroku maintenance:off')