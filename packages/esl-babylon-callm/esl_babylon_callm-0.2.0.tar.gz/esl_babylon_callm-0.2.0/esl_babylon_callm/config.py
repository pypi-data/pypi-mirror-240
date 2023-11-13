from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

root_folder: Path = Path(__file__).parent.resolve()


class Settings(BaseSettings):
    # App Settings
    app_dir: Path = Field(default=root_folder)
    app_name: str = Field(env="APP_NAME", default="ESL-Babylon-CaLLM")

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return init_settings, dotenv_settings, env_settings, file_secret_settings

    class Config:
        validate_assignment = True
        env_file: Path = root_folder / Path("env.ini")


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    settings.update_values()
    return settings


app_config = get_settings()
