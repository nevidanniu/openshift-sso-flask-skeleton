import os


class Config(object):
    SECRET_KEY = os.environ.get('AUTH_TOKEN') or 'you-will-never-guess'
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    OAUTH_CREDENTIALS = {
    'openshift': {
        'id': 'system:serviceaccount:examples:oauth-demo',
        'secret': ''
        }
    }
