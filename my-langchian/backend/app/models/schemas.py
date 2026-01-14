from pydantic import BaseModel
from typing import Optional

# LLM Request Schema
class LLMRequest(BaseModel):
    input_text: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1024

# LLM Response Schema
class LLMResponse(BaseModel):
    response: str
    model: str
    processing_time: Optional[float] = None

# Agent Request Schema
class AgentRequest(BaseModel):
    task: str
    context: Optional[dict] = None

# Agent Response Schema
class AgentResponse(BaseModel):
    result: str
    agent: str
    steps: Optional[list[dict]] = None
