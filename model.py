from typing import Optional,Literal
from pydantic import BaseModel
from datetime import date 

class Event(BaseModel):
    id: Optional[int] = None
    description: Optional[str] = None
    categoria: Optional[Literal["Bosch", "BISB", "Lazer"]] = None
    title: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

