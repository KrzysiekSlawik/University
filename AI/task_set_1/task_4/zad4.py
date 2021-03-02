tasks:list[list[str]] = []
with open("zad4_input.txt", encoding="utf-8") as f:
    for line in f:
        tasks += [' '.split(line)]

def opt_dist(sequence, d):
    prefix = []
    n = int(len(sequence))
    answer = n
    prefix = [0]*n
    pref_sum = 0
    for i in range(n):
        prefix[i] = pref_sum
        if sequence[i] == '1':
            pref_sum+=1
    
    iter = 0
    while iter + d < n:
        ones_before = prefix[iter]
        ones_in_range = prefix[iter+d] - ones_before
        ones_after = prefix[n-1] - ones_in_range
        changes_needed = ones_before + ones_after + d - ones_in_range
        if changes_needed < answer:
            answer = changes_needed
        iter+=1
    return answer

def main():
    # input 
    line = input()
    args = line.split()
    
    sequence = args[0]
    d = int(args[1])
    print(opt_dist(sequence,d))

f = open('zad4_output.txt', 'w', encoding="utf-8")
    for task in tasks:
        f.write("%s\n" % make_solution_line(line))

