## Measures of central tendency

First, import the Importing required libraries

import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
%matplotlib inline

Let’s show these by calculating the mean, median, and mode. Suppose we weight of luggage presented by airline passengers at the check-in (measured to the nearest kg):

# Define a list of numbers
data = [10, 12, 15, 17, 20, 20, 22, 25, 30, 35]

# Calculate the mean
mean = sum(data) / len(data)
print("Mean:", mean)

# Calculate the median
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]
print("Median:", median)

# Calculate the mode
c = Counter(data)
mode = c.most_common(1)[0][0]
print("Mode:", mode)

We could use numpy and scipy to compute these measures

import numpy as np
from scipy import stats

mean_=np.mean(data)
median_=np.median(data)
mode_=stats.mode(data)

print('mean',mean_,'median',median_,'mode',mode_)

## Your task

1- Ten patients at a doctor’s surgery wait for the following lengths of times to see their
doctor. What are the mean, median, and mode for these data?

Dataset= [5 mins, 20 mins, 28 mins, 2 mins, 5 mins,9 mins, 62 mins, 11mins, 16 mins, 5 mins]

Dataset=[5,20,28,2,5,9,62,11,16,5]

rata= np.mean(Dataset)
medi= np.median(Dataset)
modus= stats.mode(Dataset)
print(rata, medi,modus)

2- The "Datasaurus Dozen" dataset contains 13 datasets, each with a different shape but the same summary statistics. Import the `datasaurus.csv` using pandas as `df`.

Once you have imported the dataset, you can compute the mean for each dataset.

Measures of central tendency
First, import the Importing required libraries

import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import norm
import matplotlib.pyplot as plt
%matplotlib inline
Let’s show these by calculating the mean, median, and mode. Suppose we weight of luggage presented by airline passengers at the check-in (measured to the nearest kg):

# Define a list of numbers
data = [10, 12, 15, 17, 20, 20, 22, 25, 30, 35]
​
# Calculate the mean
mean = sum(data) / len(data)
print("Mean:", mean)
​
# Calculate the median
sorted_data = sorted(data)
n = len(sorted_data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]
print("Median:", median)
​
# Calculate the mode
c = Counter(data)
mode = c.most_common(1)[0][0]
print("Mode:", mode)
Mean: 20.6
Median: 20.0
Mode: 20
We could use numpy and scipy to compute these measures

import numpy as np
from scipy import stats
​
mean_=np.mean(data)
median_=np.median(data)
mode_=stats.mode(data)
​
print('mean',mean_,'median',median_,'mode',mode_)
mean 20.6 median 20.0 mode ModeResult(mode=array([20]), count=array([2]))
/tmp/ipykernel_14/649600169.py:6: FutureWarning: Unlike other reduction functions (e.g. `skew`, `kurtosis`), the default behavior of `mode` typically preserves the axis it acts along. In SciPy 1.11.0, this behavior will change: the default value of `keepdims` will become False, the `axis` over which the statistic is taken will be eliminated, and the value None will no longer be accepted. Set `keepdims` to True or False to avoid this warning.
  mode_=stats.mode(data)
Your task
1- Ten patients at a doctor’s surgery wait for the following lengths of times to see their doctor. What are the mean, median, and mode for these data?

Dataset= [5 mins, 20 mins, 28 mins, 2 mins, 5 mins,9 mins, 62 mins, 11mins, 16 mins, 5 mins]

Dataset=[5,20,28,2,5,9,62,11,16,5]
​
rata= np.mean(Dataset)
medi= np.median(Dataset)
modus= stats.mode(Dataset)
print(rata, medi,modus)
16.3 10.0 ModeResult(mode=array([5]), count=array([3]))
/tmp/ipykernel_14/3724809249.py:5: FutureWarning: Unlike other reduction functions (e.g. `skew`, `kurtosis`), the default behavior of `mode` typically preserves the axis it acts along. In SciPy 1.11.0, this behavior will change: the default value of `keepdims` will become False, the `axis` over which the statistic is taken will be eliminated, and the value None will no longer be accepted. Set `keepdims` to True or False to avoid this warning.
  modus= stats.mode(Dataset)
2- The "Datasaurus Dozen" dataset contains 13 datasets, each with a different shape but the same summary statistics. Import the datasaurus.csv using pandas as df.

Once you have imported the dataset, you can compute the mean for each dataset.

df=pd.read_csv("datasaurus.csv")
df.head()
dataset	x	y
0	dino	55.3846	97.1795
1	dino	51.5385	96.0256
2	dino	46.1538	94.4872
3	dino	42.8205	91.4103
4	dino	40.7692	88.3333
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1846 entries, 0 to 1845
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   dataset  1846 non-null   object 
 1   x        1846 non-null   float64
 2   y        1846 non-null   float64
dtypes: float64(2), object(1)
memory usage: 43.4+ KB
df.groupby('dataset').mean()
x	y
dataset		
away	54.266100	47.834721
bullseye	54.268730	47.830823
circle	54.267320	47.837717
dino	54.263273	47.832253
dots	54.260303	47.839829
h_lines	54.261442	47.830252
high_lines	54.268805	47.835450
slant_down	54.267849	47.835896
slant_up	54.265882	47.831496
star	54.267341	47.839545
v_lines	54.269927	47.836988
wide_lines	54.266916	47.831602
x_shape	54.260150	47.839717
​
sns.relplot(data=df, x='x', y='y', col='dataset', col_wrap=4);
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[15], line 1
----> 1 sns.relplot(data=df, x='x', y='y', col='dataset', col_wrap=4);

NameError: name 'sns' is not defined

3- For this task, we will explore a real-world dataset. Load the dataset flights.csv and store it in the variable flights, which contains over 300,000 observations of flights departing NYC in 2013.

We will focus on displaying a single variable, the arrival delay of flights in minutes

The flight arrival delays are in minutes and negative values mean the flight was early.

What are the mean, median, and mode for these data? Store them in f_mean, f_median, and f_mode.

flights= pd.read_csv('flights.csv')
flights.head()
Unnamed: 0	arr_delay	name
0	0	11.0	United Air Lines Inc.
1	1	20.0	United Air Lines Inc.
2	2	33.0	American Airlines Inc.
3	3	-18.0	JetBlue Airways
4	4	-25.0	Delta Air Lines Inc.
f_mean= flights['arr_delay'].mean() #np.mean(flights['arr_delay'])
f_median= np.median(flights['arr_delay'])  #flights['arr_delay'].median() 
f_mode= stats.mode(flights['arr_delay'])
f_mean
1.2971432896160044
f_median
-6.0
f_mode
​
Ellipsis
