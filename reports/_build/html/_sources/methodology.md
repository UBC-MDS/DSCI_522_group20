# Methodology

In order to investigate how substance use on Reddit has changed over the pandemic, we first introduce the dataset and then conduct an exploratory data analysis (eda) on several Reddit datasets which is described below.
## Data set

The datasets were obtained from [Reddit mental health dataset](https://zenodo.org/record/3941387#.YZl5BC1h1QL), a dataset processed and organised by Low et al {cite:p}`low2020natural`. They provide us with two CSV files, for each period (pre and post pandemic), for 15 different subreddits. 

Each observation is a Reddit user's post - a message written on a specific subreddit - which has been processed to extract features that are common in natural language processing.

### Feature details
|Feature|Description|
|---|---|
|author|author of the Reddit post|
|date|date of the Reddit post|
|post|raw post text|
|automated_readability_index|a readability metric for English text which measures the understandability of a text|
|coleman_liau_index|a readability metric for English text which measures the understandability of a text|
|flesch_kincaid_grade_level|a readability metric for English text which measures how difficult a piece of text is to understand|
|flesch_reading_ease|${\displaystyle 206.835-1.015\left({\frac {\text{total words}}{\text{total sentences}}}\right)-84.6\left({\frac {\text{total syllables}}{\text{total words}}}\right)}$|
|gulpease_index|a readability metric based on the length of words <br \> the number of words, and the length of sentences.|
|gunning_fog_index|a readability metric for English text which measures the understandability of a text|
|lix|a readability metric for English text which measures how difficult a piece of text is to understand|
|smog_index|a readability metric that measures how many years of education the average person needs to have to understand a text.|
|wiener_sachtextformel|a readability metric which measures the understandability of a text|
|n_chars|number of characters in post|
|n_long_words|number of long words in post|
|n_monosyllable_words|number of monosyllabic words in post|
|n_polysyllable_words|number of polysyllabic words in post|
|n_syllables|number of syllables in post|
|n_unique_words|number of unique words in post|
|n_words|number of words in post|
|sent_neg|negative sentiment score of post|
|sent_neu|neutral sentiment score of post|
|sent_pos|positive sentiment score of post|
|economic_stress_total|count of mentions of economic stress in post|
|isolation_total|count of mentions of isolation in post|
|substance_use_total|count of mentions of substance abuse in post|
|guns_total|count of mentions of guns in post|
|domestic_stress_total|count of mentions of domestic stress in post|
|suicidality_total|count of mentions of suicide in post|
|punctuation|count of punctuation in post|
|LIWC-based metrics|Linguistic Inquiry and Word Count - a metric derived from the degree to which various categories of words are used in a text|
|TF-IDF-based metrics| Term frequency–inverse document frequency - a statistic that is tries to reflect how important a word is in a piece of text|

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
