import argparse
from api_requests import chat_completo

# Buffer para almacenar las consultas y respuestas anteriores
conversation_buffer = []

def consulta_query():
    while True:
        query = input("Ingrese su consulta (pulse 'cursor Up' para recuperar la última consulta): ")
        if query.strip():
            return query
        print("La consulta está vacía. Por favor ingrese una consulta con texto.")

def procesar_query(query):
    try:
        print(f"You: {query}")
        completo = chat_completo(query)
        response = completo['choices'][0]['message']['content']
        print("Respuesta de chatGPT:")
        print(f"chatGPT: {response}")
        return response
    except KeyError as e:
        print("Ocurrió un error al procesar la consulta:", e)
    except Exception as e:
        print("Ocurrió un error al procesar la consulta:", e)

def main():
    parser = argparse.ArgumentParser(description='Procesar consultas con chatGPT')
    parser.add_argument('--convers', action='store_true', help='Modo de conversación')
    args = parser.parse_args()

    if not args.convers:
        print("Modo de conversación desactivado. Ejecute python main.py --convers para habilitar este modo.")
        return

    while True:
        try:
            query = consulta_query()
            response = procesar_query(query)
            choice = input("¿Desea realizar otra consulta? (s/n): ").strip().lower()
            if choice != 's':
                break
        except Exception as e:
            print("Ocurrió un error en la ejecución del programa:", e)

if __name__ == "__main__":
    main()




