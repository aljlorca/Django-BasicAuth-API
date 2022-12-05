import base64
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

## Function to autenticate via HTTP_AUTHORIZATION protocole
def request_auth(request):
        try:
            auth = request.META.get('HTTP_AUTHORIZATION')
            auth_splited = auth.split()
            if len(auth_splited) == 2:
                if auth_splited[0].lower() == "basic":
                    decoeded_auth= base64.b64decode(auth_splited[1])
                    decoeded_auth = str(decoeded_auth)  
                    decoeded_auth=decoeded_auth.split(':')
                    user = decoeded_auth[0]
                    user = user[2:]
                    password = decoeded_auth[1]
                    try:
                        u = User.objects.get(username=user)
                        userlist = list(User.objects.filter(username=user).values())
                        if check_password(password[:-1], u.password):
                            if u.is_active == True:
                                return userlist
                            else:
                                return {'message-error':'Inactive User',}
                        else:
                            return {'message-error':'Invalid Password',}
                    except:
                        return {'message-error':'User Not Found',}
        except:
            return {'message-error':'You have to authenticate',}