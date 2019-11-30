#!/usr/bin/env bash

# Print strings that can be used as Python tuples, where the first item in the
# tuple is the hex encoding of a string, and the second is the base64 encoding
# of the same string.

STRINGS=( \
"I'm killing your brain like a poisonous mushroom" \
"Deadly, when I hear a dope melody" \
"Anything less than the best is a felony" )
for s in "${STRINGS[@]}"
do
    hex_string="$( echo -n ${s} | xxd -p -c 256 )"
    base64_string="$( echo ${hex_string} | xxd -r -p | base64 )"
    echo "( \"${hex_string}\","
    echo   "\"${base64_string}\" ),"
done
