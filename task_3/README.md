# Task 3
## Subtask 1
### Approach 
I start by identifying the proteins that do not reside in the same compartment, 
for the purpose of this task we will consider that proteins reside in one or the other cell compartment 
(biologically this is unlikely as some proteins can shuttle between cell compartments).
As theoretically any protein that is in compartment 1 can be a soft negative of any protein in compartment 2. 
I then compute all the different unique combinations (permutations) and then filter out the interactions that are in the `protein_interaction.txt` dataset.
### Result
Can be found in this csv: `result_task_3_subtask1.csv`.

## Subtask 2:
### Approach
I use the filtered unique combinations of two proteins that are not in the same compartment that we computed in the previous subtask. 
Then, I identify subgraphs for all proteins by determining all the connections of each protein using the Breadth First Search algorithm.
Finally, I filter out the soft negative connections that are part of the same subgraph.
### Result
Can be found in this csv: `result_task_3_subtask2.csv`.

## Running the script
The two subtasks can we answered with the same script, which can be run as follows:

```commandline
python <path_to_main>/main.py
```
The script should be run in a virtualenv created with the libraries in the `requirements.txt` file.

To run tests:
```commandline
python unit_tests/task_3/BFS_test.py
```
