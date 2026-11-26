c_ans=0
w_ans=0
q=input("what is capital of India").lower()
print(q, "after Lower")

if q=="delhi":
    c_ans=1
    print("correct answer")
else:
    w_ans=1
    print("wrong answer")

q=input("what is capital of Karnataka").lower()
print(q, "after Lower")
if q=="bengaluru":
    c_ans=1
    print("correct answer")
else:
    w_ans=1
    print("wrong answer")
print(c_ans, "correct answer")
print(w_ans, "wrong answer")