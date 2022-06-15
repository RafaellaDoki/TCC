#!/bin/sh

IFS=$'\n'
for input in `find no/ -type f -iname "*.jpg"`; do 
    output=`basename "$input"`
    echo "Convertendo image($input) de dimensões diversas para 512x512..."
    convert $input -resize 512x512 -gravity center -background black -extent 512x512 -crop 512x512+0+0 "no_512/$output" 
    echo "Convertendo image(no_512/$output) para arquivo mat..."
    ./convert_to_mat.py "no_512/$output"
done; 
unset IFS


