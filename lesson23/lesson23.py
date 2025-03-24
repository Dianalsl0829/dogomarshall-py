# Lesson 23
user = True
total = 0
average = 0
while user:
    state = input("Enter mark or 'exit' to quit:")
    mark = 0
    if state.lower() =='exit':
        user = False
        break
    else:
        if 0<=int(state)<=100:
            mark = int(state)
            total += mark
            average += 1

print(f'The average mark is {total/average}.')