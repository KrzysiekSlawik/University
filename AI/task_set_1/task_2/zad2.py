POLISH_WORDS:set = set()
with open("polskie_slowa.txt", encoding="utf-8") as f:
    for line in f:
        POLISH_WORDS.add(line.strip())
TADEUSZ_LINES:list[str]=[]
with open("pan_tadeusz_bez_spacji.txt", encoding="utf-8") as f:
    for line in f:
        TADEUSZ_LINES += [line]

LEGIT_SEQUENCE:dict[str, list[str]] = {}
LEGIT_SEQUENCE[""] = []
def word_reward(word:str) -> int:
    return len(word) ** 2

def max_seq(a:list[str], b:list[str]) -> list[str]:
    reward_a:int = sum(map(word_reward, a))
    reward_b:int = sum(map(word_reward, b))
    if reward_a > reward_b:
        return a
    return b

def solve(line:str) -> list[str]:
    max_sequence:list[str] = []
    for i in range(1,len(line)+1):
        if line[:i] in POLISH_WORDS:
            if line[i:] in LEGIT_SEQUENCE:
                max_sequence = max_seq([line[:i]] + LEGIT_SEQUENCE[line[i:]], max_sequence)
            else:
                max_sequence = max_seq([line[:i]] + solve(line[i:]), max_sequence)
        else:
            continue
    LEGIT_SEQUENCE[line] = max_sequence
    return max_sequence

def make_solution_line(line:str) -> str:
    LEGIT_SEQUENCE = {}
    LEGIT_SEQUENCE[""] = []
    separator = ' '
    return separator.join(solve(line))

def aux():
    f = open('zad2_output.txt', 'w', encoding="utf-8")
    for line in TADEUSZ_LINES:
        f.write("%s\n" % make_solution_line(line))

aux()