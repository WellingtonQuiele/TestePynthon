import asyncio # Importa o asyncio para operações assíncronas
import websockets # Protocolo websocket



# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Função que executada para cada conexão
async def handle_connection(websocket, path):
    print("Conexão estabelecida com sucesso")

    try:
        async for message in websocket:
            if message.startswith("fatorial: "):  # Verifica se a mensagem inicia com fatorial : não esquecer de colocar espaço após o :
                number = int(message.split(":")[1])
                result = calcular_fatorial(number)
                await websocket.send(f"O fatorial de {number} é {result}")
            else:
                await websocket.send("Comando não reconhecido")

    except websockets.exceptions.ConnectionClosedOK:
        print("Conexão fechada")

# Função principal que inicia o servidor 
async def servidor():
    server = websockets.serve(handle_connection, "localhost", 8765)# Cria o servidor WebSocket
    print("Servidor iniciado")

    await server
    await asyncio.Event().wait()

# Inicia o servidor com asyncio para ter operações assincronas 
asyncio.run(servidor())