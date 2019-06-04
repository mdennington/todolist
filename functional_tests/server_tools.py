from fabric.api import run
from fabric.context_managers import settings, prefix


def reset_database(host):
    with settings(host_string=f'mdennington@{host}'):
        with prefix('workon todolist-venv'):
            run(f'python todolist/manage.py flush --noinput')


def create_session_on_server(host, email):
    with settings(host_string=f'mdennington@{host}'):
        with prefix('workon todolist-venv'):
            run(f'python --version')
            session_key = run(
                f'python todolist/manage.py createsession {email}')
            return session_key.strip()
