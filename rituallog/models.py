from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, select
from pydantic import validator


class Ritual(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    element: str
    circle: int
    cost: int
    execution: str
    range: str
    target: str
    duration: str
    mat_comp: str = "?"
    resistance: str = ""
    date: datetime = Field(default_factory=datetime.now)

    @validator("circle")
    def validate_circle(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v


# ritual = Ritual(name='Amaldiçoar arma', element='escolha 1', circle=1, cost=1, execution='movimento', range='toque', target='1 arma que cause dano fisico', duration='cena')
