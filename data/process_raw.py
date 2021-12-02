# author: Nobby Nguyen
# date: 2021-11-24

"""Load a csv data file from a local input file and split into test and training data set and write to 2 separate local output files. 
Usage: process_raw.py --in_dir=<in_dir> --out_dir=<out_dir> 

Options:
--in_dir=<in_dir>                        The path where we want to load from
--out_dir=<out_dir>    The path and the filename and the extension where we want to save the cleaning data file in our disk

"""

import os
import pandas as pd
import importlib.util

os.chdir('..') # this should always be '..' I think
spec = importlib.util.spec_from_file_location("docopt", "docopt.py")
docopt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docopt)

opt = docopt.docopt(__doc__)

def main(in_dir, out_dir):
    print("Start data cleaning script")
    
    list_of_files = []
    for f in os.listdir(in_dir):
        if f[-3:] == "csv":
            list_of_files.append(f)
    
    
    # Step 1: Read in the data

    for file in list_of_files:
        formated_path = in_dir + file
        input_df= pd.read_csv(formated_path)
        
    # Step 2: Read the pre and post data
    
    datasets ={'%s %s' % (file.split('_')[0], file.split('_')[1]): i for i, file in enumerate(list_of_files)}

    topics = {topic.split('_')[0] for topic in list_of_files}

    for topic in topics:
        try:
            files_to_load = [list_of_files[i] for i in [datasets[value] for value in datasets if topic in value]]
            post_data = pd.read_csv(in_dir + files_to_load[0])
            pre_data = pd.read_csv(in_dir + files_to_load[1])

            # Step 3: Combining the pre and post into one dataset
            pre_data['period'] = 'pre'
            post_data['period'] = 'post'

            subreddit_df = pd.concat([pre_data, post_data])

            # Step 4: Filter the columns of interest
            columns_of_interest = ['subreddit', 'author', 'date', 'post', 'substance_use_total', 'period']
            out_cleaning_file = subreddit_df.loc[:, columns_of_interest]
            out_cleaning_file.to_csv(out_dir + topic + '_processed.csv')
        except:
            print('failed to load files relating to ', topic)
            pass

if __name__ == "__main__":
    in_dir = opt["--in_dir"]
    out_dir = opt["--out_dir"]
    main(in_dir, out_dir)

