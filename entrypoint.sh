#!/bin/sh -l

echo "Helloooo $1"
echo "github token $2"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT
