#!/bin/bash
>&2 echo 'Assumes imagemagick is in stalled. Pipe to the shell.'
ls 2020*png | perl -lane '$f = $F[0]; $n = $f; $n =~ s/2020.*part_\d*__//; $n =~ s/.png//; print(qq(convert $f -gravity North -pointsize 30 -fill yellow -annotate 0 "$n" $f));'
