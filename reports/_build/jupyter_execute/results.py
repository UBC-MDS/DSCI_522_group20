#!/usr/bin/env python
# coding: utf-8

# # Results
# 
# 

# For each subreddit-specific dataset of processed data we computed Wilcoxon rank-sum statistic (also referred to as the Mann-Whitney-Wilcoxon rank-sum), comparing the difference in median number of references to substance abuse per reddit-post in the 'pre-COVID' and 'post-COVID' datasets. In our test we employ Scipy stats packages' `ranksums` method {cite:p}`2020SciPy-NMeth`.
# 
# According to [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ranksums.html):
# > We can test the hypothesis that two independent unequal-sized samples are drawn from the same distribution with computing the Wilcoxon rank-sum statistic.
# 
# And according to [this ISIXSIGMA article](https://www.isixsigma.com/tools-templates/hypothesis-testing/making-sense-mann-whitney-test-median-comparison/)
# > The Mann-Whitney test compares the medians from two populations and works when the Y variable is continuous, discrete-ordinal or discrete-count, and the X variable is discrete with two attributes.
# 
# While this test may not exactly fit our use case for reasons unknown to us - we do not have any better guidance at this point as to choosing a more well-suited test for the purpose of measuring a statistically significant difference in medians between these two datasets.

# Using the Wilcoxon rank-sum test, we can set up our hypotheses for this test as follows:
# 
# $H_0:$ median number of references to substance abuse per reddit-post is the same in subreddit-specific 'pre-COVID' and 'post-COVID' datasets.
# 
# $H_a:$ median number of references to substance abuse per reddit-post is **not** the same in subreddit-specific 'pre-COVID' and 'post-COVID' datasets.

# In[1]:


import pandas as pd
import os
os.chdir('../analysis')
results = pd.read_csv('stat_tests/stat_tests.csv')
results.columns = ['subreddit_topic', 'test_statistic', 'p_value']
results


# Given we set a standard threshold $\alpha = 0.05$ for statistical significance, the conclusions we may be able to draw from these results are:
# - r/adhd and r/lonely saw a statistically significant difference between median number of references to substance abuse per reddit-post when comparing the 'pre-COVID' and 'post-COVID' datasets   
# - the remaining subreddits tested showed no statistically significant difference between median number of references to substance abuse per reddit-post when comparing the 'pre-COVID' and 'post-COVID' datasets.

# In[ ]:




