# Binary to Decimal
b_num = int(input("Enter a Binary Number:  "))
b_sum = 0
i =0
while b_num !=0:
    rem = b_num %10
    b_sum = b_sum + rem * pow(2,i)
    b_num = int(b_num/10)
    i=i+1
print("Decimal Number is :",b_sum)
# Octal to Deciaml
oct_num = int(input("Enter a Octal Number:  "))
oct_sum =0
i=0
while oct_num!=0:
    rem=oct_num%10
    oct_sum= oct_sum + rem*pow(8,i)
    oct_num=int(oct_num/10)
    i=i+1
print("Deciaml Number is ",oct_sum)

# Base 5 to Deciaml
bf_num = int(input("Enter a Base 5 Number:  "))
bf_sum=0
i=0
while bf_num!=0:
    rem=bf_num%10
    bf_sum= bf_sum + rem*pow(5,i)
    bf_num=int(bf_num/10)
    i=i+1
print("Deciaml Number is ",bf_sum)
sumall = b_sum + oct_sum + bf_sum
print("Final answer is ", sumall)
