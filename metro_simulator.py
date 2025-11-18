# def display_info():
#     ## need to design the ui figma check!!!!!


#     return 1

with open('./data/Delhi metro.csv', 'r') as f:
    metro_data = f.readlines()

for line in metro_data:
    print(line.strip().split(','))