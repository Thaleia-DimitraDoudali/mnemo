import sys
import matplotlib.pyplot as plt

## Parse key and operation distribution files into a dictionary
#  The dictionary will have as a key the actual key ID
#  and as a value, a list of the READ, UPDATE operations
#  the total requests towards this key will be the length of the value list
def get_key_ops_dict(keyfile, opsfile, max_key_id):
    max_key_id = int(max_key_id)
    res = {}
    for k in range(0, max_key_id):
        res[k] = []
    ### Read key distribution file
    with open(keyfile, 'r') as f:
        keys_in = f.readlines()
        keys_in = [x.strip() for x in keys_in]
    ### Read ops distribution file
    with open(opsfile, 'r') as f:
        ops_in = f.readlines()
        ops_in = [x.strip() for x in ops_in]
    ### Populate the dictionary
    for i in range(0, len(keys_in)):
        kk = int(keys_in[i])
        res[kk].append(ops_in[i])
    return res

## Returns the mapping between requests and keys
def get_key_reqs(key_ops_dict, max_key_id):
    max_key_id = int(max_key_id)
    ### How many requests have been issued for <= keys
    reqs = []
    sum = 0
    for k in range(0, max_key_id):
        sum = sum + len(key_ops_dict[k])
        reqs.append(sum)
    return reqs;

## Returns the mapping between reads, writes and keys
def get_key_ops(key_ops_dict, max_key_id):
    ### How many reads, writes have been issued for <= keys
    max_key_id = int(max_key_id)
    r = 0
    w = 0
    reads = []
    writes = []
    for k in range(0, max_key_id):
        for req in key_ops_dict[k]:
            if (req == 'READ'):
                r = r + 1
            elif (req == 'UPDATE'):
                w = w + 1
        reads.append(r)
        writes.append(w)
    return (reads, writes)


## Plot key to requests, reads and writes.
def plot_key_ops_distr(keyfile, opsfile, max_key_id):
    max_key_id = int(max_key_id)
    key_ops_dict = get_key_ops_dict(keyfile, opsfile, max_key_id)
    reqs = get_key_reqs(key_ops_dict, max_key_id)
    (reads, writes) = get_key_ops(key_ops_dict, max_key_id)

    fig, ax = plt.subplots()
    ax.plot(reqs, '-', 	 lw = 2, color='black', label='Total Requests')
    ax.plot(reads, '--', lw = 3, color='red',	label='Reads')
    ax.plot(writes, '-.', lw = 5, color='green', label='Writes')

    ax.legend(loc='best', ncol=1, fontsize=18)
    ax.set_xlabel('Keys', fontsize=18)
    ax.set_xlim(0, max_key_id)
    ax.set_ylabel('Requests', fontsize=18)
    plt.savefig("figures/pattern.png", format='png', bbox_inches='tight')
    #plt.show()

##### Main function called from other python file ####
def main(keyfile, opsfile, max_key_id):
    # Optionally, visualize the distribution
    plot_key_ops_distr(keyfile, opsfile, max_key_id)
    # Analyze the request and key access pattern and return it to Mnemo in the form of a dictionary
    key_ops_dict = get_key_ops_dict(keyfile, opsfile, max_key_id)
    (reads, writes) = get_key_ops(key_ops_dict, max_key_id)
    res_dict = {}
    res_dict['reads'] = reads
    res_dict['writes'] = writes
    return res_dict
