from typing import Tuple

import click

from todotree.Commands.AbstractCommand import AbstractCommand
from todotree.Errors.DoneFileNotFound import DoneFileNotFound
from todotree.Task.DoneTask import DoneTask


class AddX(AbstractCommand):

    def run(self, task: Tuple):
        try:
            done = DoneTask.task_to_done(" ".join(map(str, task)))
            with self.config.paths.done_file.open("a") as f:
                f.write(done)
            click.echo(done)
        except FileNotFoundError:
            DoneFileNotFound("").echo_and_exit(self.config)
