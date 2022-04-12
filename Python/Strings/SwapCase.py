def swap_case(s):
    outarr = []
    for i in range(0, len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                outarr.append(s[i].lower())
            elif s[i].islower():
                outarr.append(s[i].upper())
            else:
                outarr.append(s[i])
        else:
            outarr.append(s[i])
                
    return "".join(outarr)
