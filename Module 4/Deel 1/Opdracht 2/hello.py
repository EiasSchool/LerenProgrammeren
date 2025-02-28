def hello(number):
    answer = ""
    for i in range(number):
        answer += f'Hello from function town {i + 1}!\n'
    return answer.strip()
    
print(hello(3))
print(f"\n{hello(7)}")