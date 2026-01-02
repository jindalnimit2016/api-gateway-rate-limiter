# main.py
from fastapi import FastAPI, Header, Request
from gateway.router.gateway_router import GatewayRouter
from gateway.config.config_manager import ConfigManager
from fastapi.responses import JSONResponse
from gateway.exceptions import UnauthorizedException, RateLimitExceededException


# FAANG-ready: centralized config
config = {
    "limiter_config": {
        "type": "token_bucket",
        "capacity": 10,
        "refill_rate": 2
    }
}
ConfigManager(config)

app = FastAPI()
gateway = GatewayRouter()

@app.get("/api")
def access_api(x_api_key: str = Header(...)):
    return gateway.handle_request(x_api_key)

@app.exception_handler(UnauthorizedException)
async def unauthorized_handler(request: Request, exc: UnauthorizedException):
    return JSONResponse(
        status_code=401,
        content={"error": "Unauthorized"}
    )

@app.exception_handler(RateLimitExceededException)
async def rate_limit_handler(request: Request, exc: RateLimitExceededException):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded"}
    )
