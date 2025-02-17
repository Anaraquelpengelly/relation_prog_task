import os, inspect
import itertools

import pandas as pd

from functions import utils
from tap import Tap

if __name__ == "__main__":

    class argparser_task3(Tap):
        path: str = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
        """Task_3 folder path"""

    parser = argparser_task3(
        underscores_to_dashes=True, description="Get proteins containing pattern "
    )
    args = parser.parse_args()

    # args
    PATH = args.path
    # SUBTASK 1
    # read the datasets:
    protein_compartments = pd.read_csv(os.path.join(PATH, "protein_compartments.csv"))
    proteins = pd.read_csv(os.path.join(PATH, "proteins.txt"), sep="\t", header=None)
    protein_inter = pd.read_csv(os.path.join(PATH, "protein_interactions.txt"), sep="\t", header=None)

    # Identify proteins that don't reside in the same compartment:
    proteins_c1 = list(protein_compartments[protein_compartments['compartment_id'] == 1]['protein_id'])
    proteins_c2 = list(protein_compartments[protein_compartments['compartment_id'] == 2]['protein_id'])

    #get all possible combinations without repetition
    soft_negatives = [(x, y) for x in proteins_c1 for y in proteins_c2]

    # Extract the pairs in the interactions file to filter them out
    protein_inter_tup = list(protein_inter.apply(lambda x: tuple(x[0].split(" ")), axis=1))

    #filter interactions out from the soft negative list:
    filtered_soft_neg = [t for t in soft_negatives if t not in protein_inter_tup]
    assert len(filtered_soft_neg) <= len(soft_negatives)

    #save the filtered soft_neg in a csv file
    utils.save_csv(filtered_soft_neg, 'soft_negative', 'result_task_3_subtask1.csv', PATH)

    # SUBTASK 2
    # I will use the filtered unique combinations of two proteins that are not in the same compartment (filtered_soft_neg) that we computed in the previous subtask.
    # As for the subgraph identification I will first determine all the connections of each protein. using the Breadth first search algorithm.

    # for this I first create a dictionary of all interacting proteins per protein
    interaction_dic = {}
    for protein in list(proteins[0]):
        interactions = []
        for t in protein_inter_tup:
            if t[0] == protein or t[1] == protein:
                t = list(t)
                t.remove(protein)
                interactions.append(list(t))
        interaction_dic[protein] = list(itertools.chain(*interactions))


    # Get subgraphs for all proteins
    subgraph_dic = {p: utils.bfs(interaction_dic, p) for p in list(proteins[0])}

    #now remove the soft negatives that are in the same subgraph:
    ##we first convert the tuples to lists to access indexes:
    results_1 = [list(item) for item in filtered_soft_neg]
    results_2 = [tuple(l) for l in results_1 if l[1] not in subgraph_dic[l[0]]]
    assert len(results_2) <= len(results_1)

    #save the re-filtered soft negative interactions:
    utils.save_csv(results_2, 'soft_negative', 'result_task_3_subtask2.csv', PATH)


