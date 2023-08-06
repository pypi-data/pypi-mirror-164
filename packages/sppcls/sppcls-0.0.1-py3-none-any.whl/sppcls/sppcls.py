#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# A module to access data from the DFG-funded SPP Computational Literary Studies
#
# Usage:
# import cls
# df = cls.DataFrame("judenbuche", ["events", "keypassages"])
#
# Author: rja
#
# Changes:
# 2022-08-25 (rja)
# - initial version

import pandas as pd

# default repository URL
SPP_CLS_GITLAB = "https://cls-gitlab.phil.uni-wuerzburg.de/spp-cls-data-exchange/spp-cls_annotationtables_data/-/raw/main/"


# consider subclassing pd.DataFrame, cf.
# https://pandas.pydata.org/pandas-docs/stable/development/extending.html#extending-subclassing-pandas
def DataFrame(work, projects, repository=SPP_CLS_GITLAB):
    """Generates a dataframe with the data of the projects for work."""
    dataframes = [_download(repository, work, project) for project in projects]
    # FIXME: use pd.merge()
    return pd.concat(dataframes, axis=1)


def _download(repository, work, project):
    # FIXME: add proper URL escaping
    url = repository + work + "/" + project + ".tsv"
    return pd.read_csv(url, sep='\t')


if __name__ == '__main__':
    pass
