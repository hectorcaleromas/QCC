# Performance of Distillation Protocols
In this project we analyze the performance of different distillation protocols: BBPSSW, DEJMPS and EPL in the presence of environmental noise (depolarization) and gate errors, using the Netsquid simulator.

# run.py
This is the main file to run simulations. It executes the shell file script.sh
# script.sh
Bash file that runs the selected protocol (DEJMPS by default) for 1000 iterations. In order to select the desired protocol, change cd dejmps to cd nameprotocol.
# Protocol folders
The files for different protocols can be found in their respective folders. The parameters of the network (depolarizing noise, gate errors...) can be tuned in the network.yaml file.

# Authors
Sibasish Mishra, Kishore Kumar & Héctor Calero.
