# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

