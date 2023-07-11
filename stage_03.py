with open('artifacts.txt', 'r') as f:
    text = f.read()

with open('artifacts.txt', 'w') as f:
    text = f.write(text+ "I have added one line")

print(text)
print("Its end of stage 3.")