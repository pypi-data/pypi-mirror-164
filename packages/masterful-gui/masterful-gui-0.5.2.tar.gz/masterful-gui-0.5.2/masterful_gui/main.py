"""Masterful GUI app main module.

This module is the main entry point for the app. Should be kept as simple
as possible, it defines the global flags for the app and runs it.
"""

import sys

from absl import app
from absl import flags

import masterful_gui.program as program

# The default port the app runs on.
_DEFAULT_PORT = 7007

# The name assigned to the server instance.
_SERVER_NAME = "Masterful GUI"

# TODO(ray): Add dynamic support across the app for using a variable port value.
# This includes CORS configurations as well as media storage URL generation.
# For now we are keeping this flag disabled untill we implement this support
# to avoid having the app break if users select a different port than the
# default one.
# flags.DEFINE_integer('port', _DEFAULT_PORT, 'The port for running the server')


def run_main():
  """The main function that runs the app."""
  visualize = program.Visualize(_SERVER_NAME)

  try:
    app.run(visualize.main)
  except Exception as e:
    print(f'Running Masterful GUI failed: {str(e)}')
    sys.exit(1)


if __name__ == '__main__':
  run_main()