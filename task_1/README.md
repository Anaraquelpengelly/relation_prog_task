# Task 1
## Corrupted file problem:
The problem here was there were two comas on line 972 of the `human_proteins_dirty.csv` file. 
The issue was solved by opening the file in vscode and manually going to line 972 and replacing the ",," with ",". 
The problem was due to the fact that csv is a comma separated file so the double comma was being interpreted as another column.

## Finding the regex pattern:
Steps to solve the problem:

* Find the regex pattern ["T-[AV]-T-*-T"]
* First create a function that will return 1 if the pattern is present or 0 if not
* Apply the function to create a new column in the data frame (called  find_pattern)
* Finally create a new csv `hu_proteins_with_pattern.csv` file with only the proteins containing the pattern.
The script can be run as follows:

To run the script:
```commandline
python main.py --path <path_to_human_proteins_dataset (clean)>
```
The script should be run in a virtualenv created with the libraries in the `requirements.txt` file.

To run tests:
```commandline
python test/find_pattern_test.py
```