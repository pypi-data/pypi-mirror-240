"""
Module for command line argument operations.
"""

import argparse


def parse_cli_args():
    """
    Parses the command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    # Create a parser
    parser = argparse.ArgumentParser(
        description="Command line interface frontent for AI assistance"
    )

    # Define optional arguments
    parser.add_argument("--version", action="store_true", help="Get version.")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose mode."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    return args
