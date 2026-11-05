'''
check whether a character is a vowel or consonant.

'''
ch = input("Enter a Charactar ")
ch = ch.upper()

if ch == 'A' or ch =='E' or ch == 'I' or ch=='O' or ch== 'U':
    print("This charactor is vowel ")

elif ch =='B' or ch =='C' or ch == 'D' or ch=='F' or ch== 'G' or ch =='H' or ch =='J' or ch == 'K' or ch=='L' or ch== 'M' or ch =='N' or ch =='P' or ch == 'Q' or ch=='R' or ch== 'S' or ch =='T' or ch =='V' or ch == 'W' or ch=='X' or ch=='Y' or ch=='Z':
    print("This is consonant")

else:
    print("This is a Special Character")