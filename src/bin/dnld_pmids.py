#!/usr/bin/env python3
"""Given a user query, query PubMed and return PMIDs. Then run NIH's iCite on the PMIDs"""

import sys
from pmidcite.pubmedqueryicite import PubMedQueryToICite


def main():
    """Download PMIDs returned for a PubMed query. Write an iCite report for each PMID"""
    # pylint: disable=bad-whitespace
    queries = [
        # Output filenames          PubMed query
        # -----------------         -----------------------------------
        ('Orcinus_Orca.txt',        'Orcinus Orca'),
        ('Orcinus_Orca_Type_D.txt', 'Orcinus Orca Type D'),
    ]

    # By default, only the last entry in the list is run.
    # This allows you to build a history of searches,
    # but not run all of them every time.
    #
    # To re-run all entries in the list:
    #   $ src/bin/dnld_pmids.py all
    #
    # To run the first query:
    #   $ src/bin/dnld_pmids.py 0
    #
    # To run the second to last query:
    #   $ src/bin/dnld_pmids.py -2
    #
    obj = PubMedQueryToICite(force_dnld=True, prt_icitepy=None)
    dnld_idx = obj.get_index(sys.argv)
    obj.run(queries, dnld_idx)


if __name__ == '__main__':
    main()
