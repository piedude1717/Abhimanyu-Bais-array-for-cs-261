# DynamicArray Scratchpad
# Abhimanyu, Bais
# Use this as a "scratchpad" to tinker with your data structure.


from dynamic_array import DynamicArray

a = DynamicArray()
a.append('fee')
a
a.append('fi')
print(a)
a.append('fo')
print(a)
last_element = a.pop()
print(a)
assertEqual('fo', last_element)
assertEqual(2, len(a))

