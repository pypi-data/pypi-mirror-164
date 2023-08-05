# Time It!

- Python Decorator for timing functions. Its fast, and fun!

```python
from time_it import time_it

@time_it
def time_max(A):
  return max(A)
  
time_max([1,4,2,5,3,3]) # prints execution time of time_max function and returns max value
```
