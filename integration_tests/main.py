from fastapi import FastAPI
from integration_tests.auth import router as router_login
from integration_tests.crud_base import router as router_crud


app = FastAPI()

app.include_router(router_login)
app.include_router(router_crud)
