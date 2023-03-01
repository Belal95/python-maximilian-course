def get_user_input():
    name = input("Enter your name:")
    age = input("Enter your age:")
    return [name, age]


user_data = get_user_input()

name = user_data[0]
age = user_data[1]


def print_user_data(name=name, age=age):
    decades = int(age)//10
    string = 'You are '+name+', you are '+age + \
        ' years old, you lived '+str(decades)+' decades'
    print(string)


print_user_data()
