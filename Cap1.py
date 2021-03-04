import pandas as pd
import pyreadstat
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns


y16 = pd.read_spss('/Users/bn/Galvanize/Capstone/GSS2016.sav', usecols=[
    'RHLTHEND', 'CESD1', 'CESD3', 'TWITTER', 'FACEBOOK', 'USUALHRS',
    'INTWKDYH', 'NOGO',  'NEWS', 'TVHOURS', 'STRESSWK'])

df=y16.copy()

'''RHLTHEND TO health'''
df['RHLTHEND'] = df['RHLTHEND'].astype(str).str.upper()

def convert_to_scale(val):
    answers = {'NAN':-1,'POOR': 1, 'FAIR': 2, 'GOOD': 3, 'EXCELLENT':4}
    return answers.get(val)
df['health']=df['RHLTHEND'].map(convert_to_scale)



'''CESD1 TO felt_dep'''
df['CESD1'] = df['CESD1'].astype(str).str.lower()  

def convert_to_scale(val):
    answers = {'nan':-1,'none or almost none of the time': 1, 'some of the time': 2, 'most of the time': 3, 'all or almost all of the time':4}
    return answers.get(val)
df['felt_dep']=df['CESD1'].map(convert_to_scale)



'''CESD3 TO felt_hap'''
df['CESD3'] = df['CESD3'].astype(str).str.lower()  

def convert_to_scale(val):
    answers = {'nan':-1,'none or almost none of the time': 1, 'some of the time': 2, 'most of the time': 3, 'all or almost all of the time':4}
    return answers.get(val)
df['felt_hap']=df['CESD3'].map(convert_to_scale)



'''STRESSWK TO stress'''
df['STRESSWK'] = df['STRESSWK'].astype(str).str.lower() 

def convert_to_scale(val):
    answers = {'nan': -1,'Almost no stress at all': 1, 'Relatively little stress': 2, 'A moderate amount of stress': 3, 'A lot of stress':4}
    return answers.get(val)
df['work stress']=df['STRESSWK'].map(convert_to_scale)





df['health'] = df['health'].astype(float)
df['felt_dep'] = df['felt_dep'].astype(float)
df['felt_hap'] = df['felt_hap'].astype(float)



norm_df = df[["health","felt_dep", "felt_hap"]]




column_maxes = norm_df.max()
df_max = column_maxes.max()
normalized_df = norm_df / df_max


fig, axs = plt.subplots(figsize=(7,7))

lst = [normalized_df[normalized_df['health']>0]['health'], normalized_df[normalized_df['felt_hap']>0]['felt_hap'], 
       normalized_df[normalized_df['felt_dep']>0]['felt_dep']]


axs.hist(lst, histtype='bar', label=['Health', 'Time felt happy', 'Time felt depressed'], edgecolor='k')
axs.set_title('Health Ratings and Time Felt Happy/Depressed', size=15, color='navy')
axs.set_xlabel('Health rating and frequency of feelings', size=12)
axs.set_ylabel('Respondents', size=15)
axs.legend(prop={'size': 9})
plt.savefig('Health_hap_dep')
# plt.show()


def bootstrap(x, iterations=10000):

    lst = []
    for i in range(iterations):
        bootstrap = np.random.choice(x, size=len(x), replace=True)
        lst.append(bootstrap)
    return lst


def bootstrap_confidence_interval(sample, stat_function=np.mean, iterations=10000, ci=95):
    '''
    sample: Numpy array
        1-d numeric data
    
    stat_function: function, optional (default=np.mean)
        Function for calculating as sample statistic on data
    
    iterations: int, optional (default=1000)
        Number of bootstrap samples to create
    
    ci: int, optional (default=95)
        Percent of distribution encompassed by CI, 0<ci<100
    
    '''
    
    bootstrap_samples = bootstrap(sample, iterations=iterations)
    bootstrap_samples_stat = list(map(stat_function, bootstrap_samples))
    low_bound = (100. - ci) / 2
    high_bound = 100. - low_bound
    lower_ci, upper_ci = np.percentile(bootstrap_samples_stat,[low_bound, high_bound])
    return lower_ci, upper_ci, bootstrap_samples_stat



health_col = normalized_df[normalized_df['health']>0]['health']
hap_col = normalized_df[normalized_df['felt_hap']>0]['felt_hap']
dep_col = normalized_df[normalized_df['felt_dep']>0]['felt_dep']



health_ci = bootstrap_confidence_interval(health_col)


fig, ax = plt.subplots(figsize=(5,5))
ax.hist(health_ci[2], edgecolor='k', bins=20)
ax.axvline(health_ci[0], color='red')
ax.axvline(health_ci[1], color='red')
ax.set_title('Bootstrapped Means', size=20, color='navy')
ax.set_xlabel('Health rating', size=15)
ax.set_ylabel('Respondents', size=15)
# plt.savefig('health_ci')



felt_hap_ci = bootstrap_confidence_interval(hap_col)
fig, ax = plt.subplots(figsize=(5,5))
ax.hist(felt_hap_ci[2], edgecolor='k', bins=20)
ax.axvline(felt_hap_ci[0], color='red')
ax.axvline(felt_hap_ci[1], color='red')
ax.set_title('Bootstrapped Means', size=20, color='navy')
ax.set_xlabel('Time felt happy', size=15)
ax.set_ylabel('Respondents', size=15)
# plt.savefig('felt_hap_ci')



felt_dep_ci = bootstrap_confidence_interval(dep_col)
fig, ax = plt.subplots(figsize=(5,5))

ax.hist(felt_dep_ci[2], edgecolor='k', bins=20)
ax.axvline(felt_dep_ci[0], color='red')
ax.axvline(felt_dep_ci[1], color='red')
ax.set_title('Bootstrapped Means', size=20, color='navy')
ax.set_xlabel('Time felt depressed', size=15)
ax.set_ylabel('Respondents', size=15)
# plt.savefig('felt_dep_ci')






def bootstrap_correlation_confidence_interval(a, v, stat_function=np.corrcoef, iterations=10000, ci=95):
    '''
    sample: Numpy array
        1-d numeric data
    
    stat_function: function, optional (default=np.mean)
        Function for calculating as sample statistic on data
    
    iterations: int, optional (default=1000)
        Number of bootstrap samples to create
    
    ci: int, optional (default=95)
        Percent of distribution encompassed by CI, 0<ci<100
    
    '''
    
    sample1 = bootstrap(a, iterations=iterations)
    sample2 = bootstrap(v, iterations=iterations)
    bootstrap_samples_stat = list(map(stat_function, sample1, sample2))
    low_bound = (100. - ci) / 2
    high_bound = 100. - low_bound
    lower_ci, upper_ci = np.percentile(bootstrap_samples_stat,[low_bound, high_bound])
    return lower_ci, upper_ci, bootstrap_samples_stat


health_hap_corr=bootstrap_correlation_confidence_interval(df['health'],df['felt_hap'])
health_dep_corr=bootstrap_correlation_confidence_interval(df['health'],df['felt_hap'])

hap_corr = np.mean(health_hap_corr)
dep_corr = np.mean(health_dep_corr)