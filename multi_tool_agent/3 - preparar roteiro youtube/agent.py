import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.tools import google_search

script_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="script_agent",
    instruction="""Você é professor(a) especializado(a) em Inteligência Artificial e educação.
    Preciso da sua ajuda para gerar roteiros para conteúdo sobre IA no YouTube..""",
    description="Responda à consulta usando a pesquisa do Google",
    tools=[google_search],
    output_key="generated_script",
)

visualizer_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="visualizer_agent",
    instruction="Gere conceitos visuais com base no script fornecido pelo estado['generated_script'].",
    description="Gere conceitos visuais com base no script fornecido",
    output_key="visual_concept",
)

formatter_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="formatter_agent",
    instruction="""Combine o script de state['generated_script'] e os conceitos visuais state['visual_concept']
    em um documento markdown""",  
    description="""Formate o script e os conceitos visuais em um documento markdown""",
    output_key="formatter",
)

code_pipeline_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[script_agent, visualizer_agent, formatter_agent],
    description="""Executa uma sequência de geração de script, desenvolvimento de conceitos visuais 
    e formatação em markdown sobre um roteiro de IA para o Youtube""",
)

root_agent = code_pipeline_agent