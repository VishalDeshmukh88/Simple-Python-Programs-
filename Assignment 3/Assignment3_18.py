import random
in_list=['a','e','i','o','u']

for i in range(10):
    random.shuffle(in_list)
    print(''.join(in_list))