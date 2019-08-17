import random

code=[chr(x) for x in range(97,123)]+[str(x) for x in range(10)]
code=random.sample(code,6)
code=''.join(code)
print(code)
