#!/usr/bin/python3


#Given two non-negative integers num1 and num2 represented as strings, return
#the product of num1 and num2, also represented as a string.

#Example 1:

#    Input: num1 = "2", num2 = "3"
#    Output: "6"

#Example 2:

#    Input: num1 = "123", num2 = "456"
#    Output: "56088"
#    Note:

#    The length of both num1 and num2 is < 110.  
#    Both num1 and num2 contain only digits 0-9.  
#    Both num1 and num2 do not contain any leading zero, except the number 0
#    itself.  
#    You must not use any built-in BigInteger library or convert the
#    inputs to integer directly.


def mul(str1,str2):
    num1,num2 = 0,0

    for i in str1:
        num1 = num1*10+ord(i)-ord('0')
    for i in str2:
        num2 = num2*10+ord(i)-ord('0')

    return(str(num1*num2))


def main():
    print(mul('123','10'))
    
if __name__ == '__main__':
    main()
