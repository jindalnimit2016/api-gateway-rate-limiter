from gateway.auth.auth_service import AuthService
from gateway.limiter.factory import RateLimiterFactory
from gateway.metrics.metrics import MetricsCollector
from gateway.exceptions import RateLimitExceededException

class GatewayRouter:
    def __init__(self):
        self.auth = AuthService()
        self.user_limiters = {}  # user_id -> limiter
        self.metrics = MetricsCollector()

    def handle_request(self, api_key: str):
        user_id = self.auth.authenticate(api_key)

        # create limiter per user dynamically
        if user_id not in self.user_limiters:
            self.user_limiters[user_id] = RateLimiterFactory.create_limiter(user_id)

        limiter = self.user_limiters[user_id]

        if limiter.allow_request(user_id):
            self.metrics.record_allowed()
            return {"status": "success"}

        # IMPORTANT CHANGE
        self.metrics.record_blocked()
        raise RateLimitExceededException("Too many requests")
