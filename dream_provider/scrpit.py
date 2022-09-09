import string    
import random
item = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase ,k = 10))    
print(str(item)) 