from typing import List
from sqlmodel.sql.expression import select
from rituallog.database import get_session
from rituallog.models import Ritual


def add_ritual_to_db(
    name: str,
    element: str,
    circle: int,
    cost: int,
    execution: str,
    range: str,
    target: str,
    duration: str,
    mat_comp: str = '?',
    resistance: str = '',
) -> bool:

    with get_session() as session:
        ritual = Ritual(
            name=name,
            element=element,
            circle=circle,
            cost=cost,
            execution=execution,
            range=range,
            target=target,
            duration=duration,
            mat_comp=mat_comp,
            resistance=resistance,
        )
        session.add(ritual)
        session.commit()

    return True


def get_rituals_from_db() -> List[Ritual]:
    with get_session() as session:
        sql = select(Ritual)

        return list(session.exec(sql))
