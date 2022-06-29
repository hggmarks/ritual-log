from typer.testing import CliRunner
from rituallog.cli import main

runner = CliRunner()

def test_add_ritual():
    result = runner.invoke(main, ['add', 'Cicatrização', 'Morte', '1', '1', 'ação padrão', 'toque', 'Um personagem', 'Instantâneo']
    )
    assert result.exit_code == 0
    assert 'Ritual added' in result.stdout
