# Tea-cluster-recommender
This personal project is a jupyter notebook file designed to web scrape data concerning tea leaves from my favorite shop.
It also includes data cleaning, clusterization via *scikit-learn* and a recommender to suggest similar teas based on the aroma profile.

![Recommender example GIF](https://github.com/CarlCharpin/Tea-cluster-recommender/blob/master/images/example.gif)

# Description

With this personal project, my aim was to get better at manipulating dataframes (*pandas*) and machine learning with *scikit-learn*. 
I figured real data was the best way to learn as it involves a lot of cleanup.
I also wanted to create someone that would be useful to me and maybe to others people as well, that's why I decided to 
build a recommender system for teas. With the diversity  available now, teas are more and more similar to wines or spirits, and it becomes harder to find new
products organically.


I started by scraping data about teas from a web shop using *BeautifulSoup4*. 
Once I gathered all the data I needed I used the dataframe for exploration and cleanup before moving on to
the clusterization with the kmeans algorithm. 
Another round of exploration allowed me to validate the model by checking how the teas were grouped.
The following images shows the resulting clusterization.

First the distribution of varieties of teas by cluster.
![Variety distribution by cluster](https://github.com/CarlCharpin/Tea-cluster-recommender/blob/master/images/groupedTea.png)

Also the distribution of aromas by cluster (presents the mean of every flavor by cluster)
![Aroma distribution](https://github.com/CarlCharpin/Tea-cluster-recommender/blob/master/images/distributionAromas.png)

Finally I programmed a recommender taking a tea from a list in input from the user and showing the most similar teas.
	
# Getting Started
## Technology
All this project was done with Python 3.7. Most of the project was done in jupyter notebooks then refactored in .py scripts.
## Dependencies
In this projet I used the following libraries:

* BeautifulSoup4
* numpy
* scipy
* numpy 
* pandas
* matplotlib
* seaborn
* sklearn (sklearn.cluster)
	
## Executing program

You can either run the notebook in the root folder or use the scripts in the scripts + data folder.
The notebook will start from scratch and scrape the data from the website. 
If you only want to get recommended teas, you can run the script *recommender.py*.


# Author
My name is Carl Charpin. I'm a physicist working towards a data scientist job.
	
# Acknowledgements
This project was inspired from the classification of whiskies you can find here.
[Classification of whiskies](https://blog.revolutionanalytics.com/2013/12/k-means-clustering-86-single-malt-scotch-whiskies.html)




