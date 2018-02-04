############# MNEMO ##############
## Author: Thaleia Dimitra Doudali
##################################

import sys, csv

import sensitivity_engine as sensitivity
import pattern_engine as pattern
import estimate_engine as estimate





#### Mnemo's Input: appropriately modify the conf.csv file####
def read_input(file):
    reader = csv.reader(open(file, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v
    return d


if __name__ == "__main__":

    conf = read_input(sys.argv[1])

    # Step 1: Execute input workload to get the performance baselines
    perf_base = sensitivity.main()

    # Step 2: Feed into the Pattern Engine, the workload related input and get the request access pattern as a dictionary
    reqs_dict = pattern.main(conf['KeyFile'], conf['ReqFile'], conf['MaxKeyID'])


