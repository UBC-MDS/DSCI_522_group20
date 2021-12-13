# Conclusion

We conducted a statistical analysis on data gathered from multiple subreddits to answer an inferential question on whether the number of substance abuse references increased during the 2020 COVID-19 pandemic on Reddit.

We discuss limitations of our analysis in our [results](results.md) and include an examination of our datasets in the [data analysis](data_analysis.md).

The hypothesis tests for each subreddit are presented in a [table](results.md) and shows the different subreddits along with the p-values. p-values less than 0.05 indicate that there is statistical evidence that the median number of references to substance abuse has changed post-COVID.

We conclude that only two subreddits, r/adhd and r/lonely show statistically siginificant difference. Accordingly, we reject the null hypothesis in favour of the alternative hypothesis - that in these subreddits, the median number of references to substance abuse per reddit-post has changed between 'pre-COVID' and 'post-COVID'.
## Further work
Note that we did not explicitly comment on whether the median is significantly less or more than pre-COVID times. It would be interesting to compare and plot how each subreddit has changed to visually show the results.

Additionally there are numerous other questions that we could have asked with this dataset, namely questions that involve text sentiment:
- Analyse which words/sentiments are most-associated with particular subreddits dedicated to particular health concerns;
- Identify whether those who self-identify with particular illnesses choose particular language to express their feelings/symptoms, or whether there are common terms across self-described mental health groups;
- How can we flag users that are in need of urgent attention and care based on their comments;
- Can we apply what we've learned from the mental-health-specific subreddits and see if we can identify related behaviour/sentiments in the non-mental-health subreddits (i.e. do people in r/divorce use some of the same language as those in r/depression).