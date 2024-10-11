import sys

STOP_VAL =  -2*10**9

def start_type(): 
    prev = int(input())
    if prev == STOP_VAL:
        return "C", True, prev
    n = int(input())
    if n == STOP_VAL:
        return "C", True, n
    if n == prev:
        return "C", False, n
    elif n < prev:
        return "D", False, n
    else:
        return "A", False, n
        

def main():
    types = {
       "C": "CONSTANT",
        "WA": "WEAKLY ASCENDING",
        "A": "ASCENDING",
        "WD": "WEAKLY DESCENDING",
        "D": "DESCENDING",
        "R": "RANDOM"
    }
    seq_type, if_end, prev = start_type()
    if if_end:
        print(types(seq_type))
        return
    n = int(input())
    while n != STOP_VAL:
        if n == prev:
            if seq_type == "D": 
                seq_type = "WD"
            elif seq_type == "A": 
                seq_type = "WA"
        elif n > prev:
            if seq_type in ["D", "WD"]:
                seq_type = "R"
                break
            elif seq_type == "C":
                seq_type = "WA"
        else:
            if seq_type in ["A", "WA"]:
                seq_type = "R"
                break
            elif seq_type == "C":
                seq_type = "WD"
        prev = n
        n = int(input())
    print(types[seq_type])
    return


if __name__ == '__main__':
    main()
