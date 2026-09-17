from openai import OpenAI
from config import (
    DEEPSEEK_API_KEY,
    BASE_URL,
)
if not DEEPSEEK_API_KEY:
    raise   RuntimeError(
        "没有找到DEEPSEEK_API_KEY"
    )
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=BASE_URL,
)