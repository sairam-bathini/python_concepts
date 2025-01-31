'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example




The query_name is 'beta'. beta's average score is .

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50
Language
Pypy 3
More
56789101112131415161718194321
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    m = len(scores)
…    formatted_sum = f"{average:.2f}"
    print(formatted_sum)
        
EMACS
Line: 1 Col: 1

Test against custom input
Python
You have earned 10.00 points!
You are now 5 points away from the 3rd star for your python badge.
88%105/110
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5

Test case 6

Test case 7

Test case 8
Compiler Message
Success
Input (stdin)
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Expected Output
56.00
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy

'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    m = len(scores)
    
    sum = 0
    for key, value in student_marks.items():
        for i in range(m):
            if  key == query_name:
                sum = sum + value[i]
                #print(sum)
    
    average = sum / m
    #print(average)
    formatted_sum = f"{average:.2f}"
    print(formatted_sum)
