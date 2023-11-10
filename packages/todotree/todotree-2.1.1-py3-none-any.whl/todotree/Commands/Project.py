import click

from todotree.Commands.AbstractCommand import AbstractCommand
from todotree.Errors.TodoFileNotFound import TodoFileNotFound
from todotree.Main import taskManager


class Project(AbstractCommand):

    def run(self):
        try:
            self.taskManager.import_tasks()
        except TodoFileNotFound as e:
            e.echo_and_exit(self.config)
        # Print due tree.
        click.echo(taskManager.print_project_tree())
