import re
import pandas as pd
import xlsxwriter

input_file = pd.read_excel("input.xlsx")
header = input_file.columns
# print(header)

hindi_sents = [line.strip() for line in input_file[header[0]]]
english_sents = [line.strip() for line in input_file[header[1]]]
# print(hindi_sents)


# initializing delimiters
list_of_hindi_conjunctions = [" और ", ", ", "।"]
list_of_eng_conjunctions = [" and ", ", ", "."]

# below list will be the list containing the list of sentences are appearing in one line.
output_hindi_list = []
for i in hindi_sents:
    # temp = i.split(delim)
    temp = re.split('( और |, |।)', i)
    output_hindi_list.append(temp)
# print(output_hindi_list)

output_eng_list = []
for i in english_sents:
    # temp = i.split(delim)
    temp = re.split('( and |, |\.)', i)
    output_eng_list.append(temp)
# print(output_eng_list)




sent = 0
for lst in output_hindi_list:                   # output_hindi_list is list of list
  temp = lst.copy()                      # lst is the list containing phrases and conjunctions of a sentences(line)
  index = 0
  while(index!=len(temp)):
     if temp[index] in list_of_hindi_conjunctions:
        temp.pop(index)
        index-=1
     index+=1
  # print(temp)
  output_hindi_list[sent] = temp
  sent+=1


sent = 0
for lst in output_eng_list:                   # output_eng_list is list of list
  temp = lst.copy()                      # lst is the list containing phrases and conjunctions of a sentences(line)
  index = 0
  while(index!=len(temp)):
     if temp[index] in list_of_eng_conjunctions:
        temp.pop(index)
        index-=1
     index+=1
  # print(temp)
  output_eng_list[sent] = temp
  sent+=1
           

row = 0
column = 0

output_file = xlsxwriter.Workbook('output.xlsx')
worksheet = output_file.add_worksheet()

for line in output_hindi_list:
  for sent in line:
    worksheet.write(row, column, sent)
    row+=1

row = 0
column = 1


for line in output_eng_list:
  for sent in line:
    worksheet.write(row, column, sent)
    row+=1

output_file.close()






