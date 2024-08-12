from fastapi import FastAPI
from api import app

#app = FastAPI()

#app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5050)
