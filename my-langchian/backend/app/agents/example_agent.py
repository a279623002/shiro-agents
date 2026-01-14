from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_openai import ChatOpenAI
from ..config import config

class ExampleAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL_ID,
            api_key=config.LLM_API_KEY,
            base_url=config.LLM_BASE_URL,
            temperature=0.5,
        )
        # Load basic tools
        self.tools = load_tools(["llm-math"], llm=self.llm)
        
        # Initialize agent
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    
    def run(self, task: str) -> str:
        """Run the agent with the given task."""
        try:
            result = self.agent.run(task)
            return result
        except Exception as e:
            raise Exception(f"Agent execution failed: {str(e)}")

# Create a global instance
example_agent = ExampleAgent()
