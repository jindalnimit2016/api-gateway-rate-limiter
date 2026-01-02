# gateway/limiter/sliding_window.py
import time
import threading
from collections import deque
from gateway.limiter.base import RateLimiter

class SlidingWindowLimiter(RateLimiter):
    def __init__(self, max_requests: int, window_size: int):
        self.max_requests = max_requests
        self.window_size = window_size
        self.user_requests = {}  # user_id -> deque
        self.lock = threading.Lock()

    def allow_request(self, user_id: str) -> bool:
        with self.lock:
            now = time.time()
            if user_id not in self.user_requests:
                self.user_requests[user_id] = deque()
            q = self.user_requests[user_id]
            while q and q[0] <= now - self.window_size:
                q.popleft()
            if len(q) < self.max_requests:
                q.append(now)
                return True
            return False
