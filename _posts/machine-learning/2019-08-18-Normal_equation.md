---
layout: post
title: Deriving Normal Equation of Linear Regression Model
category: Machine-Learning
lang: EN
description: How to derive normal equation
sticky: false
---

This article is inspired by [an excellent post by Eli Bendersky](https://eli.thegreenplace.net/2015/the-normal-equation-and-matrix-calculus). Let's continue with the derivation.

**Cost function** has been explained in [Week 1](https://www.coursera.org/learn/machine-learning/home/week/1) and [Week 2](https://www.coursera.org/learn/machine-learning/home/week/2) of [_Machine Learning_ course taught by Andrew Ng](https://www.coursera.org/learn/machine-learning/home/welcome). This post tries to explain how to derive **normal equation** for _linear regression with multiple variables_. It is a good thing if all readers has studied [Week 1](https://www.coursera.org/learn/machine-learning/home/week/1) and [Week 2](https://www.coursera.org/learn/machine-learning/home/week/2) before reading this post.

The **cost function** of _linear regression with multiple variables_, $J(\theta)$ is formulated as follows:   

$$ \begin{equation} J(\theta) = \frac{1}{2m} \sum_{i=1}^{m}{(h_{\theta}(x^{(i)}) - y^{(i)})^2}  \tag{1}\label{eq:cost-function} \end{equation} $$

with $m$ is number of instances in dataset, $h_{\theta}(x^{(i)})$ is our hyphotesis also known as prediction model for the $i$th instance, and $y^{(i)}$ is true value for the $i$th instance.

We also have studied that 

$$ \begin{equation} h_{\theta}(x^{(i)}) = \theta_0 + \theta_1 x_1^{(i)} + \cdots + \theta_n x_n^{(i)}  \tag{2}\label{eq:the-hyphotesis} \end{equation} $$

By substituting \eqref{eq:the-hyphotesis} into \eqref{eq:cost-function}, we obtain

$$ \begin{align}  J(\theta) &= \frac{1}{2m} \sum_{i=1}^{m}{(\theta_0 + \theta_1 x_1^{(i)} + \cdots + \theta_n x_n^{(i)} - y^{(i)})^2}  \tag{3}\label{eq:derivation-1} \\
&= \frac{1}{2m} ((\theta_0 + \theta_1 x_1^{(1)} + \cdots + \theta_n x_n^{(1)} - y^{(1)} )^2 + \cdots + (\theta_0 + \theta_1 x_1^{(m)} + \cdots + \theta_n x_n^{(m)} - y^{(m)} )^2 ) \tag{4}\label{eq:derivation-2} \\
&= \frac{1}{2m} \underbrace{ \begin{bmatrix} (\theta_0 + \theta_1 x_1^{(1)} + \cdots + \theta_n x_n^{(1)} - y^{(1)}) & \cdots & (\theta_0 + \theta_1 x_1^{(m)} + \cdots + \theta_n x_n^{(m)} - y^{(m)}) \end{bmatrix}}_{\text{matrix with size: } 1 \times m} \underbrace{\begin{bmatrix} (\theta_0 +\theta_1 x_1^{(1)} + \cdots + \theta_n x_n^{(1)} - y^{(1)}) \\
\vdots \\
(\theta_0 +\theta_1 x_1^{(m)} + \cdots + \theta_n x_n^{(m)} - y^{(1)})
 \end{bmatrix}}_{\text{matrix with size: } m \times 1} \tag{5}\label{eq:derivation-3} \\
 &= \frac{1}{2m} \left( \begin{bmatrix} (\theta_0 + \theta_1 x_1^{(1)} + \cdots + \theta_n x_n^{(1)} - y^{(1)}) & \cdots & (\theta_0 + \theta_1 x_1^{(m)} + \cdots + \theta_n x_n^{(m)} - y^{(m)}) \end{bmatrix} - \begin{bmatrix} y^{(1)} & \cdots & y^{(m)} \end{bmatrix} \right) \left( \begin{bmatrix} \theta_0 + \theta_1 x_1^{(1)} + \cdots + \theta_n x_n^{(1)} \\
 \theta_0 + \theta_1 x_1^{(2)} + \cdots + \theta_n x_n^{(2)} \\
 \vdots \\
 \theta_0 + \theta_1 x_1^{(m)} + \cdots + \theta_n x_n^{(m)} \end{bmatrix}  - \begin{bmatrix} y^{(1)} \\ 
 y^{(2)} \\
 \vdots \\
 y^{(m)} \end{bmatrix} \right) \tag{6}\label{eq:derivation-4} \\
 &= \frac{1}{2m} \left( \begin{bmatrix} \theta_0 & \theta_1 & \cdots & \theta_n \end{bmatrix} \begin{bmatrix} 1 & 1 & \cdots & 1 \\ 
 x_1^{(1)} & x_1^{(2)} & \cdots & x_1^{(m)} \\
 \vdots & \vdots & \cdots & \vdots \\
 x_n^{(1)} & x_n^{(2)} & \cdots & x_n^{(m)} \\\end{bmatrix} - \begin{bmatrix} y^{(1)} & \cdots & y^{(m)} \end{bmatrix} \right) \left( \begin{bmatrix} 1 & x_1^{(1)} & \cdots & x_n^{(1)} \\
  1 & x_1^{(2)} & \cdots & x_n^{(2)} \\
  \vdots & \vdots & \cdots & \vdots \\
  1 & x_1^{(m)} & \cdots & x_n^{(m)} \end{bmatrix} \begin{bmatrix} \theta_0 \\ 
 \theta_1 \\
 \vdots \\
 \theta_n \end{bmatrix} - \begin{bmatrix} y^{(1)} \\
  y^{(2)} \\ 
  \ldots \\
  y^{(m)} \end{bmatrix} \right) \tag{7}\label{eq:derivation-5}  \end{align}$$

By defining 

$$ \begin{equation} \theta = \begin{bmatrix} \theta_0 \\ 
\theta_1 \\ 
\vdots \\
\theta_n \end{bmatrix} \tag{8}\label{eq:defining-theta} \end{equation} $$

and 

$$ \begin{equation} X = \begin{bmatrix} 1 & x_1^{(1)} & \cdots & x_n^{(1)} \\
1      & x_1^{(2)} & \cdots  & x_n^{(2)} \\ 
\vdots & \vdots    &  \vdots &  \vdots  \\
1 & x_1^{(m)} & \cdots & x_n^{(m)} \end{bmatrix} \tag{9}\label{eq:defining-X} \end{equation} $$

also

$$ \begin{equation} Y = \begin{bmatrix} y^{(1)} \\ 
y^{(2)} \\ 
\vdots \\
y^{(m)} \end{bmatrix}, \tag{10}\label{eq:defining-Y} \end{equation} $$

equation \eqref{eq:derivation-5} becomes

$$ \begin{align} J(\theta) &= \frac{1}{2m} (\theta^T X^T - Y^T)(X \theta - Y) &&\text{by transpose property} \tag{11}\label{eq:derivation-6} \\
&= \frac{1}{2m} (\theta^T X^T X \theta - \underbrace{\theta^T X^T Y}_{\text{a scalar}} - \underbrace{Y^T X \theta}_{\text{a scalar}} + Y^T Y)  &&\text{by matrix multiplication} \tag{12}\label{eq:derivation-7} \\
&= \frac{1}{2m} (\theta^T X^T X \theta - \theta^T X^T Y - (X \theta)^T Y + Y^T Y) &&\text{by rearranging a scalar} \tag{13}\label{eq:derivation-8} \\
&= \frac{1}{2m} (\theta^T X^T X \theta - \theta^T X^T Y - \theta^T X^T Y + Y^T Y) &&\text{by transpose property} \tag{14}\label{eq:derivation-9} \\
&= \frac{1}{2m} (\underbrace{\theta^T X^T X \theta}_{\text{Part I}} - \underbrace{2 \theta^T X^T Y}_{\text{Part II}} + Y^T Y) &&\text{by summation property} \tag{15}\label{eq:derivation-10} \\
\end{align}$$

We have arrived into a matrix form from **linear regression cost function**. Our next step would be: 

>How can we minimize the **cost function** in Equation \eqref{eq:derivation-10}?     

We will employ the derivation formula from [Matrix Calculus](https://en.wikipedia.org/wiki/Matrix_calculus); specifically, we use **two scalar-by-vector identities** with **denominator layout** (result: column vector). The identities are as follows:

$$ \begin{equation} 
	\frac{\partial \mathbf{x}^T \mathbf{A} \mathbf{x} }{\partial \mathbf{x}} = 2 \mathbf{A} \mathbf{x} \tag{16}\label{eq:identity-1}
\end{equation} $$

and 

$$ \begin{equation} 
	\frac{\partial \mathbf{a}^T \mathbf{x} }{\partial \mathbf{x}} = \frac{\partial \mathbf{x}^T \mathbf{a} }{\partial \mathbf{x}} = \mathbf{a} \tag{17}\label{eq:identity-2}
\end{equation} $$

Now equipped with these identities, let us minimize Equation \eqref{eq:derivation-10} by computing the first derivation of $J(\theta)$; specifically, the Part I is computed with Equation \eqref{eq:identity-1} and Part II with Equation \eqref{eq:identity-2}:

$$ \begin{equation} 
	\frac{\partial J }{\partial \theta} = \frac{1}{2m} ( 2 X^T X \theta - 2 X^T Y ) \tag{18}\label{eq:derivation-of-J}
\end{equation} $$

In order to find $\theta$ which minimize Equation \eqref{eq:derivation-10}, we need to solve 

$$ \begin{align} \frac{\partial J}{\partial \theta} = 0 &\Longleftrightarrow \frac{1}{2m} ( 2 X^T X \theta - 2 X^T Y ) = 0 \\
 &\Longleftrightarrow 2 X^T X \theta - 2 X^T Y = 0 \\
   &\Longleftrightarrow 2 X^T X \theta = 2 X^T Y  \\ 
   &\Longleftrightarrow X^T X \theta = X^T Y \\ 
   &\Longleftrightarrow \theta = (X^T X)^{-1} X^T Y &&\text{by inverse matrix} \tag{19}\label{eq:final-result} \end{align} $$


At last, we have derived **the normal equation of linear regression model** that is 

$$ \begin{equation} \bbox[5px,border:2px solid blue] {\theta = (X^T X)^{-1} X^T Y}. \end{equation} $$
