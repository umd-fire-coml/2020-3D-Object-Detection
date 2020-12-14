#!/bin/sh

cd "${0%/*}"
cd ../checker

diff data-checker--file-output.txt  data-checker--file-output-MASTER.txt

echo DONE!