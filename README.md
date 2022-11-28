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
![output1](https://user-images.githubusercontent.com/119037668/204262331-a4ba60c0-6efe-444d-8771-91df75ccccef.PNG)
![output2](https://user-images.githubusercontent.com/119037668/204262378-538b8bfb-a844-4bd2-8d34-3c6ed59209a8.PNG)
![output3](https://user-images.githubusercontent.com/119037668/204262385-d2540c2a-007b-48f4-b160-9861babb606c.PNG)
![output4](https://user-images.githubusercontent.com/119037668/204262386-529760f6-dbc7-4134-9a30-d33914dfbcd3.PNG)
![output8](https://user-images.githubusercontent.com/119037668/204262396-d109831a-678a-4ffa-9b30-ee6fe3a43d1b.PNG)
![output5](https://user-images.githubusercontent.com/119037668/204262389-c405e730-a60e-4df3-811a-c348c90887e1.PNG)
![output6](https://user-images.githubusercontent.com/119037668/204262391-b322d556-1747-45a5-8a17-993fc90eda8c.PNG)
![output7](https://user-images.githubusercontent.com/119037668/204262394-c0f30ebf-50b9-444a-83a6-92a110488917.PNG)


