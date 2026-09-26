from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "EduGenie"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.8-flash"
    local_explainer_enabled: bool = True
    local_explainer_model: str = ""
    max_input_chars: int = 20000
    request_timeout_seconds: int = 90

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()