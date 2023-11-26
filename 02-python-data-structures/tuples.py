"""
An introduction to tuples
"""

t = ("ballet", "hip-hop", "modern")
print(t)
print(type(t))

# adding to the tuple, use concatenation
print(t + ("jazz", "classical"))

# using mixed types and nesting
# tuples can work without parentheses too
t_mixed = "jazz", True, 3
print(t_mixed)

t_dance = ("jazz", 3), ("ballroom", 2), ("contemporary", 5)
print(t_dance)