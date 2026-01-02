import time
from gateway.limiter.token_bucket import TokenBucketLimiter

def test_token_bucket():
    limiter = TokenBucketLimiter(capacity=2, refill_rate=1)
    user = "user_1"
    assert limiter.allow_request(user) == True
    assert limiter.allow_request(user) == True
    assert limiter.allow_request(user) == False
    time.sleep(1.1)
    assert limiter.allow_request(user) == True

if __name__ == "__main__":
    test_token_bucket()
    print("TokenBucketLimiter test passed ✅")
