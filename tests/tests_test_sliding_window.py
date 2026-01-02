import time
from gateway.limiter.sliding_window import SlidingWindowLimiter

def test_sliding_window():
    limiter = SlidingWindowLimiter(max_requests=2, window_size=2)
    user = "user_1"
    assert limiter.allow_request(user) == True
    assert limiter.allow_request(user) == True
    assert limiter.allow_request(user) == False
    time.sleep(2.1)
    assert limiter.allow_request(user) == True

if __name__ == "__main__":
    test_sliding_window()
    print("SlidingWindowLimiter test passed ✅")
