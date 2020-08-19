import json

from rauth import OAuth2Service
from flask import current_app, url_for, request, redirect


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = current_app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('auth.oauth_callback', provider=self.provider_name,
                       _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]

class OpenshiftSignIn(OAuthSignIn):
    def __init__(self):
        super(OpenshiftSignIn, self).__init__('openshift')
        self.service = OAuth2Service(
            name='openshift',
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://api.openshift.local:8443/oauth/authorize',
            access_token_url='https://api.openshift.local:8443/oauth/token',
            base_url='https://api.openshift.local:8443/'
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            client_id=self.consumer_id,
            approval_prompt="force",
            redirect_uri=self.get_callback_url(),
            response_type='code',
            scope='user:info user:check-access'
        )
        )

    def callback(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        if 'code' not in request.args:
            return None, None, None

        oauth_session = self.service.get_auth_session(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()},
            decoder=decode_json

        )
        me = oauth_session.get('apis/user.openshift.io/v1/users/~').json()
        test = oauth_session.post("apis/authorization.openshift.io/v1/subjectaccessreviews", '{"namespace":"monitoring","resource":"services","verb":"list", "scopes": ["user:full"]}')
        return (
            me['metadata']['uid'],
            me['metadata']['name'],
            me['metadata']['name']+"@cluster.local",
        )
