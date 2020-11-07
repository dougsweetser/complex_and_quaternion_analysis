#!/usr/bin/env python
"""
Aid to merging pdfs using ghostscript command.
Take from https://askubuntu.com/questions/2799/how-to-merge-several-pdf-files

Only prints the command needed to STDOUT. Pipe to a shell to "make it so."

usage: pdf_merge.py [-o OUTPUT] <files>...

optional arguments:
  -o OUTPUT --output OUTPUT   output file name [default: merged.pdf]
"""

from docopt import docopt

if __name__ == "__main__":
    ARGS = docopt(__doc__)

output = ARGS["--output"]
files = " ".join(ARGS["<files>"])

command = "gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dAutoRotatePages=/None "

command += f"-sOutputFile={output} {files}"

print(command)
