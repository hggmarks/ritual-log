from rituallog.core import get_rituals_from_db, add_ritual_to_db


def test_add_ritual_to_db():
    assert add_ritual_to_db(
            name='Imagem Projetada',
            element='energia / conhecimento',
            circle=1,
            cost=1,
            execution='ação padrão',
            range='Pessoal',
            target='Voce',
            duration='Cena',
            mat_comp='Um espelho quebrado',
            )

def test_get_ritual_from_db():
    results = get_rituals_from_db()
    assert len(results) > 0
