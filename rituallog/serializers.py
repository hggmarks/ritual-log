from datetime import datetime
from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class RitualOut(BaseModel):
    id: int
    name: str
    element: str
    circle: int
    cost: int
    execution: str
    range: str
    target: str
    duration: str
    mat_comp: str = '?'
    resistance: str = ''
    date: datetime


class RitualIn(BaseModel):
    name: str
    element: str
    circle: int
    cost: int
    execution: str
    range: str
    target: str
    duration: str
    mat_comp: str = '?'
    resistance: str = ''

    @validator('circle', 'cost')
    def validate_circle_cost(cls, v, field):
        if v < 1 or v > 10:
            raise HTTPException(
                detail=f'{field.name} must be between 1 and 10',
                status_code=status.HTTP_400_BAD_REQUEST
                    )
        return v
        

