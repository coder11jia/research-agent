import os


DEEPSEEK_API_KEY=os.getenv("DEEPSEEK_API_KEY")
BASE_URL = "https://api.deepseek.com"
MODEL = "deepseek-v4-flash"
MAX_TASKS=5
MAX_STEPS_PER_TASK=5
MAX_RETRIES_PER_TASK = 1