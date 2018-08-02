Understanding Open Source Project Dynamics Using the GitHub Event Stream

1. Build D3.js visualizations of project activity over time and other features such as mean time to respond to issues, release frequency, etc. 2. Given a project, use machine learning to determine similar projects and show statistics about them. 3. Use sentiment analysis to determine which languages have projects with the happiest contributors, and predict any features of a bug report that elicit positive/negative responses. 4. Predict projects that are likely to grow over the next year.

Description of each file:

get_readmes.ipynb
-input: json files
-find popular repos (measured by number of star events for a particular time period) and get readme files for each of thos repos.

make_user_repo_matrix.ipynb
-input: json files
-output: csr matrix where (i,j) = 1 if user i starred repo j; list of users; list of repos
-output is based on the star events that occurred during the specified time period given in the input files. 
-example output files: user_repo_matrix.npz; user_list.csv; repo_list.csv

sentiment_analysis.ipynb
-input: json files
-output: csv file containing the following columns: repo_name, num_issue_comments, avg_sentiment
-output is based on the issue comments created during the specified time period in the input files. 
-since there are too many issue comments, we subsample the comments (e.g. analyze <=k comments only per repo). 
-example output file: sentiment.2018.7.16.15.csv

data_exploration_amy.ipynb
-random stuff for data exploration
