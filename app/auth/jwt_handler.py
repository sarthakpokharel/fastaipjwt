#This file is responsible for signing, encoding and decoding and returning JWTS.

import time
import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')

#Funciton returns generated Tokens (JWTs)
def token_response(t_response):
	return t_response

#Function used for signing the JWT string
def signJWT(username : str, user_role:str):
	payload = {
	'username': username,
	'user_role': user_role,
	"expiry" : time.time() + 86400 #24 hours after login
	}
	token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
	t_response = { #id also can be sent
		"username": username,
		"user_role":user_role,
		"token":token 
	}
	return token_response(t_response)



def decodeJWT(token: str):
	try: 
		decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
		return decode_token if decode_token['expires'] >= time.time() else None
	except:
		return {}



#This part is an INCOMPLETE CODE
def current_user_info(token: str):
    #check validity of token
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALGORITHM])
        username = payload.get('username')
        user_role = payload.get('user_role')
        expiry = payload.get('expiry')
        if expiry < time.time():
            raise jwt.ExpiredSignatureError
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        raise ValueError("Invalid Token")
    return username, user_role, expiry