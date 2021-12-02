# author: Maeve Shi
#date: 2021-11-24

"""
This script performs exploratory data visualization on a given dataset

Usage: eda/eda_script.py --data_path=<dir> --outputfile=<outputfile>
Options:
--data_path=<dir>            the dir where preprocessed data is stored
--outputfile=<outputfile>         Specify the place to save the images.
"""

# import relevant modules
from datetime import date
import altair as alt
import glob

import numpy as np
import pandas as pd
from altair_saver import save
import os
import importlib.util
os.chdir('..') # this should always be '..' I think
spec = importlib.util.spec_from_file_location("docopt", "docopt.py")
docopt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docopt)

opt = docopt.docopt(__doc__)
alt.data_transformers.enable('data_server')
alt.renderers.enable('mimetype')

def main(data_path, outputfile):
    """
    calls visualization function to create charts and bars from the dataset
    and save them as png files at a specified location.
    -----
    data_path: str
        path of the input dataset
    outputfile: str
        path to save the output images
    Returns
    -----
    None
    """
    #creat path of the output img if the path doesn't exist
    if not os.path.exists(os.path.dirname(outputfile)):
        os.makedirs(os.path.dirname(outputfile))
    #load the data sets     
    preprocessed_data_files = [datafile.split('\\')[-1] for datafile in glob.glob(data_path + '/*.csv')] # '..\..\data\*.csv'
    files = [x for x in preprocessed_data_files]
    
    for i, file in enumerate(files):
        # analysis\preprocessing\*.csv
        df = pd.read_csv(file)
        #create output images name
        name = os.path.splitext(os.path.split(data_path+file)[1])[0]
        print(name)
        name_hist = name + '_histogram.png'
        name_line = name + '_line.png'
        #get the distribution of the target feature
        histograms(df, outputfile, name_hist)
        #get the time series plot of the target feature
        create_timeseries(df, outputfile, name_line)


def histograms(data, outputfile, name_hist):
    """
    create histograms of given features to obtain the distribution 
    to see the difference before and after the pandamic,
    then save the figure as png file to the outputfile location.
    -----
    data: pandas dataframe
    outputfile: str
      path to save the output images.
    Returns:
    -----
    None
    """
    #create histogram of given column/feature

    hist = (
        alt.Chart(data).mark_bar(opacity=0.8).encode(
            x=alt.X('substance_use_total', bin=alt.Bin(maxbins=30)),
            y='count()')
    )

    #save the file
    save(hist, outputfile + name_hist)

def create_timeseries(data, outputfile, name_line):
    """
    create time on the x axis and number of substance_use_total on the y-axis, 
    to see the trend over time, then save the figures as png file to the outputfile location.
    """
    #change column type to datetime, then extract month and year
    data['date'] =  pd.to_datetime(data['date'], format='%Y-%m-%d')
    data['month'] = data.date.dt.strftime('%m')
    data['year'] = data.date.dt.strftime('%Y')
    #concat the month and year
    data["time"] = data['year'] + data['month'] 
    #group by certain year and month, then sum up the substance use total
    month_substance = data.groupby(['time'])['substance_use_total'].sum().reset_index()

    line = (
         alt.Chart(month_substance).mark_line().encode(
            x = alt.X('time', title='Time'),
            y = alt.Y('substance_use_total', title='Substance Use Total'))


    )
    #save the file
    save(line, outputfile + name_line)


if __name__ == "__main__":
    main(opt["--data_path"], opt["--outputfile"])

