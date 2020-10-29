#!/bin/bash
>&2 echo 'Assumes imagemagick is in stalled. Pipe to the shell'
perl -e 'use Cwd qw(cwd); $d = cwd(); $d =~ s/.*(Week_.).*/$1/; print(qq(convert 2020*png $d.pdf\n));'
