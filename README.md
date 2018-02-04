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
![Data flow and functionality description of Mnemo.](https://github.com/Thaleia-DimitraDoudali/mnemo/tree/master/figures/system_design.png)

All software components are implemented in Python.
The Sensitivity Engine includes a customized version of the YCSB client. 


