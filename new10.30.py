from iteration_utilities import deepflatten
# if you only have one depth nested_list, use this
def flatten(l):
  return [item for sublist in l for item in sublist]
l = [[1,2,3],[3]]
print(flatten(l))
# [1, 2, 3, 3]
# if you don't know how deep the list is nested
l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]
print(list(deepflatten(l, depth=3)))

a, b = 1,0
try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")
