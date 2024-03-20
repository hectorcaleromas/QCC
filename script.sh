#!/bin/bash

cd dejmps
echo "Running bash" >> "results.txt"
for i in {1..1000}
	do
  	netqasm simulate >> "results.txt"
done
