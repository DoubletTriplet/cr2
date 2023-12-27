import logging
from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics
from tsc.routes import words
from tsc.utils.config import SETTINGS

logging.basicConfig(
    level=logging.INFO,
)

app = FastAPI(
    debug=SETTINGS.DEBUG,
    title="TSC - Translation Service Challenge",
    summary="API to translate words and find synonyms"
)

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

routers = [
    words.router
]


for router in routers:
    app.include_router(router)

