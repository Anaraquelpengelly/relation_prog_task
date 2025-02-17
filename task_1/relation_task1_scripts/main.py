import os, inspect
from typing import Optional

import pandas as pd
from pandas import DataFrame

from functions import utils
from tap import Tap

if __name__ == "__main__":

    class argparser_task1(Tap):
        path: str = os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
        """Task_1 folder path"""

    parser = argparser_task1(
        underscores_to_dashes=True, description="Get proteins containing pattern "
    )
    args = parser.parse_args()

    # args
    PATH = args.path
    PATTERN = r"T[AV]T.T"
    hu_proteins: Optional[DataFrame] = pd.read_csv(os.path.join(PATH, "human_proteins_clean.csv"),
                          sep=",", lineterminator='\n')
    # we first convert the sequence column to string:
    hu_proteins['sequence'] = hu_proteins['sequence'].astype('string')
    # apply the find_pattern function to the sequence column

    hu_proteins['pattern'] = hu_proteins['sequence'].apply(lambda x: utils.find_pattern(x, PATTERN))

    # check that the pattern is present in a few of the protein sequences:
    print(hu_proteins.pattern.value_counts())

    #select the proteins that have the pattern
    hu_proteins_with_pattern = hu_proteins[hu_proteins['pattern'] == True]

    #save the dataframe as csv to the same folder
    hu_proteins_with_pattern.drop(columns=["pattern", "Unnamed: 0"]).to_csv(os.path.join(PATH, "hu_proteins_with_pattern.csv"), index=False)
    print("file created!")


