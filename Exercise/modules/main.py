#1.  function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
import random 
import string

# used random module methods --- 
# random.choices() - return list of random characters
# random.randint() - return random integer
# random.shuffle() - shuffle the list

# used string module methods --- 
# string.ascii_letters - string of all letters
# string.digits - string of all digits
# string.hexdigits - string of all hexadecimal numbers


"""def user_id_gen_by_user() : 
    num_characters = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs: "))
    for i in range(num_ids) : 
        # work - random.choices() return list of random characters
        # join() - join the list of random characters
        # string.ascii_letters + string.digits - string of all letters and digits
        # k = num_characters - number of random characters to be generated
        print("".join(random.choices(string.ascii_letters + string.digits, k = num_characters)))

user_id_gen_by_user()"""


# 2. function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
"""def rgb_color_gen() : 
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

print(f"rgb_color_gen{rgb_color_gen()}")"""

# 3. function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
"""def list_of_hexa_colors() : 
    for i in range(6) : 
        # print("#" + "".join(random.choices(string.ascii_letters + string.digits, k = 6)))
        print("#" + "".join(random.choices(string.hexdigits, k = 6)))

list_of_hexa_colors() """  


# 4. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
"""
def shuffle_list(arg) : 
    random.shuffle(arg)
    return arg

print(shuffle_list([1, 2, 3, 4, 5]))"""


#  function which returns an array of seven random numbers in a range of 0-9. All the numbers in list must be unique

def random_numbers(length) : 
    newList = []
    # for i in range(length) : 
    #     if random.randint(0, 9) not in newList : 
    #         newList.append(random.randint(0, 9)) 
    #     else : 
    #         i -= 1
    while len(newList) <= length:
        num = random.randint(0, 9)
        if num not in newList:
            newList.append(num)
    return newList

print(random_numbers(7))
print(random_numbers(5))
print(random_numbers(8))


