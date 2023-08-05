"""
Welcome to CoPR (Complex Pipeline Runner).

©2022 - Subconscious Compute 'All rights reserved.'
"""

import logging
import os

import typing as T

import bitia.infra.cache
import bitia.common
import bitia.run
import typer

app = typer.Typer()


import bitia.bootstrap

app.add_typer(bitia.bootstrap.app, name="bootstrap")

import bitia.check

app.add_typer(bitia.check.app, name="check")


import bitia.server.main

app.add_typer(bitia.server.main.app_cli, name="server")

# NOTE: typer does not support Union Type yet.
@app.command("run")
def run_user_input(
    user_input: str,
    server: T.Optional[str] = None,
    executor: bitia.common.Executor = bitia.common.Executor.podman,
    interactive: bool = False,
):
    """runs the passed command or file inside a docker container and returns the output

    Parameteres
    -----------
    user_input : str
        It could be a command, a directory or a file.
    server : str, optional
        Gets the server address from the user.
    executor: str, optional
        'bash', 'docker', 'podman'
    interactive: bool, default `False`
        If `True`, run docker command in `interactive` mode. Useful when
        debugging.

    Returns
    -------
    None

    See Also
    --------
    bitia.daemon.daemon

    """
    bitia.run.submit_job(
        user_input, server=server, executor=executor, interactive=interactive
    )


#
# Utilities
#
@app.command("make_available")
@app.command("download")
def make_available(urls_or_file):
    """Make the data available from a given user input.

    Parameters
    ----------
    urls_or_file : str, Path
        urls as csv or a file containing url. One one each line.
    """
    bitia.infra.cache.make_available(urls_or_file)


if __name__ == "__main__":
    app()
