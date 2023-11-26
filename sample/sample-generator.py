def sample_generator():
    num = 1
    while num < 11:
        yield num
        num += 1
        
for i in sample_generator():
    print(i, end = " ")