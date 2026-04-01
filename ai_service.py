import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "google/gemini-2.0-flash-001"

def create_simple_tasks(description):

    if not os.getenv("OPENROUTER_API_KEY"):
        return ["Error: API key no encontrada. Por favor, configura la variable OPENROUTER_API_KEY en el archivo .env"]
    try:
        client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url=OPENROUTER_BASE_URL,
        )

        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
        
        Tarea: {description}

        Formato de la respuesta:
        - Subtarea 1
        - Subtarea 2
        - Subtarea 3
        - etc.

        responde solo con la lista de subtareas, una por línea, empezando cada una por un guión."""

        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No se pudieron generar subtareas. Por favor, intenta con una descripción de tarea diferente."]

    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
            return ["Error: Límite de peticiones alcanzado. Espera unos minutos o revisa tu crédito en https://openrouter.ai"]
        return [f"Error: {type(e).__name__}: {e}"]
   