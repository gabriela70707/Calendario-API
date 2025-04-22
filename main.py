from fastapi import FastAPI,status,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Event



app = FastAPI()
# Configuração do CORS
origins = [
    "http://localhost:5173"  # URL do front-end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite apenas esta origem
    allow_credentials=True,  # Permite o envio de cookies (se necessário)
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)



events = {
    1:{
        "title":"Copa BISB",
        "description": "Vai ser incrivel demais",
        "categoria": "BISB",
        "start_date":"2025-04-20",
        "end_date":"2025-04-20"
    },

    2:{
        "title":"resende sai do exercito",
        "start_date":"2025-04-20",
        "end_date":"2025-04-20"
    },
    3:{
        "title":"resende sai do exercito",
        "start_date":"2025-04-20",
        "end_date":"2025-04-20"
    },
    4:{
        "title":"resende sai do exercito",
        "start_date":"2025-04-20",
        "end_date":"2025-04-20"
    },
}

@app.get("/")
async def get_events():
    return {"msg":"A API ESTA FUNCIONADO ACESSE A DOCUMENTAÇÃO EM http://127.0.0.1:8000/docs"}

@app.get("/eventos")
async def get_events():
    return events

@app.post("/eventos")
async def add_events(evento:Event):
    novo_id = max(events.keys(), default=0) + 1
    evento.id = novo_id
    events[novo_id] = evento.dict()
    return {"message":f"Evento adicionado com sucesso", **evento.dict()}

@app.delete("/eventos/{id}")
async def delete_event(id:int):
    if(id not in events):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Não foi possivel deletar pois o evento com id:{id} não existe")
    else:
        del events[id]
        return {"message":f"evento com id {id} deletado com sucesso"}
    
@app.patch("/eventos/{id}",status_code=status.HTTP_202_ACCEPTED)
async def edit_event(id:int,evento:Event):
    if id in events:
        evento_existente = events[id]
        editar_evento = evento.dict(exclude_unset=True)
        evento_existente.update(editar_evento)
        return evento_existente
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Não foi possivel editar pois o evento com id:{id} não existe")

if(__name__ == "__main__"):
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8000,log_level='info',reload=True)

    """ OBSERVAÇÕES 
    
    SE VOCE MUDAR QUALQUER COISA NO CODIGO, VOCE TEM QUE RODAR O SERVIDOR NOVAMENTE PARA FUNCIONAR. """