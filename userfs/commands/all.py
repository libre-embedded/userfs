# =====================================
# generator=datazen
# version=3.2.3
# hash=4a20da8fec7342f05a3715fb1cd2b996
# =====================================

"""
A module aggregating package commands.
"""

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from userfs.commands.build import add_build_cmd
from userfs.commands.custom import add_custom_cmd
from userfs.commands.fetch import add_fetch_cmd


def commands() -> list[tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "build",
            "attempt to build a software project from its sources",
            add_build_cmd,
        ),
        (
            "custom",
            "perform a custom interaction, sourced from external hooks",
            add_custom_cmd,
        ),
        (
            "fetch",
            "attempt to obtain some software from the internet",
            add_fetch_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
