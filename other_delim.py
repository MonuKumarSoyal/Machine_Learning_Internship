import re

input_file = "./source.txt"
output_file = "./target.txt"

with open(input_file, "r") as source:
  lines = source.readlines()

source_sents = [line.strip() for line in lines]
# print(source_sents)


# initializing delim
delim = " and "
list_of_conjuctions = [" and ", " but ", " yet ", " although ", " so "]

# below list will be the list containing the list of sentences are appearing in one line.
output_list = []
for i in source_sents:
    # temp = i.split(delim)
    temp = re.split('( and | but | yet | although | so )', i)
    output_list.append(temp)
# print(output_list)

# print("-----------------------------------------")


index = 0
for lst in output_list:                   # output_list is list of list
   temp = lst.copy()
   for item in lst:                       # lst is the list containing phrases and conjuctions of a sentences(line).
        for i in range(len(lst)-1):
            # print(f"the value of i:{i}")
            # print(lst[i])
            if lst[i] in list_of_conjuctions:
               pre_list = lst[i-1].split(" ")
               post_list = lst[i+1].split(" ")
               if(len(pre_list) >= 6 and len(post_list) >=6):
                  if(lst[i] in temp):
                     temp.remove(lst[i])
               else:
                  temp[i-1] = lst[i-1] + lst[i] + lst[i+1]
                  if(lst[i] in temp):
                     temp.remove(lst[i])
                  if(lst[i+1] in temp):
                     temp.remove(lst[i+1])
   # print(index, end=" ")
   output_list[index] = temp
   index+=1
   

# print(output_list)


# Save the translations to the a file
with open(output_file, "w+") as target:
  for line in output_list:
    for sent in line:
        # target.write(sent + "\n")
        if sent[-1] == '.':
            list_of_char = list(sent)
            list_of_char[0] = list_of_char[0].upper()
            # list_of_char[0] = ''
            sent = ''.join(list_of_char)
            target.write(sent + "\n")
        else:
            list_of_char = list(sent)
            # list_of_char[len(list_of_char)-1] = '.'
            list_of_char[0] = list_of_char[0].upper()
            if list_of_char[len(list_of_char)-1] == ',':
               list_of_char[len(list_of_char)-1] = ''
            sent = ''.join(list_of_char)  
            target.write(sent + ".\n")