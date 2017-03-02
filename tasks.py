"""Tarefas da applicação tasks."""

import invoke


@invoke.task(default=True)
def runserver(ctx, settings='development'):
    """Executa o servidor de desenvolvimento."""
    cmd = f'./manage.py runserver --settings=todo.settings.{settings}'
    ctx.run(cmd, pty=True, echo=True)


@invoke.task
def test(ctx, tests='', settings='test'):
    """Testa as aplicações do projeto (com exceção dos testes funcionais)."""
    cmd = f'coverage run ./manage.py test {tests} --settings=todo.settings.{settings}'
    ctx.run(cmd, echo=True, pty=True)
    cmd = 'coverage report'
    ctx.run(cmd, echo=True, pty=True)
