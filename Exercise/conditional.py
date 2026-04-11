'''
1. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
'''

# UserFruit = input("Enter food name :- ")
# fruits = ['banana', 'orange', 'mango', 'lemon']   # list 

# for i in range(4) : 
#     if fruits[i] == UserFruit : 
#         print("already exist")
#         break
#     else : 
#         fruits.append(UserFruit)
#         print(set(fruits))
#         break

    
'''
2. * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
   * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
   * If a person skills has only JavaScript and React, print('He is a front end developer'), 
    if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
    if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
'''

person={ 'skills': ['React', 'JavaScript'] } 

#   
    # if person['skills'] : 
    #     # print(person['skills'][2])
    #     print(person['skills'][int(person['skills'].__len__()/2)])


#   
    # for i in person.keys() :
    #     if i == 'skills' : 
    #         print(True)
    #         print(type(person['skills']))  # list
    #         for i in person['skills'] : 
    #             if i == 'Python' : 
    #                 print("all done")
    #             else : 
    #                 print("person has no python skills")
    #     else : 
    #         print("person has no skills")

    
#   needs values in same order to match
''' 
    cond1 =  person['skills'] == ['JavaScript', 'React']
    cond2 = person['skills'] == ['Node', 'Python', 'MongoDB']
    cond3 = person['skills'] == ['React', 'Node', 'MongoDB']
    if cond1 : 
        print("He is a front end developer")
    elif cond2 : 
         print("He is a backend developer")
     elif cond3 : 
         print("He is a fullstack developer")
     else : 
         print("unknown title")
'''

#   values in any order can be checked using all() function
'''
    cond1 = ['JavaScript', 'React']
    cond2 = ['Node', 'Python', 'MongoDB']
    cond3 = ['React', 'Node', 'MongoDB']

    if all(i in person['skills'] for i in cond1 ) :
        print("frontend dev")
    elif all(i in person['skills'] for i in cond2 ) :
        print("backend dev")
    elif all(i in person['skills'] for i in cond3 ) :
        print("fullstack dev")
    else :
        print("unknown title")
'''