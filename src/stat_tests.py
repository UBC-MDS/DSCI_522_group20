# author: Luke Collins
# date: 2021-11-25

"""
This script runs preprocessed data through Wilcoxon rank-sum tests
for significance of difference of median substance_use_total
between 'pre' and 'post' datasets.

Usage: stat_tests.py --data_path=<dir> [--output=<file>]
Options:
--data_path=<dir>  path to dir in which preprocessed data is stored
--output=<file>    file to write csv output [default: './analysis/stat_tests/stat_tests_output.csv']
"""

import pandas as pd
from scipy.stats import ranksums
import glob
import importlib.util
import os
os.chdir('..') # this should always be '..' I think
spec = importlib.util.spec_from_file_location("docopt", "docopt.py")
docopt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docopt)

opt = docopt.docopt(__doc__)

def main(data_path, output_file):
    """
    Performs Wilcoxon rank-sum tests on pre/post data files
    -----
    data_path: str
        path to dir in which preprocessed data csvs are stored
    output_file: str
        path to dir in which csv output of stat tests will be written.
        default val is './stat_tests_output.csv'
    Returns
    -----
    None
    """
    # read the datasets
    # print(glob.glob(data_path + '/*.csv'))
    preprocessed_data_files = [datafile.split('\\')[-1] for datafile in glob.glob(data_path + '/*.csv')] # '..\..\data\*.csv'
    files = [x for x in preprocessed_data_files]

    results = {}
    for i, file in enumerate(files):
        # analysis\preprocessing\*.csv
        df = pd.read_csv(file)
        pre = df.loc[df['period'] == 'pre']['substance_use_total']
        post = df.loc[df['period'] == 'post']['substance_use_total']
        test_statistic, p_val = ranksums(pre, post, alternative='two-sided')
        results[file.split('_')[0]] = {'test_statistic': test_statistic,
                                                  'p_value': p_val}

    pd.DataFrame(results).T.to_csv(output_file)


if __name__ == "__main__":
    data_path = opt["--data_path"]
    output_file = opt["--output"]
    main(data_path, output_file)