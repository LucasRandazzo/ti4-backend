import os
from pydantic_settings import BaseSettings

def get_env_filename():
    # Define um arquivo padrão para ambiente local
    return os.environ.get("ENV_FILE", ".env.local")

class EnvironmentSettings(BaseSettings):
    APP_NAME: str
    API_VERSION: str
    ASYNC_DATABASE_URL: str
    DEBUG_MODE: bool
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_EXP_DELTA_SECONDS: int

    class Config:
        env_file = get_env_filename()

def get_database_url(env: EnvironmentSettings) -> str:
    # Apenas retorna a DATABASE_URL já existente
    return env.ASYNC_DATABASE_URL

def get_environment_variables():
    env = EnvironmentSettings()
    return env
