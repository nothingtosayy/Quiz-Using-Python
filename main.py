# Basic Quiz Logic!!


dict = {"q1":"c","q2":"b","q3":"a"}
questions = ["Who is our Prime Minister?\n a)Balayya\n b)Chiranjeevi\n c)Narendra Modi\n", 
"Whose nickname is king of Cricket?\n a)M.s Dhoni\n b)Virat Kohli\n c)Sachin\n", 
"Who is called as Missile Man of India?\n a)Dr.A.P.J Abdul Kalam\n b)ManMohan Singh\n c)Rahul Gandhi\n"]
marks = 0
highest_marks = 3
for question in questions:
    print(question)
for i in dict:
    user_ans = input(f"Enter the option for {i} : ")
    if user_ans == dict[i]:
        marks = marks + 1
    else:
        marks = marks - 1
print(f"Marks you have been awarded are : {marks}")
if marks == highest_marks:
    print("Woh! congratulations, You are the Topper")
else:
    print("Best Luck Next time")
