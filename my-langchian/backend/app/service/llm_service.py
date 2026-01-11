from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ..config import config

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL_ID,
            api_key=config.LLM_API_KEY,
            base_url=config.LLM_BASE_URL,
            temperature=0.7,
        )
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("user", "{input}")
        ])
        self.output_parser = StrOutputParser()
        self.chain = self.prompt_template | self.llm | self.output_parser
    
    def call_model(self, input_text: str, temperature: float = 0.7, max_tokens: int = 1024) -> str:
        """Call the local LLM model with the given input text and parameters."""
        try:
            # Create a new chain with custom parameters
            custom_llm = ChatOpenAI(
                model=config.LLM_MODEL_ID,
                api_key=config.LLM_API_KEY,
                base_url=config.LLM_BASE_URL,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            custom_chain = self.prompt_template | custom_llm | self.output_parser
            response = custom_chain.invoke({"input": input_text})
            return response
        except Exception as e:
            raise Exception(f"LLM call failed: {str(e)}")

# Create a global instance
llm_service = LLMService()
