from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import artifactory, items, rqm

app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://10.161.204.45:8080",
    "http://10.161.230.149:8080",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(artifactory.router)
app.include_router(items.router)
app.include_router(rqm.router)


@app.get("/", status_code=200)
async def root():
    return {"msg": "helloworld"}
