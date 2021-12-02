#!/bin/bash

# A script to create folder structure for every new day

if [[ $# == 0 ]]
then
  echo "Enter Day no. as argument"
else
  dir="day$@"
  problem="./$dir/problem.md"
  input="./$dir/input.txt"
  part1="./$dir/part1.py"
  part2="./$dir/part2.py"

  if [[ -d $dir ]]
  then
    echo "the folder for day $@ already exists"
    exit 1
  else
    mkdir $dir
    touch $problem $input $part1 $part2
  fi

  vi $part1
fi
