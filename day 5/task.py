fruits = ['apple', 'orange', 'pawpaw']
for fruit in fruits:
  print(fruit)
student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]
# max_score = max(student_scores)
# print(max_score)
max_num = student_scores[0]
for score in student_scores:
  if score > max_num:
    max_num = score 
print(max_num)

num = 0
for number in range(1,101):
  num += number
print(num)