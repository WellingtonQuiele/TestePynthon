import asyncio # Importa o asyncio para operações assíncronas
import websockets# Protocolo websocket


async def cliente():
    # Estabelece a conexão  com o servidor local na porta 8765
    async with websockets.connect("ws://localhost:8765/") as websocket:
        # Solicita ao cliente para digitar uma mensagem
        message = input("Digite uma mensagem: ")
        await websocket.send(message)
        print(f"Mensagem enviada: {message}")

        # Resposta do servidor 
        response = await websocket.recv()
        print(f"Mensagem recebida: {response}")

# Executa a função main
asyncio.run(cliente())