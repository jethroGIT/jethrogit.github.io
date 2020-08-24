---
layout: post
title: Creating a One-Hot Encoding in PyTorch
category: Machine-Learning
lang: EN
description: One-hot encoding in PyTorch
sticky: false
---

This article explains how to create a_one-hot encoding_ of categorical values using PyTorch library. The idea of this post is inspired by "[_Deep Learning with PyTorch_](https://www.manning.com/books/deep-learning-with-pytorch?query=deep%20lea)" by Eli Stevens, Luca Antiga, and Thomas Viehmann.     

Sooner or later every data scientist meets categorical values in one's dataset. For example, the size of a t-shirt (_small_ (S), _medium_ (M), _large_ (L), and  _extra large_ (XL)) has four categorical values. Therefore, the problem formulation of this post will be 

> How do we encode these categorical values before we feed them into Machine Learning algorithms?  
    
Suppose that we have installed [**PyTorch**](https://pytorch.org) in our machine and as an example, we use the [_train set_](https://maranathaedu-my.sharepoint.com/:x:/g/personal/hendra_bunyamin_it_maranatha_edu/ERfx1C28MeFEuKuNY1ptbKMBEjOFOwxaqfnQIeXYyOF9ww?e=BSnKsb) of Titanic dataset.    

[![img1]({{ site.baseurl }}/assets/images/Titanic-Sinking.jpg){:class="img-responsive"}]({{ site.baseurl }}/assets/images/Titanic-Sinking.jpg)*<center>The RMS Titanic sank in the North Atlantic Ocean in the early morning hours of 15 April 1912. Image taken from <a href="https://www.greenscene.co.id/2020/06/25/7-kejadian-nyata-di-titanic-yang-berbeda-dengan-filmnya/">Greenscene</a>, some rights reserved.</center>*    

Let's get started by reading the train set.
```python
from pathlib import Path
import pandas as pd
import numpy as np
import torch
torch.set_printoptions(edgeitems=2, precision=2, linewidth=75)

# This is the path to our train set. You might modify it accordingly.
TITANIC_DATASET = Path( '/home/hbunyamin/Perkuliahan/Pembelajaran-Mesin-Maranatha/projects/UTS/Titanic' ) 
titanic_df = pd.read_csv( TITANIC_DATASET / 'train.csv' ) 
```
<br/>
Next, we show several rows from the dataframe.
```python
titanic_df.head()
``` 
Out:
[![img1]({{ site.baseurl }}/assets/images/titanic-head.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/titanic-head.png)
<br/>
We also show the statistics of the Titanic train as follows: 
```python
titanic_df.describe()
```
Out:
[![img1]({{ site.baseurl }}/assets/images/titanic-df-describe.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/titanic-df-describe.png)
<br/>
We are interested in making the passenger classes (`Pclass`) column into a one-hot encoding. Let's show each value and its frequency inside `Pclass` column. 
```python
titanic_df['Pclass'].value_counts()
```
Out:
```
3    491
1    216
2    184
Name: Pclass, dtype: int64
```
The number of occurrences in the dataset for value `3`, `1`, and `2` are `491`, `216`, and `184` respectively.   

Next, we convert `1`, `2` , and `3` into a one-hot encoding. Since indices in PyTorch starts from `0`and the values of `Pclass` column start from `1`, we need to make an adjustment. Let's subtract `1` from each value in `Pclass` column and view the values.     
```python
pclass = titanic_df['Pclass'] - 1
pclass.unique()
```
Out:
```
array([2, 0, 1])
```
Now the values in `pclass` consist of `0`, `1`, and `2`.
<br/>
Subsequently, we convert the `pclass` into a tensor.
```python
pclass = torch.tensor(pclass)
pclass.shape
```
Out:
```
torch.Size([891])
```
<br/>
Now we are ready to convert 

$$ \begin{equation} \texttt{0} \Rightarrow \begin{bmatrix} 1 \\ 
0  \\ 
0 \\ \end{bmatrix}, \; \texttt{1} \Rightarrow \begin{bmatrix} 0 \\ 
1  \\ 
0 \\ \end{bmatrix}, \text{ and } \texttt{2} \Rightarrow \begin{bmatrix} 0 \\ 
0  \\ 
1 \\ \end{bmatrix}. \end{equation}$$

We initialize the one-hot encoding with a zero matrix with dimension: $891 \times 3$.
```python
pclass_onehot = torch.zeros(pclass.shape[0], 3)
pclass_onehot.shape
```
Out:
```
torch.Size([891, 3])
```
<br/>
Next, we call `scatter_` method. The underscore after the method name means that the method will not return a new tensor; instead, it will modify the tensor in place.    
```python
pclass_onehot.scatter_(1, pclass.unsqueeze(1), 1.0)
``` 
Out:
```
tensor([[0., 0., 1.],
        [1., 0., 0.],
        ...,
        [1., 0., 0.],
        [0., 0., 1.]])
```
The second argument (`pclass.unsqueeze(1)`) adds a new dimension to tensor `pclass`. Therefore, the dimension of `pclass` changes from `torch.Size([891])` to `torch.Size([891, 1])`. The first argument (`1`) states that the axis `1` (column) of `pclass` that will be expanded from `1` into `3`. We need to make sure that the column size of `pclass_onehot` is the same as the number of unique values in `pclass` with each value represents a column index.   
   
We conclude the post by showing that our conversion works well.    
This is the `pclass`.
```python
pclass[:10]
```
Out:
```
tensor([2, 0, 2, 0, 2, 2, 0, 2, 2, 1])
```
Next, this is the one-hot encoding of `pclass`.
```python
pclass_onehot[0:10]
```
Out:
```
tensor([[0., 0., 1.],
        [1., 0., 0.],
        [0., 0., 1.],
        [1., 0., 0.],
        [0., 0., 1.],
        [0., 0., 1.],
        [1., 0., 0.],
        [0., 0., 1.],
        [0., 0., 1.],
        [0., 1., 0.]])
```
