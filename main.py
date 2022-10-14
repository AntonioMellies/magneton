import uvicorn
from fastapi import FastAPI
from routers import company

app = FastAPI()

app.include_router(company.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)
