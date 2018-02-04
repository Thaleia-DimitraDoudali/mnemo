import sys, csv
import matplotlib.pyplot as plt

###### Estimation model #####
def estimate(freads, fwrites, drlat, dwlat, srun):
    return srun + freads*drlat/1000.0 + fwrites*dwlat/1000.0

def slowdown(est,frun):
    return (est/frun - 1)*100

###### Cost model ######
def mem_to_cost(p, max_key_id):
    res = []
    for F in range(0,max_key_id,1):
        r = (F + (max_key_id - F)*p)/max_key_id
        res.append(r)
    return res

## Estimate input:
#  1. Workload access pattern
#  2. Fast and Slow performance baselines
#  3. The max key ID in the key space
#  4. Flag to normalize values as a performance slowdown
def get_estimate(reqs_dict, fast_base, slow_base, max_key_id, do_norm):
    max_key_id = int(max_key_id)
    est=[]
    # First value added is the actual worst case runtime, when all data is in slow memory.
    est.append(slow_base['runtime'])
    # For all other keys calculate the estimate:
    for i in range(1, max_key_id):
        est.append(estimate(reqs_dict['reads'][i], reqs_dict['writes'][i],
                            fast_base['avg_read'] - slow_base['avg_read'],
                            fast_base['avg_write'] - slow_base['avg_write'],
                            slow_base['runtime']))
    # Last value added is the actual best case runtime, when all data is in fast memory.
    est.append(fast_base['runtime'])

    #Normalize data?
    if (do_norm == "True"):
        est = [slowdown(x, fast_base['runtime']) for x in est]
    return est

## Plot the estimate curve as performance to keys and performance to cost reduction factor.
def plot_estimate(p, est, max_key_id, do_norm):
    p = float(p)
    max_key_id = int(max_key_id)
    # x-axis representations:
    x = []
    x.append(range(0, max_key_id+1))
    x.append(mem_to_cost(p, max_key_id+1))

    for repr in range(0, len(x)):

        fig, ax = plt.subplots()
        ax.plot(x[repr], est, '-', color='blue', label='estimate', lw=1)
        ax.legend(loc='best', ncol=1, fontsize=16)
        plt.grid(True)
        if (do_norm == "True"):
            ax.set_ylabel('Runtime slowdown (%)', fontsize=18)
        else:
            ax.set_ylabel('Runtime (ms)', fontsize=18)
        if repr == 0:
            ax.set_xlabel('Keys', fontsize=18)
            plt.savefig("figures/estimate_to_keys.png", format='png', bbox_inches='tight')

        else:
            ax.set_xlabel('Memory cost reduction factor', fontsize=18)
            plt.savefig("figures/estimate_to_cost.png", format='png', bbox_inches='tight')
        #plt.show()

## Generate the output csv file
def generate_output_format(p, est, max_key_id, do_norm):
    p = float(p)
    max_key_id = int(max_key_id)
    keys = range(0, max_key_id+1)
    price = mem_to_cost(p, max_key_id+1)

    output = []
    for i in range(0,len(est)):
        output.append([str(keys[i]), str(est[i]), str(price[i])])
    return output


##### Main function called from other python file ####
def main(p, reqs_dict, fast_base, slow_base, max_key_id, do_norm):
    est = get_estimate(reqs_dict, fast_base, slow_base, max_key_id, do_norm)
    plot_estimate(p, est, max_key_id, do_norm)
    output = generate_output_format(p, est, max_key_id, do_norm)
    return output
