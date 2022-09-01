#!/bin/bash

for i in 10 50 250 1250; do
	echo $i; R --vanilla --silent < tau.r $i; ./tau.py $i;
done
