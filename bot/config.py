from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMINS: str
    ASSISTANTS: str 
    SUPER_USERS: str 
    POSTGRES_CONTAINE_NAME: str 
    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_DB: str


    class Config:
        env_file = ".env"

config = Settings()