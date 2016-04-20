#!/bin/bash

clear ;

for x in $(ls *.py)
do
	python "$x"
done
