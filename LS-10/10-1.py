#Functions with Outputs

def name_formatting(f_name, l_name):
    if f_name == '' or l_name == '':
        return "Nothing was provided"
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return f"{new_f_name} {new_l_name}"

print(name_formatting(input("What is the first name?: "), input("What is the last name?: ")))
