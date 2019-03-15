import sys
start_block_reward = 100
reward_interval = 800000

def max_money():
    total = 0
    cnt = 1
    current_reward = block_subsidy(cnt)
    while current_reward > 0:
        total += current_reward
        totalFLO = total/100000000
        sys.stdout.write("\rBlock: %d, Reward: %d flotoshis, Total: %f FLO          " % (cnt, current_reward, totalFLO))
        cnt += 1
        current_reward = block_subsidy(cnt)
    return total

def block_subsidy(height):
    halvings = height / reward_interval
    if halvings > 64:
        return 0

    subsidy = 100 * 10**8

    subsidy >>= int(halvings)
    return subsidy


print("\nTotal FLO to ever be created: ", max_money()/100000000, "FLO")

