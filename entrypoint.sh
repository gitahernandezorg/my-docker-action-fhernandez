#!/bin/sh -l

echo "Hello $1"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT
echo "API TOKEN: ${GITHUB_TOKEN}"
