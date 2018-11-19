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
![mnemo_design](https://user-images.githubusercontent.com/10352792/48679845-f1bfc780-eb62-11e8-8160-274a5d48af6c.jpg)


All software components are implemented in Python.<br/>
The Sensitivity Engine includes a customized version of the YCSB client. <br/>


