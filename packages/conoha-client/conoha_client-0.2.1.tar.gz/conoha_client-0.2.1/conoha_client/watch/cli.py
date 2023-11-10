"""watch cli."""

import click


@click.command("watch", help="VM起動からn時間後に削除する")
def watch_cli() -> None:
    """Watch cli."""
