#!/bin/bash

# A script to create folder structure for every new day

fetch_input() {
  echo "Fetching inputs"
  http --ignore-stdin --timeout=5 --session=../session.json\
    "https://adventofcode.com/2021/day/$1/input" > $2
}

if [[ $# != 1 ]]
then
  echo "Enter day no. as argument"
  exit 1
fi

day=$@
day=${day#0}  # making 01 into 1
dir="$(printf 'day%02d' $day)"  # 1 => day01; 25 => day25

if [[ -d $dir ]]
then
  echo "the folder for day $day already exists"
  exit 1
fi

input="./input.txt"
part1="./part1.py"
part2="./part2.py"

mkdir $dir
cd $dir
touch $input $part1 $part2
fetch_input $day $input
vi $part1
