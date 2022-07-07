# The TokenizerProd Tool is for tokenizing XML files
# created from cubes developed in the prod environment.
# This WILL NOT WORK for cubes from DEV!

# Customer inputs
customerShortname = input("Enter customer shortname: ")
cubeName = input("Enter cube name: ")
AC_DB_Server = input("Enter AC DB server name (Ex: EAGLE2005AE): ")
LNK_DB_Server = input("Enter LNK DB server name (Ex: Cardinal1010AE): ")
LM_DB_Server = input("Enter LM DB server name (Ex: 172.21.1.110): ")
EDW_DB_Server = input("Enter EDW DB server name (Ex: SuwPrdSQL01AE.m3.local): ")
cube_version =  input("Enter cube version (Ex: Standard or Advanced): ")
source_filename = input("Enter source filename (Ex: ZZ5_Cube_Advanced.xml): ")
source_location = input("Enter source location(Ex: /Users/burljohnson/Documents/M3Dev/SourceFolder/): ")
output_location = input("Enter output location(Ex: /Users/burljohnson/Documents/M3Dev/tokenizerFolder/): ")

# Create folder for tokenizer
from importlib.resources import read_binary, read_text
import os
from traceback import print_tb
#from this import s 
tokenizerFolder = output_location
if not os.path.exists(tokenizerFolder):
    os.makedirs(tokenizerFolder)

# Define source and target folder
src = source_location + source_filename
trg = tokenizerFolder
 
# Copy populated XML file to tokenizer folder
import shutil
shutil.copy(src, trg, follow_symlinks=True)


# Function to find the right text and replace with tokens
from pathlib2 import Path, PurePath
import string

# Opening the file using the Path function
file = Path(tokenizerFolder + source_filename)

# Reading and storing the content of the file in a data variable
data = file.read_text()

replace_text = {"a" + customerShortname + "XwAaCube" : 'a__TKNCubeName__XwAaCube',
                cubeName : "__TKNCubeName___Cube",
                "'" + customerShortname + "'" : "'__TKNCustomerShortName__'",
                'Database="' + customerShortname + "_" + customerShortname + '_acc" ' + 'Server="' + AC_DB_Server + '"' : 'Database="' +  '__TKNAccDB__" ' + 'Server="' + '__TKNAccDBServer__"',
                'Database="' + customerShortname + "_" + customerShortname + '_Acc" ' + 'Server="' + AC_DB_Server + '"' : 'Database="' +  '__TKNAccDB__" ' + 'Server="' + '__TKNAccDBServer__"',
                'Database="' + customerShortname + "_" + customerShortname + '_ACC" ' + 'Server="' + AC_DB_Server + '"' : 'Database="' +  '__TKNAccDB__" ' + 'Server="' + '__TKNAccDBServer__"',
                'Database="' + customerShortname + "_" + customerShortname + '_lnk" ' + 'Server="' + LNK_DB_Server + '"' : 'Database="' +  '__TKNLnkDB__" ' + 'Server="' + '__TKNLnkDBServer__"',
                'Database="' + customerShortname + "_" + customerShortname + '_Lnk" ' + 'Server="' + LNK_DB_Server + '"' : 'Database="' +  '__TKNLnkDB__" ' + 'Server="' + '__TKNLnkDBServer__"',
                'Database="' + customerShortname + "_" + customerShortname + '_LNK" ' + 'Server="' + LNK_DB_Server + '"' : 'Database="' +  '__TKNLnkDB__" ' + 'Server="' + '__TKNLnkDBServer__"',
                'Database="Skywalker_Beta" ' + 'Server="' + LM_DB_Server + '"' : 'Database="' +  '__TKNTimeDB__" ' + 'Server="' + '__TKNTimeDBServer__"',
                'Database="skywalker_Beta" ' + 'Server="' + LM_DB_Server + '"' : 'Database="' +  '__TKNTimeDB__" ' + 'Server="' + '__TKNTimeDBServer__"',
                'Database="M3_DataWarehouse" ' + 'Server="' + EDW_DB_Server + '"' : 'Database="' +  '__TKNDataWarehouseDB__" ' + 'Server="' + '__TKNDataWarehouseDBServer__"',
                'Database="M3_Datawarehouse" ' + 'Server="' + EDW_DB_Server + '"' : 'Database="' +  '__TKNDataWarehouseDB__" ' + 'Server="' + '__TKNDataWarehouseDBServer__"',
                "Server&quot;:&quot;" + AC_DB_Server + "&quot;" : "Server&quot;:&quot;" + "__TKNAccDBServer__" + "&quot;",
                "Database&quot;:&quot;" + customerShortname + "_" + customerShortname + "_acc&quot;" : "Database&quot;:&quot;" + '__TKNAccDB__' + "&quot;",
                "Database&quot;:&quot;" + customerShortname + "_" + customerShortname + "_Acc&quot;" : "Database&quot;:&quot;" + '__TKNAccDB__' + "&quot;",
                "Database&quot;:&quot;" + customerShortname + "_" + customerShortname + "_ACC&quot;" : "Database&quot;:&quot;" + '__TKNAccDB__' + "&quot;",
                "Server&quot;:&quot;" + LNK_DB_Server + "&quot;" : "Server&quot;:&quot;" + "__TKNLnkDBServer__" + "&quot;",
                "Database&quot;:&quot;" + customerShortname + "_" + customerShortname + "_lnk&quot;" : "Database&quot;:&quot;" + '__TKNLnkDB__' + "&quot;",
                "Database&quot;:&quot;" + customerShortname + "_" + customerShortname + "_Lnk&quot;" : "Database&quot;:&quot;" + '__TKNLnkDB__' + "&quot;",
                "Database&quot;:&quot;" + customerShortname + "_" + customerShortname + "_LNK&quot;" : "Database&quot;:&quot;" + '__TKNLnkDB__' + "&quot;",
                "Server&quot;:&quot;" + LM_DB_Server + "&quot;" : "Server&quot;:&quot;" + "__TKNTimeDBServer__" + "&quot;",
                "Database&quot;:&quot;Skywalker_Beta&quot;" : "Database&quot;:&quot;" + '__TKNTimeDB__' + "&quot;",
                "Database&quot;:&quot;skywalker_Beta&quot;" : "Database&quot;:&quot;" + '__TKNTimeDB__' + "&quot;",
                "Server&quot;:&quot;" + EDW_DB_Server + "&quot;" : "Server&quot;:&quot;" + "__TKNDataWarehouseDBServer__" + "&quot;",
                "Database&quot;:&quot;M3_DataWarehouse&quot;" : "Database&quot;:&quot;" + '__TKNDataWarehouseDB__' + "&quot;",
                "Database&quot;:&quot;M3_DataWarehouse&quot;" : "Database&quot;:&quot;" + '__TKNDataWarehouseDB__' + "&quot;"}


# Replacing the text using the replace function
for key, value in replace_text.items():
    data = data.replace(key,value)

# Writing the replaced data in the text file
file.write_text(data)

# Renaming new tokenized file
os.rename(tokenizerFolder + source_filename, tokenizerFolder + "M3_Cube_" + cube_version + ".xml")
ready_file = ( "M3_Cube_" + cube_version + ".xml")


# Error Checking
tokenized_file = Path(tokenizerFolder + ready_file)
error_check = ['a__TKNCubeName__XwAaCubeXwAa', '__TKNCubeName___Cube_', '_ACC','_Acc', '_acc,','lnk','Lnk', '_LNK', 'Skywalker','skywalker', 'M3_DataW','M3_Dataw']

def search_multiple_strings_in_file(tokenized_file, error_check):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(tokenized_file, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in error_check:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search, line_number, line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results        

# search for given strings in the tokenized file
matched_lines = search_multiple_strings_in_file(tokenized_file, error_check)
print('Total Matched lines : ', len(matched_lines))
for elem in matched_lines:
    print('Error: Variable not tokenized. Check XML for changes. = ', elem[0], ' :: Line Number = ', elem[1])

# Human readable output for error or success
if len(matched_lines) == 0:
        print(
        '''
        *************************************
        '''
        + ready_file + ' is ready!!!!!!!!!'
        '''
        *************************************
        ''')
elif len(matched_lines) > 0:
        print(
        '''
        *************************************
        '''
        'Errors listed above! You have variables that are not tokenized. Please check the Tokenizer for changes.'
        '''
        *************************************
        ''')


                    
  


