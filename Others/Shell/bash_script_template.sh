#!/bin/bash

set -e
set -u
set -o pipefail

if [ "$#" -lt 3 ] # are there less than 3 arguments?
then
  echo "error: too few arguments, you provided $#, 3 required"
  echo "usage: script.sh arg1 arg2 arg3"
  exit 1
fi

echo \$0 shows the name of this script: $0
echo \$1 is the first argument: $1
echo \$2 is the second argument: $2
echo etc...

string_a="Hello"
string_b="World"

echo $string_a $string_b
