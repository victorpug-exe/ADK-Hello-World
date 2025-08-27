from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="Responder dúvidas de IA",
    instruction="""Você é professor especializado em Inteligência Artificial (IA).
    Preciso da sua ajuda para responder dúvidas sobre IA.""",
    description="""Responda à consulta usando a pesquisa do Google""",
    tools=[google_search],
)

root_agent = agent