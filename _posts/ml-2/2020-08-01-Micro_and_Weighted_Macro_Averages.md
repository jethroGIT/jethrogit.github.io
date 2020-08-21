---
layout: post
title: Micro-average = Weighted Macro-average 
category: ML-2
lang: EN
description: Micro-average & Weighted Macro-average 
sticky: true
---

Common classification problems in Machine Learning (ML) are binary and multi-class (Sokolova and Lapalme, 2009). For binary classification, we have _accuracy_, _precision_, _recall_, and a combination of _precision_ and _recall_ which is so-called $$F_1$$ score. However, the _precision_ and _recall_ from binary classification cannot be utilized literally to measure multi-class classification.

To measure the performance of multi-class classification, two important modifications on precision and recall of binary classification are introduced. Their names are **macro-average** and **micro-average**. Therefore, for example, the precision of multi-class classification shall become **macro-average** precision and **micro-average** precision.

Let's begin with an example of multi-class classification with $$4$$ classes ($$0$$, $$1$$, $$2$$, and $$3$$). Suppose we have $$\text{our predictions}$$ and the $$\text{true labels}$$ for five data instances as follows:

$$
    \begin{align} 
        \text{our predictions} &= [ 0, 0, 2, 2, 3 ],  \\
        \text{true labels} &= [ 0, 1, 3, 3, 3 ] 
    \end{align}$$

Our first prediction is $0$ and the true label is $0$. Next, our second prediction is $0$ and the true label is $1$. Our third prediction is $2$ while the true label is $3$ and so on. Let's denote 

$$\begin{align} tp_i &= \text{true positive for class }i \; (i = 0,1,2,3), \\
                fp_i &= \text{false positive for class }i \; (i = 0,1,2,3).  \end{align}$$

After counting the true and false positives for each class, we obtain

$$\begin{align} tp_0 &= 1, \; tp_1 = 0, \; tp_2 = 0, \; tp_3 = 1, \text{ and} \\
                fp_0 &= 1, \; fp_1 = 0, \; fp_2 = 2, \; fp_3 = 0.  \end{align}$$

As we've already known, $\text{precision}$ for class $i$ ($\text{precision}_i$) is defined as follows:

$$ \begin{equation}
    \text{precision}_i = \frac{tp_i}{tp_i + fp_i}, \text{ for }i = 0,1,2,3. \tag{1}\label{eq:precision-formula}
\end{equation}$$

Therefore, employing Equation \eqref{eq:precision-formula}, we get

$$ \begin{equation}
    \text{precision}_0 = 0.5, \; \text{precision}_1 = 0, \; \text{precision}_2 = 0, \; \text{precision}_3 = 1. \tag{2}\label{eq:precision-results}
\end{equation}$$


As explained in "[Micro Average vs Macro average Performance in a Multiclass classification setting](https://datascience.stackexchange.com/questions/15989/micro-average-vs-macro-average-performance-in-a-multiclass-classification-settin)", the **macro-average** precision ($\text{precision}_M$) for $4$ classes is defined as 
    
$$\begin{align}
    \text{precision}_M &= \frac{\sum_{i=0}^{3}{\text{precision}_i}}{4} \\
                       &= \frac{0.5 + 0 + 0 + 1}{4} \\
                       &= 0.375.
\end{align}$$

However, the **micro-average** precision ($\text{precision}_\mu$) for $4$ classes is defined as 

$$\begin{align}
    \text{precision}_\mu &= \frac{\sum_{i=0}^{3}{tp_i}}{\sum_{i=0}^{3}{(tp_i + fp_i)}} \\
                       &= \frac{1+0+0+1}{2+0+2+1} \\
                       &= 0.4.
\end{align}$$

If there is a [class imbalance problem](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/), one of the options will be using **weighted macro-average** as performance metrics. The **weighted macro-average** precision ($\text{precision}_{WM}$) for $4$ classes is defined as

$$\begin{equation}
    \text{precision}_{WM} = \sum_{i=0}^{3} \text{weight}_i \times \text{precision}_i  \tag{3}\label{eq:weighted-precision}
\end{equation}$$

with $\text{weight}_i$ is the weight assigned to class $i$ as follows:

$$\begin{equation}
    \text{weight}_i = \frac{tp_i + fp_i}{\sum_{i=0}^{3}{(tp_i + fp_i)}} \tag{4}\label{eq:weight}
\end{equation}$$

Using Equation \eqref{eq:weighted-precision} and \eqref{eq:weight}, we compute the **weighted macro-average** precision as follows:

$$\begin{align}
    \text{precision}_{WM} &= \frac{2}{5} \times 0.5 + 0 \times 0 + \frac{2}{5} \times 0 + \frac{1}{5} \times 1 \\
                          &= 0.4.
\end{align}$$

Next, we shall show that the **weighted macro-average** precision equals to the **micro-average** precision. 

$$\require{cancel} \begin{align}
    \text{precision}_{WM} &= \sum_{i=0}^{3} \text{weight}_i \times \text{precision}_i   \\
                          &= \sum_{i=0}^{3} \frac{tp_i + fp_i}{\sum_{i=0}^{3}{(tp_i + fp_i)}} \times \frac{tp_i}{tp_i + fp_i} \\
                          &= \sum_{i=0}^{3} \frac{\cancel{tp_i + fp_i}}{\sum_{i=0}^{3}{(tp_i + fp_i)}} \times \frac{tp_i}{\cancel{tp_i + fp_i}} \\ 
                          &= \sum_{i=0}^{3} {\frac{tp_i}{\sum_{i=0}^{3}{(tp_i + fp_i)}}} \\
                          &= \frac{\sum_{i=0}^{3}{tp_i}}{\sum_{i=0}^{3}{(tp_i + fp_i)}} \\
                          &= \text{precision}_\mu.

\end{align}$$

Finally we have reached the end of this post. In brief, we have shown how to compute **macro-average**, **micro-average**, and **weighted macro-average**. Moreover, we have also shown that the **micro-average** equals to **weighted macro-average**.

<br/>   
#### References
Sokolova, M. and Lapalme, G. (2009). A systematic analysis of performance measures for classification tasks. _Information Processing & Management_, 45(4):427 - 437.
