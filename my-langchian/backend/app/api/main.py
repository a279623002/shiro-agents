from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from app.config import config
from app.models.schemas import LLMRequest, LLMResponse
from app.service.llm_service import llm_service
from app.api.routes.map import router as map_routes



app = FastAPI(title="LangChain Local LLM API", description="API for calling local LLM model using LangChain")


app.include_router(map_routes, prefix="/api")

@app.post("/api/llm", response_model=LLMResponse)
async def call_llm(request: LLMRequest):
    """Call the local LLM model with the provided input text."""
    try:
        response = llm_service.call_model(
            request.input_text,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        return LLMResponse(
            response=response,
            model=config.LLM_MODEL_ID
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Root endpoint for health check."""
    return {"message": "LangChain Local LLM API is running"}

@app.get("/docs")
async def redirect_to_docs():
    """Redirect to Swagger UI documentation."""
    return RedirectResponse(url="/docs")
