from typing import List
from fastapi import FastAPI, Response, status
from rituallog.core import get_rituals_from_db
from rituallog.serializers import RitualOut, RitualIn
from rituallog.database import get_session
from rituallog.models import Ritual

api = FastAPI(title='Rituallog')


@api.get('/rituals/', response_model=List[RitualOut])
async def list_rituals():
    """Lists rituals from the database"""
    rituals = get_rituals_from_db()
    return rituals

@api.post('/rituals/', response_model=RitualOut)
async def add_ritual(ritual_in: RitualIn, response: Response):

    ritual = Ritual(**ritual_in.dict())

    with get_session() as session:
        session.add(ritual)
        session.commit()
        session.refresh(ritual)

    response.status_code = status.HTTP_201_CREATED
    return ritual
