from fabric.api import run
from fabric.context_managers import settings, shell_env


def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py'


# these are SSH commands which need to be converted to
# heroku run bash (runs terminal)

# this is heroku run python manage.py flush --noinput
def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'elspeth@{host}'):
        run(f'{manage_dot_py} flush --noinput')

# do I need env vars ?
def _get_server_env_vars(host):
    env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)

# this could be simply a run of
# heroku run python manage.py createsession edith@example.com
def create_session_on_server(host, email):
# manage_dot_py = _get_manage_dot_py(host)
    local_ctx = Context()
    session_key = local_ctx.run('heroku run python manage.py createsession {email}')

    # with settings(host_string=f'elspeth@{host}'):
    #     env_vars = _get_server_env_vars(host)
    #     with shell_env(**env_vars):
    #         session_key = run(f'{manage_dot_py} createsession {email}')
    return session_key.strip()
