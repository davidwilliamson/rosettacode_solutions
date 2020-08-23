#! /usr/bin/env bash

# Runs all the scripts in the solutions directory

# python files we should not run. Whitespace delimited.
skips='__init__.py'

failed=''
fail_count=0

for f in $(find ./solutions -name '*.py'|sort); do
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
    result=$?
    if [[ "$result" != '0' ]]; then
        failed="$failed"$'\n'$script
        fail_count=$(( fail_count + 1 ))
    fi
done

if [[ -n "$failed" ]]; then
    echo $'\n'"=============== Problems ==============="
    echo "$fail_count scripts failed:${failed}"
else
    echo $'\n'"All scripts ran OK"
fi
