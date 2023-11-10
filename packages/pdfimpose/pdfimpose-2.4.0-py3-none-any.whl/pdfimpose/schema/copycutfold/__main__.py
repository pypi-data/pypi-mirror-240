# Copyright 2011-2022 Louis Paternault
#
# This file is part of pdfimpose.
#
# Pdfimpose is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pdfimpose is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pdfimpose.  If not, see <https://www.gnu.org/licenses/>.

"""Parse arguments for the schema "copycutfold"."""

import logging
import sys

from ... import UserError, pdf
from .. import ArgumentParser
from ..cards.__main__ import format2signature
from . import __doc__ as DESCRIPTION
from . import impose


def main(argv=None):
    """Main function"""

    parser = ArgumentParser(
        subcommand="copycutfold",
        description=DESCRIPTION,
        options=[
            "omargin",
            "imargin",
            "mark",
            "last",
            "cutsignature",
            "format",
            "bind",
            "creep",
            "group0",
        ],
    )

    try:
        args = parser.parse_args(argv)

        args.files = pdf.Reader(args.files)

        sourcesize = args.files.size
        if args.bind in ("top", "bottom"):
            sourcesize = (2 * sourcesize[1], sourcesize[0])
        else:
            sourcesize = (2 * sourcesize[0], sourcesize[1])
        format2signature(sourcesize, args)

        return impose(**vars(args))

    except UserError as uerror:
        logging.error(uerror)
        sys.exit(1)


if __name__ == "__main__":
    main()
