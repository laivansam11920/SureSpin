from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    MONGO_URI: str = Field(..., alias="MONGO_URI")
    MONGO_MAIN_DB: str = Field(default="Wheel", alias="MONGO_MAIN_DB")
    LIST_ID_SPECIAL: list[int] = Field(default=[2, 7, 10], alias="LIST_ID_SPECIAL")

    model_config = SettingsConfigDict(populate_by_name=True)


Config = Config()
