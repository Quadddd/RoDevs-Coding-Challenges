import string

letters = [x for x in string.ascii_letters if x.lower() == x]

def get_str_val(a):
    count = 0
    for i in letters:
        count += a.count(i) * (letters.index(i) + 1)
    return count

def get_string(f, s):
    out = ""
    fC, sC = get_str_val(f), get_str_val(s)
    diff = fC > sC and fC - sC or sC - fC
    out = fC > sC and s or f

    if diff < 26:
        ltr = letters[diff - 1]
        if get_str_val(ltr) > get_str_val(out):
            tempOut = out
            out = ltr
            out += tempOut
    else:
        for i in letters:
            if get_str_val(i) * (letters.index(i) + 1) > fC + sC:
                out += i 
                break
    return out

def eq_string(a, b):
    aC, bC = get_str_val(a), get_str_val(b)
    solved = get_string(a, b)
    print(f"Your output string with a total of {aC + bC} is " + solved)
