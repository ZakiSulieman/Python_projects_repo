# Weighted Exam Score Average


#Enter how many exams you have done
number_of_exams = int(input("Enter number of exams: "))


#Enter how many credits these exam cover
total_credits = int(input("Enter how many credits these exam cover: "))

# Begin with the average of 0 and then add up percentages from each exam  
average = 01

for exam in range(number_of_exams):
    score = int(input("Enter exam score: "))
    exam_credits = int(input("Enter how many credits this exam cover: "))


    average = average + score * exam_credits/total_credits
print(f"Your average is, {average}")




