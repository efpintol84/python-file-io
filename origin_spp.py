#! /usr/bin/env python3





print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening origin_spp.txt')
    with open('origin_spp.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            inherit_list = line.split()
            inherit_list.sort()
            for word in inherit_list:
                out_stream.write('{0}\n'.format(word))
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('origin_spp.txt is closed?', out_stream.closed)
