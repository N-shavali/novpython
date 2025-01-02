# corr_ans=0
# wrong_ans=0
# q=['1.what is the capital of andhra pradesh?','2. who is the cm of andhra pradesh?','3. what is the national animal of india?','4.how many colours in national flag?','5.what is the name of python trainer in scholar logic']
# ans=['vizag','babu','tiger','3','mr arjun']
# for x in q:
#     print(x)
#     user_ans=input('Enter Your Answer :').lower()
#     if user_ans in ans:
#         corr_ans+=1
#         print('correct Answer')
#     else:
#         print('Wrong Answer')
#         wrong_ans+=1
#     print('percentage',((corr_ans/(corr_ans+wrong_ans))*100))

corr_ans=0
wrong_ans=0
q=['1.what is the capital of andhra pradesh?','2. who is the cm of andhra pradesh?','3. what is the national animal of india?','4.how many colours in national flag?','5.what is the name of python trainer in scholar logic']
ans=['vizag','babu','tiger','3','mr arjun']
for x in range(len (q)):
    print(q[x])
    user_ans=input('Enter Your Answer :').lower()
    if user_ans==ans[x]:
        corr_ans+=1
        print('correct Answer')
    else:
        print('Wrong Answer')
        wrong_ans+=1
    print('percentage',((corr_ans/(corr_ans+wrong_ans))*100))


# att=[100,200,[60,70]]
# print(att[2][1])

# att=[100,78,77,66,[55,66],90]
# print(att[3])


