#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_name():
    name = input('Please enter your name >>> ')
    if len(name) == 0:
        print('Please enter a name')
        print_name()
    def print_name_subfunc():
        decorator = input('please enter a single character (alphanumeric or symbols) >>> ')
        if len(decorator) != 1:
            print('Please choose a single character')
            print_name_subfunc()
        else:
            patterns = {0:[0],1:[0,0,0,0,1],2:[0,0,0,1,0],3:[0,0,1,0,0],4:[0,0,1,1,1],5:[0,1,0,0,0],6:[0,1,0,1,0],7:[0,1,1,0,0],8:[0,1,1,0,1],9:[0,1,1,1,0],10:[0,1,1,1,1],11:[1,0,0,0,0],12:[1,0,0,0,1],13:[1,0,0,1,0],14:[1,0,0,1,1],15:[1,0,1,0,0],16:[1,0,1,0,1],17:[1,1,0,0,0],18:[1,1,0,0,1],19:[1,1,0,1,1],20:[1,1,1,1,0],21:[1,1,1,1,1]}
            alphabet = {' ':[0],'A':[9,12,12,21,12,12,12],'B':[20,12,12,20,12,12,20],'C':[9,12,11,11,11,12,9],'D':[20,12,12,12,12,12,20],'E':[21,12,11,20,11,12,21],'F':[21,12,11,20,11,11,11],'G':[9,14,11,11,14,12,10],'H':[12,12,12,21,12,12,12],'I':[21,16,3,3,3,16,21],'J':[4,2,2,2,2,13,7],'K':[12,13,15,17,15,13,12],'L':[11,11,11,11,11,12,21],'M':[12,19,16,16,12,12,12],'N':[12,12,18,16,14,12,12],'O':[9,12,12,12,12,12,9],'P':[20,12,12,20,11,11,11],'Q':[9,12,12,12,16,13,8],'R':[20,12,12,20,15,13,12],'S':[10,11,11,9,1,1,20],'T':[21,16,3,3,3,3,3],'U':[12,12,12,12,12,12,9],'V':[12,12,12,12,19,6,3],'W':[12,12,12,16,16,16,6],'X':[12,12,6,3,6,12,12],'Y':[12,12,6,3,3,3,3],'Z':[21,12,2,3,5,12,21]}
            for letter in name:
                for pattern in alphabet[letter.upper()]:
                    for decorator_position in patterns[pattern]:
                        if decorator_position == 0:
                            print(' ', end = "")
                        else:
                            print(decorator, end = "")
                    print('')
                print('')
    print_name_subfunc()


# In[2]:


print_name()


# In[ ]:




