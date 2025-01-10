import os
import jwt
import json

token = os.environ.get('ACTIONS_ID_TOKEN_REQUEST_TOKEN')

print(f'Token: {token}')

try:
    decoded_token = jwt.decode(token, options={"verify_signature": False},  algorithms="RS256")

    print(f'Decoded Token: {json.dumps(decoded_token)}')
except jwt.DecodeError as e:
    raise ValueError('Failed to decode ACTIONS_ID_TOKEN_REQUEST_TOKEN') from e