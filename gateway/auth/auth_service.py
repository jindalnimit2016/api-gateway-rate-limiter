from gateway.config.mongo_client import get_user_config
from gateway.exceptions import UnauthorizedException

class AuthService:
    def authenticate(self, api_key: str):
        user = get_user_config(api_key)
        if not user:
            raise UnauthorizedException("Invalid API key")
        return user["user_id"]
