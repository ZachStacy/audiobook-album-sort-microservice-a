# audiobook-album-sort-microservice-a
# 
# Overview:
#     This microservices categorizes folders in a given directory based on specified conditions such as  
#     having subfolders in those directory folders that contain the word 'chapter' in the title or have  
#     mp3 files that are longer than 10 minutes long both being audiobooks.   
#     The client programmatically requests folder categorization by writing a directory path to input.txt.  
#     The server reads input.txt, processes the directory, and writes the categorization results to   
#     output.txt. 
# 
# Communication Contract:
#     REQUESTING:
#     To request data, instruct your program to write the target directory path to input.txt. The server
#     will read this file to identify the directory to categorize. An example:
#
#                 with open("input.txt, "w") as file:
#                   file.write("C:/path/to/directory")
#
#     The directory path should be the absolute path to the folder containing subfolders of audio files
#     you would like categorized.
#     
#     RECEIVING:
#     After processing, the microservice writes the results to output.txt. Each line in output.txt will
#     display a subfolder name and its category(Album or Audiobook).
#     In your program, read output.txt to receive data after processing. An example:
#                
#                  results = []
#                  with open("output.txt", "r") as file:
#                      lines = file.read().splitlines()  # Read all lines and remove newline characters
#                  
#                      for line in lines:
#                          # Split each line by ': ' to separate the album name and category
#                          folder_name, category = line.split(": ")
#                          results.append({"folder_name": folder_name, "category": category})
#
#     
#   Client                           Server
#      |                                |
#      |-- Write directory path to -->  |
#      |   input.txt as data request    |
#      |                                |
#      |                                |-- Read input.txt for directory path
#      |                                |
#      |                                |-- Categorize folders in specified directory
#      |                                |
#      |                                |-- Write categorization results to output.txt
#      |                                |
#      |<-- Send confirmation message --|
#      |                                |
#      |-- Read output.txt data       --|

