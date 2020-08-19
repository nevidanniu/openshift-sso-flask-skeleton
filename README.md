# OPENSHIFT-SSO-FLASK-SKELETON
skeleton for flask sso via openshift server.
oauth class contains endpoints to query for user info and
test variable for checking user access.

based on https://github.com/miguelgrinberg/flask-oauth-example/tree/master/templates


##configure
Create serviceaccount and add annotate for route
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    serviceaccounts.openshift.io/oauth-redirectreference.primary: '{"kind":"OAuthRedirectReference","apiVersion":"v1","reference":{"kind":"Route","name":"oauth-demo"}}'
  name: oauth-demo
  namespace: examples
``` 

get token:
```bash
oc sa get-token oauth-demo
```
set config in config.py
```
    'id': 'system:serviceaccount:examples:oauth-demo',
    'secret': 'eyJhbGcIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNUiOiJjaS1leGFtcGxlcyIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJvYXV0aC1kZW1vLXRva2VuLW5ybjdrIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6Im9hdXRoLWRlbW8iLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIzYWY1MzFiNi1kZjJkLTExZWEtYTE2MC1mYTE2M2VjMTU0NWYiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6Y2ktZXhhbXBsZXM6b2F1dGgtZGVtbyJ9.Ys2mrW2YDfAcyr_CNijj7ZRGSleED3RwTZgwv61TFRUjx_PLrAclcX5f2s392UE09ThzIIkziYR1KguR2dzrmbwAo2PzS2QO0Zm5eT_hQj_ATQxDpq15i3mDsXiiG-zxT-VXGHMuh4g9mQuH0UNdtXAbIjS8_jC-A8duplO87tXBHYF1AgOjuyH5fedLkg9d1iIImL9ioCwOQDJ8MNMmLMDmzwcpBDgrVf_OfJKNM7JvAoF65hzCTqYLVQWOI7hEchLeIlNycFMiIGYxHuB1bgbfFdAnmCJfo_b-h0RfH0IjMFdgnY5MCqzgeAchKEMO7oDWXRxhQ1DcrCRTB1mteA'
    
```