# BL-Capstone-1
# Capstone 1 Presentation

### For this capstone I used data from the General Social Survey (GSS).  The GSS is one of the most influential studies in the social sciences.  The data collected in the survey includes demographic, financial, health and educational information.   It also includes respondents' opinions and beliefs on matters like government spending, the state of race relations, science, technology, and even philosophies about the nature of life.  It's an awesome dataset.

<br>

![GSS logo](/images/gss.jpg)
______________________________________

<br>

###  I wanted to use variables from the years 2016 and 2018 which I downloaded in two separate dataframes.  Each dataframe had about 2500 rows and about 10 columns.  I found that when I merged them into one dataframe there were millions of rows which didn't seem right.  After some zigzagging around issues of different datatypes and a massive amount of NaNs, I eventually discovered that the study design and execution was a little different from my initial understanding which may have been the reason that was happening.
<br>

### I created scales from respondents answers to be able to work with the numbers.  For example take a question like, "How often do you feel happy?" The choices respondents could choose might be something like *Almost never, Sometimes, A lot of the time, or Almost all the time.*  For that question I would convert those four answers to a number scale from 1-4.

<br>

### First I replaced the NaNs with the means of their columns which seemed like a perfect way to handle the NaNs.  However, when I made some plots like the ones below to start visualizing the distributions for myself, all those means were going to make calculations less accurate.  So I decided to omit the NaNs from the calculations instead of replacing them with the means.

<br>




![GSS logo](/images/resize_initial_vis.png)

![GSS logo](/images/resize_vis_hm.png)


______________________________________


### I normalized the data because the scales were different in different columns.  To keep this capstone presentation within the given time limit and to be able to show something with a reasonable level of validity, I chose a small set of three variables to compare from the 2016 dataframe:  Health, Time feeling happy, and Time feeling depressed.
<br>

![GSS logo](/images/Health_hap_dep.png)


<br>

______________________________________

### **Hypothesis**

### Null:   Health **is not** affected by feeling happy more often.
### Alternative:  Health **is** affected by feeling happy more often.
______________________________________


### Omitting the NaNs reduced the sample sizes to the hundreds but there was still enough for resampling with the bootstrap technique. 

### Using 95% confidence intervals, I found that bootstrapping with 10,000 iterations produced normal distributions for each variable and the means of the bootstrapped samples aligned with the means of the original samples.
<br>

![health ci](/images/health_ci.png)

<br>

![health ci](/images/felt_hap_ci.png)

<br>

![health hap ci](images/felt_dep_ci.png)

______________________________________


### Next, I wrote a function to bootstrap the correlations of the samples.  The bootstrapped correlation results suggest that what was shown in the first graph of the original samples is a reasonably reliable representation of the relationships between health, feeling happy, and feeling depressed.  Based on the correlations I was able to reject my null hypothesis.

______________________________________


<br><br>

### Navigating the GSS codebook to find and pull variables was complicated and with more time an even better tuned set of variables could be selected. In the future I will revisit this dataset with an expanded set of skills and a better knowledge of how to get the data I want from it.  I want explore what the GSS has to say about the ways people change over time and the reasons behind those changes.

<br><br>

![wayne](/images/Wayne.png)