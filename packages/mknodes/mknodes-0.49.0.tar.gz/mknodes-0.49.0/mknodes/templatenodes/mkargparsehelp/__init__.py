from __future__ import annotations

import argparse

from mknodes.basenodes import mkcontainer, mkheader, mktext
from mknodes.utils import log


logger = log.get_logger(__name__)


class MkArgParseHelp(mkcontainer.MkContainer):
    """Node to describe an argparse parser."""

    ICON = "material/bash"
    STATUS = "new"
    VIRTUAL_CHILDREN = True

    def __init__(self, parser: argparse.ArgumentParser, **kwargs):
        self.parser = parser
        super().__init__(**kwargs)

    @property
    def items(self):
        # ArgumentParser.format_usage()
        # ArgumentParser.format_help()
        items = [
            mkheader.MkHeader(self.parser.prog),
            mktext.MkText(self.parser.description),
            mktext.MkText("Options:"),
        ]
        lines = []
        for action in self.parser._actions:
            opts = [f"`{opt}`" for opt in action.option_strings]
            if not opts:
                continue
            line = "- " + ",".join(opts)
            if action.metavar:
                line += f" `{action.metavar}`"
            line += f": {action.help}".replace(" Default: %(default)s", "")
            if action.default and action.default != argparse.SUPPRESS:
                line += f"(default: `{action.default}`)"
            lines.append(line)
        items.append(mktext.MkText("\n".join(lines)))
        for i in items:
            i.parent = self
        return items

    @items.setter
    def items(self, value):
        pass

    @classmethod
    def create_example_page(cls, page):
        from git_changelog import cli

        import mknodes as mk

        parser = cli.get_parser()

        node = MkArgParseHelp(parser)
        page += mk.MkReprRawRendered(node)


if __name__ == "__main__":
    from git_changelog import cli

    parser = cli.get_parser()

    text = MkArgParseHelp(parser)
    print(text)
