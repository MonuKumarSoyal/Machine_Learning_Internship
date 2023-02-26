input_file = "breaker/source.txt"
output_file = "breaker/target.txt"

with open(input_file, "r") as source:
  lines = source.readlines()

source_sents = [line.strip() for line in lines]
# print(source_sents)
# initializing delim
delim = " and "

# below list will be the list containing the list of sentences are appearing in one line.
output_list = []
for i in source_sents:
    temp = i.split(delim)
    output_list.append(temp)
# print(output_list)


# Save the translations to the a file
with open(output_file, "w+") as target:
  for line in output_list:
    for sent in line:
        if sent[-1] == '.':
            target.write(sent + "\n")
        else:
            target.write(sent + ".\n")

