from fake_math import divide as fake_divide
from true_math import divide as true_divide

fake_result = fake_divide(10, 0)
true_result = true_divide(10, 0)
print(fake_result)
print(true_result)

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)