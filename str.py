corr_ans=0
wrong_ans=0
print('1. which is the capital of karnataka?')
user_ans=input('Enter Your Answer:').lower()
print(user_ans)
if user_ans=='bangalore':
    corr_ans+=1
    print('correct answer')
else:
    wrong_ans+=1
    print('wrong answer')
print('2. who is the father of python?')
user_ans=input('Enter Your Answer:')
print(user_ans)
if user_ans=='van rossum':
    corr_ans+=1
    print('correct answer')
else:
    wrong_ans+=1
    print('wrong answer')
print('3.what is the name of python trainer in scholar logic?')
user_ans=input('Enter Your Answer:')
print(user_ans)
if user_ans=='mr arjun':
    corr_ans+=1
    print('correct answer')
else:
    wrong_ans+=1
    print('wrong answer')
print('4. what is the national bird of india?')
user_ans=input('Enter Your Answer:')
print(user_ans)
if user_ans=='peacock':
    corr_ans+=1
    print('Correct answer')
else:
    wrong_ans+=1
    print('wrong')
print('5. who is the founder of absolute shawarma?')
user_ans=input('Enter Your Answer:')
print(user_ans)
if user_ans=='arjun':
    corr_ans+=1
    print('correct answer')
else:
    wrong_ans+=1
    print('wrong answer')
print('percentage',((corr_ans/(corr_ans+wrong_ans))*100))