import click

from todotree.Commands.AbstractCommand import AbstractCommand
from todotree.Errors.TodoFileNotFound import TodoFileNotFound


class PrintRaw(AbstractCommand):

    def run(self):
        try:
            with open(self.taskManager.config.paths.todo_file, "r") as f:
                click.echo(f.read())
        except FileNotFoundError:
            TodoFileNotFound("").echo_and_exit(self.config)

