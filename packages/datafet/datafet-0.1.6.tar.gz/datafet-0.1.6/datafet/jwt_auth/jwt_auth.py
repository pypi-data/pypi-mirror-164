import base64
import logging
import time

import ecdsa
import jwt
from ecdsa import SigningKey, VerifyingKey
from pydantic import BaseModel, EmailStr

LOG = logging.getLogger(__name__)
DEFAULT_ALGORITHM = "ES256"


class JwtParam(BaseModel):
    email: EmailStr
    firstName: str
    domain: str


def create_jwt(
    jwt_param: JwtParam,
    signing_key: SigningKey,
    audience: str,
    issuer: str,
    exp_days=2,
    algorithm=DEFAULT_ALGORITHM,
):

    now = int(time.time())
    expiry = now + exp_days * 24 * 60 * 60
    return jwt.encode(
        {
            "email": jwt_param.email,
            "firstName": jwt_param.firstName,
            "domain": jwt_param.domain,
            "aud": audience,
            "exp": expiry,
            "iss": issuer,
            "iat": now,
            "nbf": now,
        },
        signing_key.to_pem(),
        algorithm=algorithm,
    )


def create_empty_jwt(
    signing_key: SigningKey, audience: str, issuer: str, algorithm=DEFAULT_ALGORITHM
) -> str:

    now = int(time.time())
    return jwt.encode(
        {
            "aud": audience,
            "exp": now,
            "iss": issuer,
            "iat": now,
            "nbf": now,
        },
        signing_key.to_pem(),
        algorithm=algorithm,
    )


def decode_jwt(
    jwt_string: str,
    verifying_key: VerifyingKey,
    audience: str,
    algorithm=DEFAULT_ALGORITHM,
):
    return jwt.decode(
        jwt_string,
        verifying_key.to_pem(),
        algorithms=[algorithm],
        audience=audience,
    )


def is_valid_jwt(
    jwt_string: str,
    verifying_key: VerifyingKey,
    audience: str,
    algorithm=DEFAULT_ALGORITHM,
):
    try:
        decoded = decode_jwt(jwt_string, verifying_key, audience, algorithm)
        if decoded:
            return True
    except Exception as _ex:
        return False


def get_user_email(
    jwt_string: str,
    verifying_key: VerifyingKey,
    audience: str,
    algorithm=DEFAULT_ALGORITHM,
):
    decoded = decode_jwt(jwt_string, verifying_key, audience, algorithm)
    if decoded:
        return decoded.get("email")
    return None


def who_am_i(
    jwt_string: str,
    verifying_key: VerifyingKey,
    audience: str,
    algorithm=DEFAULT_ALGORITHM,
):
    result = decode_jwt(jwt_string, verifying_key, audience, algorithm)
    if result:
        jwt_param = JwtParam(
            email=result.get("email"),
            firstName=result.get("firstName"),
            domain=result.get("domain"),
        )
        if jwt_param.email and jwt_param.firstName and jwt_param.domain:
            return jwt_param
        else:
            raise Exception(f"JWT token is missing mandatory field(s) {jwt_param}")
    else:
        raise Exception("Invalid JWT token")
