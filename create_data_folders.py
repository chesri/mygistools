#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     25/02/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re, os, sys

root_folder = r'C:\My Toolboxes\GitHub\mygistools\dependencies'
output_folder = r'C:\Temp\SOFPREP_FS'

for root, dirs, files in os.walk(root_folder):
    for f in files:
        print("\n FILE: {}".format(f))
        if f.endswith('.txt'):

            the_file = os.path.join(root,f)
            parent = 'Unknown'
            parent = [p for p in 'Charts', 'Elevation', 'Imagery', 'vector' if len(re.findall(p,f)) == 1][0]

            lol = list(line.strip() for line in open(the_file, 'rb'))

            breadcrumb = {}

            for rIndex,line in enumerate(lol):

                the_string = re.sub('[:|]', '', line)
                z = re.match("(^-+)(.*)",the_string)
                if z:
                    the_dashes = z.groups()[0]
                    the_word = z.groups()[1]
                    count = len(the_dashes)

                    breadcrumb[count] = the_word
                    for k in range(1,19,2):
                        if k > count:
                            breadcrumb.pop(k,None)

                    #path = [breadcrumb[i] for i in range(1,count + 1,2)] if count != 1 else [breadcrumb[1]]
                    path = []
                    if count != 1:
                        for i in range(1,count + 1, 2):
                            if i in breadcrumb:
                                path.append(breadcrumb[i])
                    else:
                        path.append(breadcrumb[1])

                    folder = os.path.join(output_folder,parent)

                    for p in path:

                        if p != '.':
                            if count == 1:
                                folder = os.path.join(folder, p.lstrip("-"))
                            else:
                                folder = os.path.join(folder, p.lstrip("-"))

                    if not os.path.exists(os.path.dirname(folder)):
                        os.mkdir(os.path.dirname(folder))
                    if not os.path.exists(folder):

                        os.mkdir(folder)

                    print("{}: {}".format(rIndex,folder))



