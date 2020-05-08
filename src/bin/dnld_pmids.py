#!/usr/bin/env python3
"""Given a user query, query PubMed and return PMIDs. Then run NIH's iCite on the PMIDs"""

import sys
from pmidcite.pubmedqueryicite import PubMedQueryToICite


def main(force_dnld=False):
    """Download PMIDs returned from user queries"""
    obj = PubMedQueryToICite(force_dnld)
    # Write to: ./log/pmids and ./log/icite
    obj.querypubmed_runicite('Orcinus_Orca_Type_D.txt', 'Orcinus Orca Type D')


if __name__ == '__main__':
    main(len(sys.argv) != 1)
