from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from database import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
