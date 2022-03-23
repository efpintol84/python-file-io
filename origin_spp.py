#! /usr/bin/env python3


import re

"A script to match specific patterns (words) in a text and print them and the number of lines where they appear" 


"""

First, I need to define the string pattern that I need to find in the origin.txt file" 

"""


re_pattern_string = r'((?:inherit|INHERIT|Inherit)(\w*))'


"""

Next, step: I open the file and seek line by line the term/s defined in the previous step

Requierements
_____________

1. It is important to use "with" when opening the document to ensure it will be closed when I
run and close the script.

2. I will generate an additional file (origin_spp.txt) where I will keep all the words that
I need.

"""

originmain_list = []
re_pattern_object = re.compile(re_pattern_string)
print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening origin_spp.txt')
    with open('origin_spp.txt', 'w') as out_stream:
        for num, line in enumerate (in_stream):
            temp_list = re_pattern_object.findall(line)
            for word in temp_list:
                out_stream.write(str(num) + '\t{0}\n'.format(word[0]))
                originmain_list.append((num, word[0]))


print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('origin_spp.txt is closed?', out_stream.closed)

if __name__ == '__main__':
    print(originmain_list)
