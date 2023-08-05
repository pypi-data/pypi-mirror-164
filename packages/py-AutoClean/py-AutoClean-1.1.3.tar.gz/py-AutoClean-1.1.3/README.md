# AutoClean - Automated Data Preprocessing & Cleaning
 
**AutoClean automates data preprocessing & cleaning for your next Data Science project in Python.**

Read more on the AutoClean algorithm in my **Medium** article [Automated Data Cleaning with Python](https://eliselandman.medium.com/automated-data-cleaning-with-python-94d44d854423).

View the AutoClean project on [GitHub](https://github.com/elisemercury/AutoClean).

---

## Description
It is commonly known among Data Scientists that data cleaning and preprocessing make up a major part of a data science project. And, you will probably agree with me that it is not the most exciting part of the project. **Wouldn't it be great if this part could be automated?**

AutoClean helps you exactly with that: it performs **preprocessing** and **cleaning** of data in Python in an **automated manner**, so that you can **save time** when working on your next project.

AutoClean supports:

* Handling of **duplicates** **[ NEW with version v1.1.0 ]**  
* Various imputation methods for **missing values**  
* Handling of **outliers**  
* **Encoding** of categorical data (OneHot, Label)  
* **Extraction** of datatime values  
* and more!

## Basic Usage

AutoClean takes a **Pandas dataframe as input** and has a built-in logic of how to **automatically** clean and process your data. You can let your dataset run through the default AutoClean pipeline by using:

```python
from AutoClean import AutoClean
pipeline = AutoClean(dataset)
```

The resulting output dataframe can be accessed by using:

```python
pipeline.output

> Output:
    col_1  col_2  ...  col_n
1   data   data   ...  data
2   data   data   ...  data
... ...    ...    ...  ...
```

## Adjustable Parameters

In some cases, the default settings of AutoClean might not optimally fit your data. Therefore it also supports **manual settings** so that you can adjust it to whatever processing steps you might need. 

It has the following adjustable parameters, for which the options and descriptions can be found below:

```python
AutoClean(dataset, mode='auto', duplicates=False, missing_num=False, missing_categ=False, 
          encode_categ=False, extract_datetime=False, outliers=False, outlier_param=1.5, 
          logfile=True, verbose=False)
```

| Parameter | Type | Default Value | Other Values |
| ------ | :---: | :---: | ------ | 
| **mode** | `str` | `'auto'` | `'manual'` |
| duplicates | `str` | `False` | `'auto'`, `True` |
| missing_num | `str` | `False` | `'auto'`, `'linreg'`, `'knn'`, `'mean'`, `'median'`, `'most_frequent'`, `'delete'`, `False` |
| missing_categ | `str` | `False` | `'auto'`, `'logreg'`, `'knn'`, `'most_frequent'`, `'delete'`, `False` |
| encode_categ | `list` | `False` | `'auto'`, `['onehot']`, `['label']`, `False` ; to encode only specific columns add a list of column names or indexes: `['auto', ['col1', 2]]` |
| extract_datetime | `str` | `False` | `'auto'`, `'D'`, `'M'`, `'Y'`, `'h'`, `'m'`, `'s'` |
| outliers | `str` | `False` | `'auto'`, `'winz'`, `'delete'`|
| outlier_param | `int`, `float` | `1.5` | any int or float, `False` |
| logfile | `bool` | `True` | `False` |
| verbose | `bool` | `False` | `True` |

By setting the `mode` parameter, you can define in which mode AutoClean will run:

* **Automated processing** (`mode` = `'auto'`): the data will be analyzed and cleaned automatically, by being passed through all the steps in the pipeline. All the parameters are set to = `'auto'`.
* **Manual processing** (`mode` = `'manual'`): you can manually define the processing steps that AutoClean will perform. All the parameters are set to `False`, except the ones that you define individually.

For example, you can choose to only handle outliers in your data, and skip all other processing steps by using:

```python
pipeline = AutoClean(dataset, mode='manual', outliers='auto')
```

---

**Please see the [AutoClean documentation on GitHub](https://github.com/elisemercury/AutoClean) for a detailed usage guide and descriptions of the parameters.**