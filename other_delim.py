import re

input_file = "breaker/source.txt"
output_file = "breaker/target.txt"

with open(input_file, "r") as source:
  lines = source.readlines()

source_sents = [line.strip() for line in lines]
# print(source_sents)
# initializing delim
delim = " and "
list_of_conjuctions = ["and", "but"]

# below list will be the list containing the list of sentences are appearing in one line.
output_list = []
for i in source_sents:
    # temp = i.split(delim)
    temp = re.split('( and | but )', i)
    output_list.append(temp)
print(output_list)

print("-----------------------------------------")

"""
Here i have to perform checking of the length of phrases
"""
index = 0
for lst in output_list:                   # output_list is list of list
   temp = lst
   for item in lst:                       # lst is the list containing phrases and conjuctions of a sentences(line).
        for i in range(len(lst)-1):
           if lst[i] in list_of_conjuctions:
              pre_list = lst[i-1].split(" ")
              post_list = lst[i+1].split(" ")
              if(len(pre_list) >= 6 and len(post_list) >=6):
                 temp.remove(lst[i])
              else:
                 temp[i-1] = lst[i-1] + lst[i] + lst[i+1]
                 temp.remove(lst[i])
                 temp.remove(lst[i+1])
   print(temp)
   output_list[index] = temp
   index+=1
   
    #   if item in list_of_conjuctions:
    #      lst.remove(item)    

print(output_list)


# Save the translations to the a file
with open(output_file, "w+") as target:
  for line in output_list:
    for sent in line:
        # target.write(sent + "\n")
        if sent[-1] == '.':
            # list_of_char = list(sent)
            # list_of_char[1] = list_of_char[1].upper()
            # list_of_char[0] = ''
            # sent = ''.join(list_of_char)
            target.write(sent + "\n")
        else:
            # list_of_char = list(sent)
            # list_of_char[len(list_of_char)-1] = '.'
            # sent = ''.join(list_of_char)  
            target.write(sent + "\n")