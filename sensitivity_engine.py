import re, os

### Parses the results file of YCSB client execution.
## Uses regular expressions to match the text that will give the corresponding metric
### Returns values in a dictionary
def parse_client_output(fname):

    res_dict = {}

    exp_run = re.compile("\[OVERALL\], RunTime\(ms\), (?P<t>\d+)")
    exp_rlat = re.compile("\[READ\], AverageLatency\(us\), (?P<t>\d+.\d+)")
    exp_wlat = re.compile("\[UPDATE\], AverageLatency\(us\), (?P<t>\d+.\d+)")

    res_dict['avg_write'] = 0.0
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

# Executes the customized version of YCSB client 
# against the specified data store
def run_client(name, ip, port, res_file, key_file, ops_file, num_keys, num_ops):
    
    cmd = ("cd YCSB/; bin/ycsb run " + name + 
        #" -s -P workloads/workloada" + 
        " -s -p workload=com.yahoo.ycsb.workloads.CoreWorkload" +
        " -p recordcount=" + num_keys + 
        " -p operationcount=" + num_ops + 
        " -p " + "customkeyfile=" + key_file +  
        " -p " + "customopsfile=" + ops_file +  
        " -p " + name + ".host=" + ip + 
        " -p " + name + ".port=" + port +  
        " > ../" + res_file )
    
    print cmd
    os.system(cmd)


##### Main function called from other python file ####
def main(name, fast_ip, fast_port, slow_ip, slow_port, key_file, ops_file, num_keys, num_ops):
    # Step 1: Run the input workload in all-fast
    fast_file = "raw_results/fast_results.txt"
    run_client(name, fast_ip ,fast_port, fast_file, key_file, ops_file, num_keys, num_ops)
    
    # Step 2: Run the input workload in all-slow
    slow_file = "raw_results/slow_results.txt"
    run_client(name, slow_ip ,slow_port, slow_file, key_file, ops_file, num_keys, num_ops)
    
    # Step 3: Analyze the result files on the client and get the performance baselines
    fast_dict, slow_dict = get_perf_baselines(fast_file, slow_file)
    return fast_dict, slow_dict
