import os


class Config(object):
    SECRET_KEY = os.environ.get('AUTH_TOKEN') or 'you-will-never-guess'
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    AUTHORIZE_URL = 'https://api.openshift.local:8443/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.openshift.local:8443/oauth/token'
    BASE_URL = 'https://api.openshift.local:8443/'
    OAUTH_CREDENTIALS = {
    'openshift': {
        'id': 'system:serviceaccount:examples:oauth-demo',
        'secret': 'secretkeyishere'
        }
    }
