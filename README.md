# BL-Capstone-1
# An exploration of health related data from the General Social Survey

### For this project I used data from the 2016 administration of the General Social Survey (GSS).  The GSS is one of the most influential studies in the social sciences.  The data collected in the survey includes demographic, financial, health, educational information and much more.   Something that makes this study so valuable is that it also includes respondents' opinions and beliefs on matters like government spending, the state of race relations, science, technology, and even philosophies about the nature of life.  For this capstone I set out to explore connections between overall health and other variables.

<br>

![GSS logo](/images/gss.jpg)
______________________________________
### **Hypotheses**

### Null:   Health **is not** related to feeling happy more often.
### Alternative:  Health **is** related to feeling happy more often.
______________________________________

###  A large amount of time was given to data wrangling and variable exploration.  Using only data from the 2016 administration of the survey, I created scales from respondents answers to be able to make some insightful calculations.  For example for a question like, "How often do you feel happy?" respondents could choose answers like, *"Almost never, Sometimes, A lot of the time, or Almost all the time."*  For that type of question I would convert those four answers to a number scale from 1-4.  Then, I moved on to creating some simple plots and the heatmap shown below to start visualizing the distributions and correlations of the variables.

<br>

![GSS logo](/images/resize_initial_vis.png)

![GSS logo](/images/resize_vis_hm.png)


______________________________________


### To keep my presentation within the given time limit and to be able to show something with a reasonable level of validity, I chose a set of three variables to compare from the 2016 survey:  Health, Time feeling happy, and Time feeling depressed.  
<br>

![GSS logo](/images/Health_hap_dep.png)


<br>

______________________________________



### Omitting the NaNs from the data to make more accurate calculations reduced my samples to the hundreds.  But there was still enough there for resampling with the bootstrap technique. Using 95% confidence intervals, I found that bootstrapping with 10,000 iterations produced normal distributions for each variable and the means of the bootstrapped samples aligned with the means of the original samples.  This was a good indication that the sample data was representative of the population at the time the data was collected in 2016.
<br>

![health ci](/images/health_ci.png)

<br>

![health ci](/images/felt_hap_ci.png)

<br>

![health hap ci](images/felt_dep_ci.png)

______________________________________


### Next, I bootstrapped the correlations between variables.  The bootstrapped correlation results suggested that what was shown by the sample data is a reasonably reliable representation of the relationships between health, feeling happy, and feeling depressed for the population of the United States in 2016.  As a result I was able to reject my null hypothesis and confidently say that there is a strong relationship between overall health and the time a person feels happy.

______________________________________


### In the future I'll revisit this important dataset with an expanded set of skills and a stronger understanding of how to pull out different variables.  The structure of this dataset did present some unique challenges at this point in my data science studies and I'm excited about further exploring the insight it has to offer. I want uncover more about what the GSS has to say about the ways people change over time and the reasons behind those changes.

<br><br>

![wayne](/images/Wayne.png)