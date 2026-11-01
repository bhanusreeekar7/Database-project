import os
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from passlib.context import CryptContext
pwd=CryptContext(schemes=['bcrypt'], deprecated='auto'); bearer=HTTPBearer(); SECRET=os.getenv('JWT_SECRET','development-secret'); ALG='HS256'
def hash_password(v): return pwd.hash(v)
def verify_password(v,h): return pwd.verify(v,h)
def token(user_id): return jwt.encode({'sub':str(user_id),'exp':datetime.now(timezone.utc)+timedelta(minutes=int(os.getenv('ACCESS_TOKEN_MINUTES','480')))},SECRET,algorithm=ALG)
def current_user_id(c: HTTPAuthorizationCredentials=Depends(bearer)):
    try: return int(jwt.decode(c.credentials,SECRET,algorithms=[ALG])['sub'])
    except (JWTError, KeyError, ValueError): raise HTTPException(401,'Invalid or expired token')
