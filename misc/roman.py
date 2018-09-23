#!/usr/bin/python3

def roman2dec(str):
    sum = 0
    C_hascome, X_hascome, I_hascome = False, False, False
    valid = { 'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1 }
    for i in str:
        if i == 'C': C_hascome = True
        if i == 'X': X_hascome = True
        if i == 'I': I_hascome = True
        sum += valid[i]
        if (i == 'M' or i == 'D') and C_hascome:
            sum -= 2*valid['C']
            C_hascome = False
        if (i == 'L' or i == 'C') and X_hascome:
            sum -= 2*valid['X']
            X_hascome = False
        if (i == 'V' or i == 'X') and I_hascome:
            sum -= 2*valid['I']
            I_hascome = False

    return(sum)

def main():
    print(roman2dec('MDCCCXLIV'))
    
if __name__ == '__main__':
    main()

