#!/bin/bash

# A script to create folder structure for every new day

if [[ $# == 0 ]]
then
  echo "Enter Day no. as argument"
else
  if [[ -d $dir ]]
  then
    echo "the folder for day $@ already exists"
    exit 1
  fi

  dir="day$@"
  problem="./problem.md"
  input="./input.txt"
  part1="./part1.py"
  part2="./part2.py"

  mkdir $dir
  cd $dir
  touch $problem $input $part1 $part2
  vi $part1
fi
