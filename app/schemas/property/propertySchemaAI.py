

from pydantic import BaseModel

class SearchPrompt(BaseModel):
    prompt: str