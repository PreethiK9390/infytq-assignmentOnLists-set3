#lex_auth_01269441913243238467

def create_largest_number(number_list):
    number_list.sort(reverse=True)
    for i in range(len(number_list)):
        number_list[i]= str(number_list[i])
    return int("".join(number_list))
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
