a = 30
b = 5
last_name = "Romanitch"   
c = len(last_name)

is_valid_range = b < c < a       
is_greater = a > b               
is_not_equal = b != c            

is_greater_or_equal = b >= a     
is_less_or_equal = c <= b        
is_equal = a == c                

print("is_valid_range =", is_valid_range, type(is_valid_range).__name__)
print("is_greater =", is_greater, type(is_greater).__name__)
print("is_not_equal =", is_not_equal, type(is_not_equal).__name__)

print("is_greater_or_equal =", is_greater_or_equal, type(is_greater_or_equal).__name__)
print("is_less_or_equal =", is_less_or_equal, type(is_less_or_equal).__name__)
print("is_equal =", is_equal, type(is_equal).__name__)