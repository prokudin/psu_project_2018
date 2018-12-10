# psu_project_2018
# This project contains results of the fits of HERMES multiplicities.
# The fits are done by JAM3D. There are currently 2 branches of JAM3D:
# master and alexei_gk
# master is standard, alexei_gk is approximate TMD evolution.
# For master directories are inputs, notebooks, samples
# For alexei_gk directories are inputs_alexei_gk, notebooks_alexei_gk
# Steps to perform:
# 1. Go to GIT/jam3d and git pull, (ot git pull origin alexei_gk)
# 2. source setup.bash
# 3. Go to GIT/psu_project_2018
# 4. jam3d -t 3 -p inputs/***.py, or jam3d -t 3 -p inputs_alexei_gk/***.py
# -t 3 makes MC, -p parallel
# the MC files will be in the directory mcdata
# you need to concatenate results, 
# 5. go to mc data and type mcproc . it will create summary.mcp
type mcproc . -c 0.001 it will filter results and create final.mcp
# 6. move summary.mcp and final.mcp to the directory that contains samples
samples for origin and samples_alexei_gk for alexei_gk
# 7. run the corresponding notebook and observe results  