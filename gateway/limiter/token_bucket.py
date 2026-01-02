# gateway/limiter/token_bucket.py
import time
import threading
from gateway.limiter.base import RateLimiter

class TokenBucketLimiter(RateLimiter):
    def __init__(self, capacity: int, refill_rate: int):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.user_buckets = {}  # user_id -> bucket
        self.lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        with self.lock:
            bucket = self.user_buckets.get(user_id, {"tokens": self.capacity, "last": time.time()})
            now = time.time()
            elapsed = now - bucket["last"]
            refill = int(elapsed * self.refill_rate)
            bucket["tokens"] = min(self.capacity, bucket["tokens"] + refill)
            bucket["last"] = now
            if bucket["tokens"] > 0:
                bucket["tokens"] -= 1
                self.user_buckets[user_id] = bucket
                return True
            self.user_buckets[user_id] = bucket
            return False
