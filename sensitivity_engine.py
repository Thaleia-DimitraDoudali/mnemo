import re

### Parses the results file of YCSB client execution.
## Uses regular expressions to match the text that will give the corresponding metric
### Returns values in a dictionary
def parse_client_output(fname):

    res_dict = {}

    exp_run = re.compile("\[OVERALL\], RunTime\(ms\), (?P<t>\d+)")
    exp_rlat = re.compile("\[READ\], AverageLatency\(us\), (?P<t>\d+.\d+)")
    exp_wlat = re.compile("\[UPDATE\], AverageLatency\(us\), (?P<t>\d+.\d+)")

    with open(fname, 'r') as my_file:
        lines = my_file.readlines()
        for row in lines:
            # Total runtime
            res_run = re.match(exp_run, row)
            if (res_run != None):
                runp = res_run.group('t')
                res_dict['runtime'] = float(runp)
            # Avg read time
            res_run = re.match(exp_rlat, row)
            if (res_run != None):
                runp = res_run.group('t')
                res_dict['avg_read'] = float(runp)
            # Avg write time
            res_run = re.match(exp_wlat, row)
            if (res_run != None):
                runp = res_run.group('t')
                res_dict['avg_write'] = float(runp)

    return res_dict


# Extracts the raw overall runtime, avg read time, avg write time
# for the all-fast and all-slow cases
# to set the performance baselines for the estimate model
def get_perf_baselines(fast_file, slow_file):

    fast_dict = parse_client_output(fast_file)
    slow_dict = parse_client_output(slow_file)

    return fast_dict, slow_dict

##### Main function called from other python file ####
def main():
    # Run the input workload in all-fast
    fast_file = "workload/fast_results.txt"
    # Run the input workload in all-slow
    slow_file = "workload/slow_results.txt"
    # Analyze the result files on the client and get the performance baselines
    fast_dict, slow_dict = get_perf_baselines(fast_file, slow_file)
    return fast_dict, slow_dict
