from fastapi import FastAPI, Depends
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# alembic zorgt nu voor het maken van de tabellen 
# models.Base.metadata.create_all(bind=engine)

appo = FastAPI()

origins = ["*"]

appo.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

appo.include_router(post.router)
appo.include_router(user.router)
appo.include_router(auth.router)
appo.include_router(vote.router)

@appo.get("/")
async def root():
    return {"message": "Hello World!!!!!!!!!!!"}


