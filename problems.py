'''01)Electricity Bill Calculator
Moderate

Problem: Write a program that accepts the number of electricity units consumed and calculates the bill using these rates:
- First 100 units: ₹2 per unit
- Next 100 units (101–200): ₹3 per unit
- Units above 200: ₹5 per unit
- Add a fixed meter charge of ₹50.
The rates apply progressively to each portion of consumption, not to every unit at the highest rate.

Example

Input: 250

Expected bill: ₹800

Challenge: Reject negative unit values and handle exactly 0, 100, 200, and 201 units.'''


'''units=int(input())
charges=50
if units<0:
    print("invalid")
else:
    if units<=100:
        rate=charges+(units*2)
    elif units<=200:
        rate=charges+(100*2)+(units-100)*3
    else:
        rate=charges+(100*2)+(100*3)+(units-200)*5
    print(rate)'''


'''02) Triangle Validator and Classifier

Accept three side lengths and determine whether they form a valid triangle.
- All three sides must be positive.
- The sum of any two sides must be greater than the third side.
- If valid, classify it as Equilateral, Isosceles, or Scalene.
- Otherwise, print Invalid triangle.'''


'''a=int(input())
b=int(input())
c=int(input())
if a<=0 or b<=0 or c<=0:
    print("Invalid triangle")
else:
    if (a+b)>c and (b+c)>a and (c+a)>b:
        if a==b and b==c and c==a:
            print("Equilateral Triangle")
        elif a!=b and b!=c and c!=a:
            print("Scalene Triangle")
        else:
            print("Isoceles Triangle")
    else:
        print("Invalid triangle")'''


'''03)advanced Electricity Bill Calculator
Write a program that accepts electricity units and calculates the bill using the following rules:
Units consumed	Rate
First 100 units	₹2/unit
Next 100 units	₹3/unit
Above 200 units	₹5/unit

Additional rules:
- Fixed meter charge: ₹50.
- If the bill before the meter charge exceeds ₹500, apply a 10% discount to the energy charge.
- Negative units are invalid.
- If units are zero, the total bill is ₹50.
- Display the energy charge, discount, meter charge, and final bill separately.'''

'''units=int(input())
charges=50
rate=0
discount=0
if units<0:
    print("invalid")
else:
    if units==0:
        finalrate=charges
    elif units<=100:
        finalrate=charges+(units*2)
    elif units<=200:
        rate=(100*2)+(units-100)*3
        if rate>500:
            discount=rate*0.1
            finalrate=(rate-discount)+charges
        else:
            finalrate=rate+charges
    else:
        rate=(100*2)+(100*3)+(units-200)*5
        if rate>500:
            discount=rate*0.1
            finalrate=(rate-discount)+charges
        else:
            finalrate=rate+charges
    print(rate)
    print(discount)
    print(charges)
    print(finalrate)'''


'''04: Smart Shopping Discount 🛒
Write a Python program that calculates the final amount a customer must pay.
Rules
1. Ask the user for the shopping amount.
2. Ask whether they are a member (yes or no).
3. Apply the first discount based on the shopping amount:
Shopping amount	Discount
Below ₹1,000	0%
₹1,000 to below ₹5,000	10%
₹5,000 or more	20%

4. If the customer is a member, apply an additional 5% discount to the amount remaining after the first discount.
5. Reject negative amounts and invalid membership answers.
6. Print the original amount, first discount, member discount, and final amount to pay'''


'''amount=int(input())
member=input("Are you a member? (yes/no): ").lower()
discount=0
memberdiscount=0

if amount<0:
    print("invalid")
else:
    if amount<1000:
        discount=0
        
    elif amount<5000:
        discount=amount*0.1
        
    else:
        discount=amount*0.2
    price=amount-discount
    if member=="yes":
        memberdiscount=price*0.05
        price=price-memberdiscount
    print(amount)
    print(discount)
    print(amount-discount)
    print(price)'''

'''05)Number Analyzer 🔢
Let's make your next program a little harder.

Write a program that accepts an integer and:
1. Rejects negative numbers.
2. Prints whether the number is even or odd.
3. Checks whether it is divisible by both 3 and 5.
4. Classifies it as:
   - Zero if the number is 0.
   - Small if it is between 1 and 100.
   - Medium if it is between 101 and 1000.
   - Large if it is above 1000.'''


'''x=int(input())
if x<0:
    print("invalid")
else:
    print("even" if x%2==0 else "odd")
    if x%3==0 and x%5==0:
        print("yes")
    else:
        print("no")
    if x==0:
        print("zero")
    elif x>=1 and x<=100:
        print("small")
    elif x>=101 and x<=1000:
        print("medium")
    else:
        print("large")'''

'''06)ATM Withdrawal Simulator 🏧
Moderate Hard
Write a program that simulates withdrawing money from an ATM.

Rules:
1. Start with a balance of ₹10,000.
2. Ask the user how much they want to withdraw.
3. Reject withdrawals that are zero or negative.
4. Reject withdrawals greater than the available balance.
5. Allow withdrawals only in multiples of ₹100.
6. If the withdrawal is valid, subtract it from the balance and display the withdrawn amount and remaining balance.'''

    
'''balance=10000
withdraw=int(input("Enter the amount to withdraw: "))
if withdraw<=0:
    print("invalid")
elif withdraw>balance:
    print("insufficient balance")
elif withdraw%100!=0:
    print("not a multiple of 100")
else:
    balance=balance-withdraw
    print(withdraw)
    print(balance)'''

'''07)Student Result and Grade Calculator 📚
Write a program that accepts marks for five subjects, each out of 100.

Rules:
1. If any mark is below 0 or above 100, print Invalid marks.
2. Calculate the total and percentage.
3. If any subject mark is below 35, the student fails.
4. Otherwise, assign a grade:
Percentage	Grade
90 or above	A+
80 to below 90	A
70 to below 80	B
60 to below 70	C
Below 60	D

5. Print the total, percentage, pass/fail result, and grade.'''


'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if (a < 0 or a > 100 or b < 0 or b > 100 or
    c < 0 or c > 100 or d < 0 or d > 100 or
    e < 0 or e > 100):
    print("Invalid marks")
else:
    total = a + b + c + d + e
    percentage = total / 5

    print("Total:", total)
    print("Percentage:", percentage)

    if a < 35 or b < 35 or c < 35 or d < 35 or e < 35:
        print("Result: Fail")
    else:
        print("Result: Pass")

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "D"

        print("Grade:", grade)'''


'''08)Factorial Calculator'''


'''x=int(input())
fact=1
for i in range(1,x+1):
    fact=fact*i
print(fact)'''


'''09)palindrome'''


'''x=int(input())
temp=x
r=0
while temp>0:
    digit=temp%10
    r=r*10+digit
    temp=temp//10
if x==r:
    print("palindrome")
else:
    print("not a palindrome")'''



'''10)Armstrong number'''


'''
x = int(input())
temp = x
digits = len(str(x))
r = 0

while temp > 0:
    digit = temp % 10
    r = r + digit ** digits
    temp = temp // 10

if x == r:
    print("Armstrong")
else:
    print("Not Armstrong")
'''

'''11)GCD of Two Numbers 💪
The GCD (Greatest Common Divisor) is the largest number that divides two numbers without leaving a remainder.

For example:
- Input: 12 18
- Output: 6
Because 6 is the largest number that divides both 12 and 18.'''

'''a=int(input())
b=int(input())
i=1
gcd=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        gcd=i
    i+=1
print(gcd)'''


'''12)prime number'''


'''x=int(input())
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")'''


'''13)fibonacci series'''

'''a=0
b=1
n=int(input())
for i in range(n):
    print(a)
    a,b=b,a+b
print(a)
print(b)'''


'''14)reverse a number'''

'''x=int(input())
temp=x
r=0
while temp>0:
    d=temp%10
    r=r*10+d
    temp=temp//10
print(r)'''


'''15)strong number
A Strong Number is a number whose digits' factorials add up to the original number.
145=1! + 4! + 5! = 145'''

'''x=int(input())
temp=x
sum=0
while temp>0:
    fact=1
    d=temp%10
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    temp=temp//10
if x==sum:
    print("Strong")
else:
    print("Not Strong")'''

'''16)Perfect number
A Perfect Number equals the sum of its positive divisors, excluding itself.
Example: 6
Its proper divisors are 1, 2, 3.
1 + 2 + 3 = 6
'''
'''x=int(input())
sum=0
for i in range(1,x):
    if x%i==0:
        sum+=i
if sum==x:
    print("Perfect")
else:
    print("Not Perfect")'''


'''17)Harshad Number Checker
A Harshad number is divisible by the sum of its digits.
For example, 18:
- Sum of digits = 1 + 8 = 9
- (18 / 9 = 2), with no remainder.
Therefore, 18 is a Harshad number'''

'''x=int(input())
temp=x
sum=0
while x>0:
    d=x%10
    sum+=d
    x=x//10
if temp%sum==0:
    print("Harshad")
else:
    print("Not Harshad")'''

'''18)Automorphic Number Checker

Moderate → Harder
A number is automorphic if its square ends with the original number.
Example 1: 5

5^2 = 25

25 ends in 5, so it's automorphic.'''

'''x=int(input())
a=x**2
b=a%(10**len(str(x)))
if b==x:
    print("Automorphic")
else:
    print("Not Automorphic")'''


'''19)Abundant Number Checker
A number is abundant if the sum of its proper divisors is greater than the number itself.
For example, 12 has proper divisors 1, 2, 3, 4, 6.
Their sum is:
1+2+3+4+6=16
Since 16>12, the number is abundant.'''

'''x=int(input())
sum=0
for i in range(1,x):
    if x%i==0:
        sum+=i
if sum>x:
    print("Abundant")
else:
    print("Not Abundant")'''


'''20)heck an Amicable Pair

Two different numbers are amicable if the sum of the proper divisors of each number equals the other number.
Example: 220 and 284.
- Proper divisors of 220 add up to 284.
- Proper divisors of 284 add up to 220.
So they are an amicable pair!'''


'''x=int(input())
y=int(input())
sum=0
add=0
for i in range(1,x):
    if x%i==0:
        sum+=i
for i in range(1,y):
    if y%i==0:
        add+=i
if x==add and y==sum:
    print("amicable")
else:
    print("not amicable")'''

'''21)Spy Number Checker

Moderate → Harder
A Spy Number is a number whose digits' sum equals the product of its digits.

Example: 1124
- Sum:1+1+2+4=8
- Product:1*1*2*4=8
Since the sum equals the product, 1124 is a Spy Number'''

'''x=int(input())
temp=x
sum=0
product=1
while temp>0:
    d=temp%10
    sum+=d
    product*=d
    temp=temp//10
if sum==product:
    print("Spy")
else:
    print("not spy")'''

'''22) Digital Root
Keep adding the digits of a number until only one digit remains.
Examples
- Input: 9875 → Output: 2
- Input: 1234 → Output: 1
- Input: 9 → Output: 9
For 9875:

9+8+7+5=29

2+9=11

1+1=2'''


'''x = int(input())
while x >= 10:
    total = 0
    while x > 0:
        d = x % 10
        total += d
        x = x // 10
    x = total
print(x)'''

'''23)second largest'''

'''n=int(input())
lst=list(map(int,input().split()))
largest=lst[1]
second=lst[0]
for i in range(n):
    if lst[i]>largest:
        second=largest
        largest=lst[i]
    else:
        if lst[i]>second and lst[i]!=largest:
            second=lst[i]
    
print(second)'''



'''24)even or odd'''


'''def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
n=int(input())
print(even_odd(n))'''


'''25)sum of two numbers'''

'''def sum_num(a,b):
    return a+b
a=int(input())
b=int(input())
print(sum_num(a,b))'''


'''26)Leap Year Checker
Task: Write a function called is_leap_year(year) that returns True if the year is a leap year and False otherwise.

Rules:
- A year divisible by 400 is a leap year.
- Otherwise, a year divisible by 100 is not a leap year.
- Otherwise, a year divisible by 4 is a leap year.
- All other years are not leap years.'''

def leap_year(n):
    if n%400==0 and n%100!=0:
        return "leap year"
    elif n%100==0 and n%400!=0:
        return "not leap year"
    elif n%4==0 and n%100!=0:
        return "leap year"
    else:
        return "not leap year"
n=int(input())
print(leap_year(n))