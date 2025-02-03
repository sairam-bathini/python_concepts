maths = int(input("Marks in Maths: "))
science = int(input("Marks in Science: "))
english = int(input("Marks in English: "))

total_marks = maths + science + english
Average = total_marks/ 3
percentage = (total_marks/300)*100

if percentage >= 80 and percentage <= 100:
    grade = "A"
elif percentage >= 50 and percentage <= 79:
    grade = "B"
else:
    grade = "C"

print(f"Total Marks: {total_marks}\nAverage: {Average}\nGrade:{grade}")
