#! /usr/bin/env bash

# Runs all the scripts in the solutions directory

# python files we should not run. Whitespace delimited.
skips='__init__.py'

for f in $(find ./solutions -name *.py); do
    script=$(basename $f )
    skip_this_script=''
    for skip in $skips; do
        if [[ "$script" == "$skip" ]]; then
            skip_this_script='1'
            break
        fi
    done
    if [[ -n "$skip_this_script" ]]; then
        continue
    fi
    echo "--------------- ${script} ----------------------"
    cmd="python $f"
    eval $cmd
done
