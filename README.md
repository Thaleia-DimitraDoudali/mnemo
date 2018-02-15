# Mnemo
An application profiler that provides users with a cost-benefit presentation of the different sizing configurations of a hybrid memory system, for in-memory key-value store workloads.<br/>

## Prerequisites 
- Default YCSB installation
- Python installation

## Input
Modify the input configuration file `conf.csv` <br/>
Examples of the necessary text files in folder `workload/`

## Execution

    python launch.py conf.csv

## Output
Visualized results in folder `figures/` <br/>
Raw results in `output.txt`

### Architecture
![system_design](https://user-images.githubusercontent.com/10352792/35788436-f344390c-0a02-11e8-91a0-2fabb1b284c7.jpg)


All software components are implemented in Python.<br/>
The Sensitivity Engine includes a customized version of the YCSB client. <br/>


