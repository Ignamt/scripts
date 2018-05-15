#! python2
'''
whitespaceRemover.py - This script goes to a folder and removes all the
    whitespace in the file names and folder names, replacing them with an "_".
'''

import shutil, os, re

#TODO: Create the Regex to get all whitespaces
whitespaceRegex = re.compile(r'\s+')

#TODO: Create a function that takes the name of the file/folder and returns the new
#new name if there is whitespace in it.
def removeWhitespace(path, filename):
    if " " in filename:
        oldPath = os.path.join(path, filename)
        newFilename = re.sub(r"\s", "_", filename)
        newPath = os.path.join(path, newFilename)
        #shutil.move(oldPath, newPath)
        print 'Renaming %s to %s.' %(oldPath, newPath)


#TODO: Loop through all the items in the specifiedfolder tree, applying the
#function to both folders and files
folderPath = r'C:\os.walk testing'
if os.path.exists(folderPath) and os.path.isabs(folderPath):
    for root, folders, files in os.walk(folderPath, topdown=False):
        print 'Scanning for whitespace in %s:' %root
        for filename in files:
            removeWhitespace(root, filename)
        for foldername in folders:
            removeWhitespace(root, foldername)

