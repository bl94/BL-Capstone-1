# An exploration of health and happiness data from the General Social Survey

## Capstone 1 for the Galvanize Data Science Immersive

## Technologies Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Scikit-Learn

## Introduction
#### The GSS is one of the most influential studies in the social sciences.  Respondents are interviewed in person for about 90 minutes and the information collected includes demographic, health, financial, educational data and much more.  Something that makes this study so valuable is that it also includes respondents' opinions and beliefs on matters like government spending, the state of race relations, science, technology, and even philosophies about the nature of life.  For this project I set out to explore connections between overall health and other variables from the 2016 administration of the survey.

## Summary
#### The purpose of this project was really just to perform some basic exploratory data analysis.  The GSS dataset has thousands of features and I didn't have much time to go through them all to find the best variables to compare.  This was a challenging dataset to work with at this point in my data science studies for several reasons but I didn't want to work with something too easy.

#### After choosing some variables to compare I started by creating some plots to get an idea of the distribution of each variable.  I also created a heatmap to get an overview of their correlations.  To present something reasonably valid in the short time I had available to complete this project, a simple hypothesis and set of three significantly correlated variables were chosen to compare from the 2016 survey:  health, time feeling happy, and time feeling depressed.  I made a plot to show the distributions of those variables alongside eachother to help illustrate their relationship to eachother.  After that, I used bootstrapping to confirm that the sample data could be used to represent the population and plotted the results.  Finally, I also bootstrapped the correlations to more confidently reject my null hypothesis.

## Exploratory Data Analysis
####  The graphs and correlation heatmap below represent the distrubutions and correlations of data from survey reponses.  For a question like, "How often do you feel happy?" respondents could choose answers like, *"Almost never, Sometimes, A lot of the time, or Almost all the time,"* and those answers were converted to a number scale.

##### Distribution of each feature after replacing NaNs with the mean of the feature.
![GSS logo](/images/resize_initial_vis.png)

##### Correlation heatmap.
![GSS logo](/images/resize_vis_hm.png)

## Hypotheses
#### Hypotheses were created based on the strongest correlations found in the data.
#### Null:   Health *is not* related to feeling happy more often.
#### Alternative:  Health *is* related to feeling happy more often.

##### Graph showing the distributions of responses to health and frequency of feelings questions.

![GSS logo](/images/Health_hap_dep.png)


## Bootstrapping
#### Using 95% confidence intervals I found that bootstrapping with 10,000 iterations produced normal distributions for each variable and the means of the bootstrapped samples aligned with the means of the original samples.  This is a good indication that the sample data was representative of the population at the time the data was collected in 2016.

![health ci](/images/health_ci.png)

<br>

![health ci](/images/felt_hap_ci.png)

<br>

![health hap ci](images/felt_dep_ci.png)


#### Correlations between the variables were also bootstrapped and results showed that the data is a reasonably reliable representation of the relationships between health, feeling happy, and feeling depressed for the population of the United States in 2016.  As a result we are able to reject the null hypothesis and confidently say there is a strong relationship between overall health and the time a person feels happy.  This may be because being healthy results in being happier and/or because feeling happy contributes to better health.

<br>

## Future Improvements

#### In the future I'll revisit this important dataset with an expanded set of skills and the knowledge and time required to pull out a larger, better set of variables.  The structure of this dataset did present some unique challenges at this point in my data science studies and I'm excited about returning to it to explore the insight it has to offer. I want uncover more about what the General Social Survey has to say about the ways people change over time and the reasons behind those changes.

![wayne](/images/Wayne.png)
