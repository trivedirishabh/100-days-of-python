
import random
#list comprehension

# number = [1,2,3]
# new_list = [i + 1 for i in number]
# print(new_list)

# name = "bob"

# new_list = [i for i in name]
# print(new_list)

# new_list = [ i*2 for i in range(1,5)]
# print(new_list)

# conditional list comprehension
# new_list = ["alex", "beth", "carolina", "Dave", "Elanor", "freddie"]

# short_name = [name.upper() for name in new_list if len(name) > 5]
# print(short_name)

# Dictionary Comprehension


new_list = ["alex", "beth", "carolina", "Dave", "Elanor", "freddie"]
#new_dict = {new_key:new_value for (key,value) in dict.items() if test

student_scores = {student:random.randint(1,100) for student in new_list}
print(student_scores)

passed_student = {student:score for (student,score) in student_scores.items() if score > 32}

print(passed_student)