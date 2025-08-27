import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

#Tool
def get_weather(city: str) -> dict:
    if city.lower() == "são paulo":
        return {
            "status": "success",
            "report": (
                f"O clima em '{city}' é ensolarado com uma temperatura de 25 graus Celsius"
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Informações meteorológicas para '{city}' não estão disponíveis.",
        }

#Tool
def get_current_time(city: str) -> dict:
    if city.lower() == "são paulo":
        tz_identifier = "America/Sao_Paulo"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Desculpe, não tenho informações de fuso horário para {city}."
            ),
        }
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'A hora atual em {city} é {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

root_agent = Agent(
    name="Agente do Tempo e Hora",
    model="gemini-2.0-flash",
    description=(
        "Agente para responder perguntas sobre o clima e o tempo de São Paulo."
    ),
    instruction=(
        "Você é um agente para ajudar responder informações sobre o clima (weather) e tempo (current_time) de São Paulo."
    ),
    tools=[get_weather, get_current_time],
)