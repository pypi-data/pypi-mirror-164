from __future__ import annotations

import subprocess

from uetools.conf import Command, editor_cmd, uproject

EDITOR_COMMANDS = [
    # "debug {0}"
    "automation list",
    "runtests",
    "runall",
]


class Editor(Command):
    """Runs Editor as is. Experimental do not use"""

    name: str = "editor"

    @staticmethod
    def arguments(subparsers):
        """Adds the arguments for this command to the given parser"""
        ueditor = subparsers.add_parser("editor", help="")
        ueditor.add_argument(
            "project", type=str, help="Project name, example: <project>.uproject"
        )

        ueditor.add_argument(
            "map",
            type=str,
            help="Map to load, example: /Game/Maps/MyMap?game=MyGame&?name=MyPlayerName",
        )
        ueditor.add_argument(
            "-game", type=str, help="Launch the game using uncooked content"
        )
        ueditor.add_argument(
            "-server",
            type=str,
            help="Launch the game as a server using uncooked content",
        )

        # editor_parser.add_argument("run", type=str, help="Command to run", choices=["Launch", "cook"])
        # editor_parser.add_argument("platform", type=str, help="Target platform", choices=get_editor_platforms())
        # editor_parser.add_argument("cmds", type=str, nargs="+", help="Commands to execute", choices=EDITOR_COMMANDS)

    @staticmethod
    def execute(args):
        args = vars(args)
        run_editor(**args)


# pylint: disable=unused-argument
def run_editor(project, cmd=False, **kwargs):
    """Run the editor with the given arguments"""
    subprocess.run(
        [
            editor_cmd(),  # if cmd else editor(),
            uproject(project),
            "-stdout",  # redirect stdout to console
            # "-nullrhi",         # not graphics
            "-unattended",  # avoid user prompts
            "-fileopenlog",  # ?
            "-unversioned",  # ?
            "-UTF8Output",  # ?
            "-CrashForUAT",  # ?
            # "-NoLogTimes",      # Do not print timestamps and frame times
            "-Help",
            # f"-abslog={logpath}", # Path to log file
            # f"-Run={run}",                      # Run a ComandLet
            # f"-TargetPlatform={platform}",       # Target platform for Cooking
            # "-game", map_name,                # Launch game with this map
            # "-sandbox={path_to_cooked_game}", # Launch game using packaged/cooked game
            # "-streaming",                     # CookOnTheFlyStreaming
            # "-cookonthefly "
            # "-buildmachine"
            # -execcmds=""
            # "-Exe="
            # -Messaging -Windowed
            # "-Device="                # GPUs to use -Device=0+1+2+3
        ],
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        check=True,
    )


COMMAND = Editor
