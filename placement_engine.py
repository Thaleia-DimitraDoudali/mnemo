import os

def load_client(name, ip, port, key_file, keylength_file, valuelength_file, num_keys):

    cmd = ("cd YCSB/; bin/ycsb load " + name +
        #" -s -P workloads/workloada" +
        " -s -p workload=com.yahoo.ycsb.workloads.CoreWorkload" +
        " -p recordcount=" + num_keys +
        " -p operationcount=" + num_keys +
        " -p " + "customkeyfile=" + key_file +
        " -p " + "customkeylengthfile=" + keylength_file +
        " -p " + "customvaluelengthfile=" + valuelength_file +
        " -p " + name + ".host=" + ip +
        " -p " + name + ".port=" + port +
        " > ../" + res_file )

    print cmd
    os.system(cmd)


##### Main function called from other python file ####
def main(name, fast_ip, fast_port, slow_ip, slow_port, fast_key_file, slow_key_file, fast_keylength_file, slow_keylength_file, fast_valuelength_file, slow_valuelength_file, fast_num_keys, slow_num_keys):
    load_client(name, fast_ip ,fast_port, fast_key_file, fast_keylength_file, fast_valuelength_file, fast_num_keys)
    load_client(name, slow_ip ,slow_port, slow_key_file, slow_keylength_file, slow_valuelength_file, slow_num_keys)
