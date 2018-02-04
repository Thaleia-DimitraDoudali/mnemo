# mnemo
An application profiler that provides users with a cost-benefit presentation of the different sizing configurations of a hybrid memory system, for in-memory key-value store workloads.

## Input
Modify the input configuration file `conf.csv`
Examples of the necessary text files in folder `workload/`

## Execution

    python launch.py conf.csv

## Output
Visualized results in folder `figures/`
Raw results in `output.txt`

### Architecture
![system_design](https://user-images.githubusercontent.com/10352792/35782166-4938ccba-09c2-11e8-8205-3bdf5a96fb84.png)


All software components are implemented in Python.<br/>
The Sensitivity Engine includes a customized version of the YCSB client. 


