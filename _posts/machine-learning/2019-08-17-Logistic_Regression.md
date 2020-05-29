---
layout: post
title: Building Logistic Regression Model from Linear Regression Model
category: Machine-Learning
lang: EN
description: Logistic & linear regression relationship 
sticky: false
---

A model called **logistic regression** is introduced in [Week 3](https://www.coursera.org/learn/machine-learning/home/week/3) of [_Machine Learning_ course taught by Andrew Ng](https://www.coursera.org/learn/machine-learning/home/welcome). This post tries to explain how to obtain **logistic regression** model from _linear regression_ model which has been explained in [Week 1](https://www.coursera.org/learn/machine-learning/home/week/1) and [Week 2](https://www.coursera.org/learn/machine-learning/home/week/2) of the course. Therefore, I recommend all readers for studying [Week 1](https://www.coursera.org/learn/machine-learning/home/week/1) and [Week 2](https://www.coursera.org/learn/machine-learning/home/week/2) before reading this post.

Week 1 of the course shows that _linear regression_ model has the capability to solve classification problem with prediction model (_hypothesis_) as follows:   

$$ \begin{equation} \bbox[5px,border:2px solid blue] {h_\theta(x) = \theta^T x} \tag{1}\label{eq:linear-regression} \end{equation} $$

with $$ \theta = \begin{bmatrix} \theta_0 & \theta_1 & \theta_2 & \cdots & \theta_n \end{bmatrix}^T $$ is called parameter model and $$ x = \begin{bmatrix} 1 & x_1 & x_2 & \cdots & x_n \end{bmatrix}^T $$ is a _test example_ whose $$y$$ we would like to predict.    

The question arises as follows:

>How can we derive **logistic regression** model from _linear regression_ model?     

As we already know that $h_\theta(x)$ in **logistic regression** has a range of values between $0$ and $1$; on the other hand, $h_\theta(x)$ in _linear regression_ has a range of values between $-\infty$ and $\infty$. Therefore, $h_\theta(x)$ which belongs to **logistic regression** needs to be converted into $-\infty < h_\theta(x) < \infty$. Moreover, after the conversion is done, the new $h_\theta(x)$ shall be substituted into Equation \eqref{eq:linear-regression}.  
<br/>

Let us start by converting $h_\theta(x)$ which belongs to **logistic regression** and then substitute the new $h_\theta(x)$ into Equation \eqref{eq:linear-regression}.    

$$ \begin{align}  0 < h_\theta(x) < 1 &\Longleftrightarrow  0 < \frac{h_\theta(x)}{1-h_\theta(x)} <  \infty \tag{2}\label{eq:odds-ratio} \\ 
	                    &\Longleftrightarrow  -\infty < \underbrace{\log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right)}_{\text{the new }h_\theta(x)} < \infty \tag{3}\label{eq:logit}.  \end{align} $$

$\frac{h_\theta(x)}{1-h_\theta(x)}$ in Equation \eqref{eq:odds-ratio} is called **odds ratio** and $\log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right)$ in Equation \eqref{eq:logit} is named as **logit** function [(Raschka & Mirjalili, 2017)](https://www.packtpub.com/big-data-and-business-intelligence/python-machine-learning-second-edition).    

Now that the new $h_\theta(x)$ has the range of values between $-\infty < h_\theta(x) < \infty$, this new $ h_\theta(x) $ can be substituted into Equation \eqref{eq:linear-regression} as follows:

$$ \begin{align} \log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right) = \theta^T x &\Longleftrightarrow e^{\log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right)} = e^{\theta^T x}   \\
	     &\Longleftrightarrow  \frac{h_\theta(x)}{1-h_\theta(x)} = e^{\theta^T x} \\
	     &\Longleftrightarrow  h_\theta(x) = e^{\theta^T x} - h_\theta(x) e^{\theta^T x}  \\
	     &\Longleftrightarrow  h_\theta(x) + h_\theta(x) e^{\theta^T x} = e^{\theta^T x}   \\ 
	     &\Longleftrightarrow  h_\theta(x) \left( 1 + e^{\theta^T x} \right) = e^{\theta^T x} \\
	     &\Longleftrightarrow  h_\theta(x) = \frac{e^{\theta^T x}}{1 + e^{\theta^T x}}  \\
	     &\Longleftrightarrow  h_\theta(x) = \frac{e^{\theta^T x}}{1 + e^{\theta^T x}}  \times \frac{e^{-\theta^T x}}{e^{-\theta^T x}} \\
	     &\Longleftrightarrow h_\theta(x) = \frac{1}{1+e^{-\theta^T x}}.
	\end{align} $$

Accordingly, **logistic regression** model that we have derived is

$$ \begin{equation} \bbox[5px,border:2px solid blue] {h_\theta(x) = \frac{1}{1+e^{-\theta^T x}}} \tag{4}\label{eq:sigmoid} \end{equation} $$

**Logistic regression** model in Equation \eqref{eq:sigmoid} is popularly also called **sigmoid function**. Finally, we have successfully derived **logistic regression** model (Equation \eqref{eq:sigmoid}) from _linear regression_ model (Equation \eqref{eq:linear-regression}).     
<br/>
### References
Raschka, S. and Mirjalili, V. (2017) _Python Machine Learning Second Edition_. Packt Publishing Ltd. Page 59-60.
