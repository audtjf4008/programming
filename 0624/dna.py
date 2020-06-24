def comp(seq):
    comp_dict={'A':'T','T':'A','C':'G','G':'C'}
    seq_comp = ""
    for char in seq:
        if char in comp_dict:
            seq_comp += comp[char]
        else:
            seq_comp += '?'
    retrun seq_comp

def rev(seq):
    seq_dna = "ATGC"
    seq_rev = ""
    for char in seq:
        if char in seq_dna:
            seq_rev += char
        else:
            seq_rev += '?'
    seq_rev = ''.join(reversed(seq_rev))

def rev_comp(seq):
    tmp = comp(seq)
    return rev(tmp)

src = input("DNA sequence : ")
cvnt = int(input("1(comp), 2(Rev), 3(Rev_comp): "))
if (cvnt >= 1 and cnvt <= 3):
    if (cnvt ==1):
        rst = comp(src)
    elif (cnvt == 2):
        rst = rev(src)
    else:
        ret = rev_comp(src)
    print(src, "->", rst)
else:
    print("1(comp), 2(Rev), 3(Rev_comp)!!")
