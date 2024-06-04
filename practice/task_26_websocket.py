from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connected_clients = []

@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text: {data}")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

@app.get("/broadcast")
async def broadcast_message(message: str):
    for client in connected_clients:
        await client.send_text(f"Broadcast message: {message}")
