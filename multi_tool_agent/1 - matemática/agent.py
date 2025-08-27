from google.adk.agents import LlmAgent

def somar(side_a: float, side_b: float) -> float:
  try:
    side_a_float = float(side_a)
    side_b_float = float(side_b)
    return side_a_float + side_b_float
  except Exception as e:
    return f"Erro de cálculo: {e}"

def subtrair(side_a: float, side_b: float) -> float:
  try:
    side_a_float = float(side_a)
    side_b_float = float(side_b)
    return side_a_float - side_b_float
  except Exception as e:
    return f"Erro de cálculo: {e}"

def dividir(side_a: float, side_b: float) -> float:
  try:
    side_a_float = float(side_a)
    side_b_float = float(side_b)
    if side_b_float == 0:
      return "Erro: Divisão por zero não é permitida."
    return side_a_float / side_b_float
  except Exception as e:
    return f"Erro de cálculo: {e}"

def multiplicar(side_a: float, side_b: float) -> float:
  try:
    side_a_float = float(side_a)
    side_b_float = float(side_b)
    return side_a_float * side_b_float
  except Exception as e:
    return f"Erro de cálculo: {e}"

root_agent: LlmAgent = LlmAgent(
        name="Calculadora",
        model="gemini-2.0-flash",
        description="Ferramenta para ajudar com calculos matemáticos",
        instruction=(
            "Quando o usuário inserir 2 números, ajude-o a calcular o resultado."
            "Indique claramente o resultado ou quaisquer erros encontrados."
        ),
        tools=[somar, subtrair, dividir, multiplicar],
    )
