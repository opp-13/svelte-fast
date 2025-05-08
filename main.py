from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from domain.answer import answer_router
from domain.question import question_router
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)

@app.get("/health")
async def health_check():
    return PlainTextResponse("건강합니다", status_code=200)

@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    response = JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
