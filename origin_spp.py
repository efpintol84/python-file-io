#! /usr/bin/env python3


import re

"A script to match specific patterns (words) in a text and print them and the number of lines where they appear" 

re_pattern_string = r'(?:inherit|INHERIT|Inherti)*\w'
re_pattern_object = re.compile(re_pattern_string)
#to_search = re_pattern_object.findall('origin.txt')

print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening origin_spp.txt')
    with open('origin_spp.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            inherit_list = line.split()
            origin_list = re_pattern_object.findall('inherit_list')
            origin_list = inherit_list.append('origin_list')
	    #print(origin_list)
            #inherit_list.sort()
            #for word in to_search:
               # out_stream.write('{0}\n'.format(word))

print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('origin_spp.txt is closed?', out_stream.closed)

if __name__ == '__main__':
    print (origin_list)
