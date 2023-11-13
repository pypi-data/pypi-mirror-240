"""
The main application.
"""

import logging
import sys

from consultant import __version__
from consultant.args import parse_cli_args
from consultant.config import Config
from consultant.logger import Logger


def app():
    """
    Main application logic.

    Raises:
        KeyboardInterrupt: User tried to kill the process.
    """
    try:
        config = Config()
        args = parse_cli_args()

        # Configure logger
        logger = Logger()
        if args.verbose:
            logger.setLevel(logging.INFO)
        else:
            logger.setLevel(logging.ERROR)

        # Show the version and exit
        if args.version:
            print(__version__)
            sys.exit(0)

        logger.info("This is an info log")
        logger.debug("This is a debug log")
        logger.warning("This is a warning log")
        logger.error("This is an error log")
        logger.critical("This is a critial log")

        try:
            config.read()
        except NotImplementedError:
            logger.error("config.read() is not implemented")

        print("Hello, world!")

    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(1)


if __name__ == "__main__":
    app()
