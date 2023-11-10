import os
import subprocess
from pathlib import Path

from todotree.Config.Config import Config


# Addons https://click.palletsprojects.com/en/8.1.x/commands/#custom-multi-commands

class Addons:

    def __init__(self, config: Config = Config()):
        self.rv: list = []
        """List of programs."""

        self.default_config: Config = config
        """Configuration"""

    def list(self):
        """List the addons detected."""
        self.rv = []
        for filename in Path(self.default_config.paths.addons_folder).iterdir():
            if os.access(filename, os.X_OK):
                # Then the file is executable, add to the list.
                self.rv.append(str(filename.parts[-1]))
        self.rv.sort()
        return self.rv

    def run(self, name):
        """Run the addon with the name `name`."""
        file = Path(self.default_config.paths.addons_folder / name)
        if not file.exists():
            self.default_config.console.error(f"There is no script at {file}")
            exit(1)

        self.default_config.console.verbose(f"Running script at {file}")
        try:
            result = subprocess.run([file, str(self.default_config.paths.todo_file)], capture_output=True, text=True)
        except Exception as e:
            self.default_config.console.error(f"Error while running the addon {name}.")
            self.default_config.console.error(f"The error is {e}")
            raise e
        return result
