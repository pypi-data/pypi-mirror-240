import sys
from argparse import ArgumentError, ArgumentParser
from dataclasses import dataclass
import os
from pathlib import Path

from wizlib.class_family import ClassFamily
from wizlib.super_wrapper import SuperWrapper


RED = '\033[91m'
RESET = '\033[0m'


class CommandHandler:
    """Handle commands from a ClassFamily, with special knowledge of shell
    arguments."""

    def __init__(self, atriarch):
        """Pass in the command base class, the atriarch of a
        classfamily that meeting the CommandHandler spec"""
        self.parser = ArgumentParser(prog=atriarch.appname,
                                     exit_on_error=False)
        atriarch.add_app_args(self.parser)
        subparsers = self.parser.add_subparsers(dest='command')
        for command in atriarch.family_members('name'):
            key = command.get_member_attr('key')
            aliases = [key] if key else []
            subparser = subparsers.add_parser(command.name, aliases=aliases)
            command.add_args(subparser)
        self.atriarch = atriarch

    def get_command(self, args=None):
        args = args if args else [self.atriarch.default]
        values = vars(self.parser.parse_args(args))
        command = values.pop('command')
        command_class = self.atriarch.family_member('name', command)
        if not command_class:
            raise Exception(f"Unknown command {command}")
        return command_class(**values)

    def handle(self, args=None):
        command = self.get_command(args)
        if command:
            result = command.execute()
            return result, command.status
        else:
            return None, None

    @classmethod
    def shell(cls, atriarch):
        """Call this from a shell/main entrypoint"""
        try:
            result, status = cls(atriarch).handle(sys.argv[1:])
            if result:
                print(result)
            if status:
                print(status, file=sys.stderr)
        except Exception as error:
            if os.getenv('DEBUG'):
                raise error
            else:
                print(f"\n{RED}{type(error).__name__}: " +
                      f"{error}{RESET}\n", file=sys.stderr)


@dataclass
class Command(ClassFamily, SuperWrapper):
    """Define all the args you want, but stdin always works."""

    status = ''
    input: str = ''

    @classmethod
    def add_app_args(self, parser):
        """Add pre-subcommand arguments via argparse by optionally overriding -
        only works in the atricarch. Default is an optional 'input' argument to
        take the place of stdin in testing"""
        parser.add_argument('--input', '-i', default='')
        pass

    @classmethod
    def add_args(self, parser):
        """Add arguments to the command's parser - override this.
        Add global arguments in the base class. Not wrapped."""

    def handle_args(self):
        """Clean up args, calculate any, ask through UI, etc. - override
        this. For input, default is to grab stdin in non-tty cases."""
        if self.input:
            self.input = Path(self.input).read_text()
        elif not sys.stdin.isatty():
            self.input = sys.stdin.read()

    def execute(self, method, *args, **kwargs):
        """Actually perform the command - override and wrap this via
        SuperWrapper"""
        self.handle_args()
        result = method(self, *args, **kwargs)
        return result
