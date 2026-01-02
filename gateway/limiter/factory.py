from gateway.config.mongo_client import (
    get_user_config_by_id,
    get_global_limiter_config
)
from gateway.limiter.token_bucket import TokenBucketLimiter
from gateway.limiter.sliding_window import SlidingWindowLimiter

class RateLimiterFactory:
    @staticmethod
    def create_limiter(user_id=None):
        if user_id:
            config = get_user_config_by_id(user_id)
        else:
            config = get_global_limiter_config()

        if not config:
            raise ValueError("Rate limiter config not found")

        if config["type"] == "token_bucket":
            return TokenBucketLimiter(
                capacity=config["capacity"],
                refill_rate=config["refill_rate"]
            )

        if config["type"] == "sliding_window":
            return SlidingWindowLimiter(
                max_requests=config["max_requests"],
                window_size=config["window_size"]
            )

        raise ValueError("Unknown rate limiter type")
