# ARAxai

<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/araxai">
<img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/araxai">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/araxai">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/araxai">

## What is ARA (ARAxai package)

ARAxai (association rule analysis) is a profiling tool that discovers main influencers in data. It can be also used to explain the model by simplification to outline most significant influencers.

It uses categorical data sets and search for most significal influencers. For them, deep dive is made by calling ara for this subset.

## Using most recent documentation

For most recetn version of documentation, please use [https://github.com/petrmasa/araxai](https://github.com/petrmasa/araxai).

## Installing ARAxai

Installation is simple. Simply run 

pip install araxai


## Running ARAxai

The key command to run data/model profiling is the

```
a = ara.ara(df=df,target='Severity',target_class='Fatal',options={"min_base":1})
a.print_result()
```

Parameters are

* **df** - dataframe with categorical data
* **target** - target variable
* **target_class** - class of target variable to find influencers for
* **options** - options( see below)


The complex example how to use the data is in following box. Please just copy accidents.zip file from the Github repository to folder with your code.

```
import os

from sklearn.impute import SimpleImputer
import pandas as pd
from araxai import ara

print(os.getcwd())

df = pd.read_csv (os.path.join(os.getcwd(),'accidents.zip'), encoding='cp1250', sep='\t')

df=df[['Driver_Age_Band','Driver_IMD','Sex','Journey','Hit_Objects_in','Hit_Objects_off','Casualties','Severity']]

imputer = SimpleImputer(strategy="most_frequent")
df = pd.DataFrame(imputer.fit_transform(df),columns = df.columns)

a = ara.arap(df,'Severity','Fatal',options={"min_base":1})

print(a)

a=a["results"]["rules"]

ara.print_result(res=a)
```


## ARA options

Currently there are several options available

* **min_base** - set minimum base for the rule
* **max_depth** - maximum depth of the deep dive


