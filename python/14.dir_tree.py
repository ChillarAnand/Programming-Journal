#! /usr/bin/python

import os

rootDir = 'test/'

for dirName, subdirList, fileList in os.walk(rootDir):
#    print dirName, subdirList, fileList

    for fname in fileList:

        if '.pdf' in fname:
            #print('\t %s' % fname )

            dir_name = os.path.splitext(fname)[0]
            print dir_name
            os.system('pwd')
            command = "cp " + fname + " " + dir_name
            print command
            #os.system(command)
            
