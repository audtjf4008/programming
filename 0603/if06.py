chr = input("한 문자 입력:")

if chr.islower():
      print(chr.upper())
elif chr >= 'A' and chr <= 'z':     #elif chr >='A' and chr <= 'Z'
    print(chr.lower())
else:
    print(chr)

