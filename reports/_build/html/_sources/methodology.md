# Methodology

In order to investigate how substance use on Reddit has changed over the pandemic, we first introduce the dataset and then conduct an exploratory data analysis (eda) on several Reddit datasets which is described below.
## Data set

The datasets were obtained from [Reddit mental health dataset](https://zenodo.org/record/3941387#.YZl5BC1h1QL), a dataset processed and organised by Low et al {cite:p}`low2020natural`. They provide us with two CSV files, for each period (pre and post pandemic), for 15 different subreddits. 

Each observation is a Reddit user's post - a message written on a specific subreddit - which has been processed to extract features that are common in natural language processing.

The feature extractions are as follows (n is the number of columns):
- LIWC (n=62);
- sentiment analysis (n=4); 
- basic word and syllable counts (n=8); 
- punctuation (n=1); 
- readability metrics (n=9); 
- term frequency–inverse document frequency (TF-IDF) ngrams (256-1024) to capture words and phrases that characterize specific posts; 
- manually built lexicons about suicidality (n=1), economic stress (n=1), isolation (n=1), substance use (n=1), domestic stress (n=1), and guns (n=1). 

Alongside these features include:
- author (Reddit user name)
- date
- post
## Data cleaning/transformation

In order to answer the question "How has the substance use increased over the pandemic?", the feature `substance_use_total` is selected as the target feature, and the data is cleaned to focus exclusively on this feature.

The Python programming language {cite:p}`pypi` and the Pandas library {cite:p}`pandas` were used to perform the data cleaning process.
### Data Cleaning Steps
- Combine the `pre` and `post` datasets into one dataset. 
- Filter the dataset to keep only the columns of interest, including `subreddit`, `author`, `date`, `post`, and `substance_use_total`.
### Feature Engineering
- We apply a simple method by adding a new feature `period` to indicate the timeframe of the posts (before or after the pandemic). This helps to represent the data better and to compare the timeframes more easily in later parts of this report. 
### Room for improvement
- It is noted that in our `process_raw.py` script, we used the `try-except` block to make the script runnable. The reason behind is to allow the script to load all files except for files with extension `.DS_Store`.  The `.DS_Store` files are automatically created by Mac OS X Finder in browsed directories.
- In case more time to work on this is given, we expect to enhance the `process_raw.py` script without using the `try-except` block.
