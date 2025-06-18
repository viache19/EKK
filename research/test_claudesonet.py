import anthropic

API_KEY=""

client = anthropic.Anthropic(api_key=API_KEY)

prompt = "Cuentame un chiste andalu"

try:
    response = client.messages.create(
        model="claude-3-haiku-20240307",  # Using the most cost-effective model
        max_tokens=300,
        temperature=0.1,
        system="Eres un profesional en contar chiste de comedia. Humor al 100%.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
        
     # Extraer y parsear la respuesta JSON
    response_text = response.content[0].text
        
    print(response)
        
except Exception as e:
    raise Exception(f"Error al analizar el mensaje con Claude: {str(e)}")


