#task 6
name=input('enter your name:')
email=input('enter your email ID:')
age=int(input('enter your age:'))
gender=input('enter your gender:')
if (age>13):
    print('your account is created:')
else:
    print('you are under age:') 
#task7
a='doller'
currency=input('enter your currency name:') 
amount=int(input('enter the amount:'))
currency2=input('currency you want to convert in:')     
 

print('doller into PKR:',amount*275)
print('euros into pkr:',amount*296) 

print('yen into pkr:',amount*50)    
#task8
deposit=1  
withdraw=2000
check_balance=3
current_balance=5000
if(withdraw==current_balance):
    print('cash out withdraw amount')
else:
    print('you do not have enouhh balance')   
if(check_balance==current_balance):
    print(3)  

