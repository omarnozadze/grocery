grocery_list = {}


while True:
    try:
        grocery_item = input()
    except EOFError:
        break
    if grocery_item in grocery_list:
        grocery_list[grocery_item.upper()] += 1 
    else: 
        grocery_list[grocery_item.upper()] = 1 
    
for grocery_item in grocery_list.key():
    print(grocery_list[grocery_item], grocery_item)