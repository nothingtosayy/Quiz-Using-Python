# Quiz Logic

q1 = """Who is our Prime Minister?
            a)Rahul Gandhi
            b)Chiranjeevi
            c)Narendra Modi"""
q2 = """Whose nickname is king of Cricket?
            a)M.s Dhoni
            b)Virat Kohli 
            c)Sachin"""
q3 = """Who is called as Missile Man of India?
            a)Dr.A.P.J Abdul Kalam
            b)ManMohan Singh
            c)Rahul Gandhi"""
marks = 0    
questions_dict = {q1:"c",q2:"b",q3:"a"}
for question in questions_dict:
    print(question)
    user_ans = input("Enter your option : ")
    if user_ans == questions_dict[question]:
        print("Correct Answer")
        marks = marks + 1
    else:
        print("Wrong Answer")
        marks = marks - 1
    user_exit_process = input(f"Want to exit(yes/no) : ")
    if user_exit_process == 'yes':
        break
print(f"Marks you have been awarded are : {marks}")
