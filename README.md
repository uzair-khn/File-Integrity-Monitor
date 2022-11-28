# File-Integrity-Monitor
## Description:

Monitoring the files within the given directory. 
The Project is done in the Python Language. I use the PyCharm IDE for python.

## Requirements to run: 

Just make a new project on the PyCharm, and include all files and folders in the project mention above.
But to remember one thing, for preventing errors, install all the libraries imported in the main.py
Another thing to be mentionedis check the paths if routes to the right path of computer.

## How the project works:

### Option A: If baselines already exist, jump to option B. Otherwise,
          Make files named: file_baselne.txt  AND data_baseline.txt
              file_baseline.txt - contain all the hashes of the files present in the given directory.
              data_baseline.txt - contain all the hashes of each file data.

### Option B: After making the baselines files, want to monitor all the files in the given directory if these files 
          are modified, added or delete.
          It compares the fresh hashes with the baselines hashes, if not equal : 
              - alert and notify the user by display tthe message that the [abc_file] has been modified, added or deleted.
              - after that it pops up the window, to show all the records of the given directory.
             
## Future Modification: Some other aspects should be done like
                      - if modified, output the modified time also.
                      - if modified, output the user who changed it.
                      
## Output of the File Integrity Monitoring
![My Image](output/output1.png)
![My Image](output/output2.png)
![My Image](output/output3.png)
![My Image](output/output4.png)



