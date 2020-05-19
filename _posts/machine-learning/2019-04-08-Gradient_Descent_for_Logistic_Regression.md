---
layout: post
title: How to Compute the Gradient of Cost Function from Logistic Regression
category: Machine-Learning
lang: EN
description: Deriving partial derivatives of cost function from Logistic Regression 
sticky: false
---

In [linear regression with one variable](https://www.coursera.org/learn/machine-learning/lecture/db3jS/model-representation), we have a _design matrix_ ($X$) that represents our dataset and specifically has a shape as follows:

$$ \begin{equation} X = \begin{bmatrix} 1 & x^{(1)} \\
1      & x^{(2)} \\
\vdots & \vdots  \\
1      & x^{(m)}   \end{bmatrix}.  \end{equation} \tag{1}\label{eq:x-dataset}$$

We say that the _design matrix_ ($X$) in Equation \eqref{eq:x-dataset} has $m$ _training examples_ and 1 _feature_, $x$.    

The **logistic regression** model shall be trained on $X$. For those who are not familiar with logistic regression model can study the model in [_Machine Learning Course by Andrew Ng_](https://www.coursera.org/learn/machine-learning/lecture/1XG8G/cost-function) in Week 4. The **logistic regression** model has a model as follows:

$$ \require{cancel} \begin{equation} h_{\theta}(x^{(i)}) = \frac{1}{1 + e^{-\theta_0 - \theta_1 x^{(i)}}}. \tag{2}\label{eq:model-logistic}\end{equation} $$

Furthermore, **logistic regression** model has a _cost function_ $J(\theta)$,

$$ \begin{equation} J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \text{Cost}(h_{\theta}(x^{(i)}), y^{(i)}) \tag{3}\label{eq:cost-function} \end{equation}  $$    

with

$$ \begin{equation} \text{Cost}(h_{\theta}(x^{(i)}), y^{(i)}) = -y^{(i)} \log( h_{\theta}(x^{(i)}) ) - (1-y^{(i)}) \log(1-h_{\theta}(x^{(i)})) \end{equation} \tag{4}\label{eq:cost-logistic} $$   

and $x^{(i)}$ is an $i$th _training example_, and $y^{(i)}$ is label or class from a _training example_ $x^{(i)}$.   
This article attempts to explain how to calculate partial derivatives from **logistic regression** _cost function_ on $\theta_0$ and $\theta_1$. This partial derivatives are also called _gradient_, $\frac{\partial J}{\partial \theta}$.    
<br/>
#### **The Complete Form of Logistic Regression _Cost Function_**
By combining Equation \eqref{eq:cost-function} and \eqref{eq:cost-logistic}, a more detailed _cost function_ can be obtained as follows:    

$$ \begin{align} J(\theta) &= \frac{1}{m} \sum_{i=1}^{m} \text{Cost}(h_{\theta}(x^{(i)}), y^{(i)}) \\
                           &= \frac{1}{m} \sum_{i=1}^{m} \left( -y^{(i)} \log (h_{\theta}(x^{(i)})) - (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \\
                           &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right). \tag{5}\label{eq:cost-function-complete} \end{align} $$

Next, $\frac{\partial J}{\partial \theta_0}$ and $\frac{\partial J}{\partial \theta_1}$ shall be computed. Now we compute the partial derivative of $h_{\theta}(x)$ on $\theta_0$ or $\frac{\partial h_{\theta}}{ \partial \theta_0 }$.   
From [Calculus](https://www.khanacademy.org/math/multivariable-calculus), the derivatives of $\frac{u(x)}{v(x)}$ with each $u(x)$ dan $v(x)$ is a function of $x$ are 

$$ \begin{equation} \frac{u^{\prime} v - u v^{\prime} }{ v^2 }. \tag{6}\label{eq:formula-derivatif} \end{equation}$$

with $u^{\prime}$ and $v^{\prime}$ are the first derivatives of $u$ and $v$, respectively.   
We shall utilize this formula in Equation \eqref{eq:formula-derivatif} to calculate $\frac{\partial h_{\theta}}{ \partial \theta_0 }$ and $\frac{\partial h_{\theta}}{ \partial \theta_1 }$ as follows:

$$ \begin{align} \frac{\partial h_{\theta}}{ \partial \theta_0 } &= \frac{0 + e^{-\theta_0 - \theta_1 x}}{(1 + e^{-\theta_0 - \theta_1 x})^2} = \frac{e^{-\theta_0 - \theta_1 x}}{(1 + e^{-\theta_0 - \theta_1 x})^2} \\ 
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( \frac{e^{-\theta_0 - \theta_1 x}}{1 + e^{-\theta_0 - \theta_1 x}} \right)  \\
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( 1 - \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \\
 &= h_\theta(x) (1 - h_\theta(x)) \tag{7}\label{eq:formula-derivatif-theta0}
  \end{align}$$

and 

$$ \begin{align} \frac{\partial h_{\theta}}{ \partial \theta_1 } &= \frac{0 + e^{-\theta_0 - \theta_1 x} x}{(1 + e^{-\theta_0 - \theta_1 x})^2} = \frac{e^{-\theta_0 - \theta_1 x} x}{(1 + e^{-\theta_0 - \theta_1 x})^2} \\ 
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( \frac{e^{-\theta_0 - \theta_1 x}}{1 + e^{-\theta_0 - \theta_1 x}} \right)x  \\
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( 1 - \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right)x \\
 &= h_\theta(x) (1 - h_\theta(x)) x. \tag{8}\label{eq:formula-derivatif-theta1}
  \end{align} $$    
<br/>
#### **Calculate $\frac{\partial J}{\partial \theta_0}$**    
The partial derivative $\frac{\partial J}{\partial \theta_0}$ is calculated as follows:

$$ \begin{align} \frac{\partial J}{\partial \theta_0} &= \frac{\partial }{\partial \theta_0} \left( -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \frac{\partial }{\partial \theta_0} \left( \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_0} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Part I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_0} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Part II}} \right). \tag{9}\label{eq:bagian2-theta0} \end{align} $$

 Part I from Equation \eqref{eq:bagian2-theta0} is calculated with _chain rules_ technique and Equation \eqref{eq:formula-derivatif-theta0} becomes

 $$ \begin{align} \frac{\partial }{\partial \theta_0} \left( \log (h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log (h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_0} \\
 &= \frac{1}{h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) \\
 &= \frac{1}{ \cancel{h_{\theta}(x^{(i)})} } \cancel{h_\theta(x^{(i)})} (1 - h_\theta(x^{(i)}))  \\
 &= (1 - h_\theta(x^{(i)})). \tag{10}\label{eq:bagian-I-theta0} \end{align} $$

Part II from Equation \eqref{eq:bagian2-theta0} is also calculated with the chain rules and Equation \eqref{eq:formula-derivatif-theta0} becomes

 $$ \begin{align} \frac{\partial }{\partial \theta_0} \left( \log (1 - h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log ( 1- h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_0} \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} (1 - h_\theta(x^{(i)})) h_\theta(x^{(i)})  \\
 &= - \frac{1}{ \cancel{1 - h_{\theta}(x^{(i)})} } \cancel{(1- h_\theta(x^{(i)}))} h_\theta(x^{(i)})  \\
 &= -h_\theta(x^{(i)}). \tag{11}\label{eq:bagian-II-theta0} \end{align} $$

 By substituting Equation \eqref{eq:bagian-I-theta0} and Equation \eqref{eq:bagian-II-theta0} into Equation \eqref{eq:bagian2-theta0} we obtain

$$ \begin{align} \frac{\partial J}{\partial \theta_0} &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_0} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Part I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_0} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Part II}} \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} (1 - h_{\theta}(x^{(i)}))  - (1-y^{(i)}) h_{\theta}(x^{(i)}) \right)  \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} - y^{(i)} h_{\theta}(x^{(i)})  - h_{\theta}(x^{(i)}) + y^{(i)} h_{\theta}(x^{(i)}) \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \cancel{- y^{(i)} h_{\theta}(x^{(i)})}  - h_{\theta}(x^{(i)}) \cancel{+ y^{(i)} h_{\theta}(x^{(i)})} \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} ( y^{(i)} - h_{\theta}(x^{(i)}) )  \\
&= \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ). \end{align} $$    
<br/>
#### **Calculate $\frac{\partial J}{\partial \theta_1}$**    
The partial derivative $\frac{\partial J}{\partial \theta_1}$ can be calculated as follows:

$$ \begin{align} \frac{\partial J}{\partial \theta_1} &= \frac{\partial }{\partial \theta_1} \left( -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \frac{\partial }{\partial \theta_1} \left( \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_1} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Part I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_1} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Part II}} \right). \tag{12}\label{eq:bagian2-theta1} \end{align} $$

 Part I from Persamaan \eqref{eq:bagian2-theta1} is calculated by _chain rules_ and Equation \eqref{eq:formula-derivatif-theta1} becomes

 $$ \begin{align} \frac{\partial }{\partial \theta_1} \left( \log (h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log (h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_1} \\
 &= \frac{1}{h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) x^{(i)} \\
 &= \frac{1}{ \cancel{h_{\theta}(x^{(i)})} } \cancel{h_\theta(x^{(i)})} (1 - h_\theta(x^{(i)})) x^{(i)} \\
 &= (1 - h_\theta(x^{(i)})) x^{(i)}. \tag{13}\label{eq:bagian-I-theta1} \end{align} $$

Part II from Equation \eqref{eq:bagian2-theta1} is also calculated with chain rules and Equation \eqref{eq:formula-derivatif-theta1} becomes

 $$ \begin{align} \frac{\partial }{\partial \theta_1} \left( \log (1 - h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log ( 1- h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_1} \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) x^{(i)} \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} (1 - h_\theta(x^{(i)})) h_\theta(x^{(i)}) x^{(i)}  \\
 &= - \frac{1}{ \cancel{1 - h_{\theta}(x^{(i)})} } \cancel{(1- h_\theta(x^{(i)}))} h_\theta(x^{(i)}) x^{(i)}  \\
 &= -h_\theta(x^{(i)}) x^{(i)}. \tag{14}\label{eq:bagian-II-theta1} \end{align} $$

Again, by substituting Equation \eqref{eq:bagian-I-theta1} and Equation \eqref{eq:bagian-II-theta1} into Equation  \eqref{eq:bagian2-theta1}, we obtain

$$ \begin{align} \frac{\partial J}{\partial \theta_1} &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_1} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Bagian I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_1} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Bagian II}} \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} (1 - h_{\theta}(x^{(i)})) x^{(i)}  - (1-y^{(i)}) h_{\theta}(x^{(i)}) x^{(i)} \right)  \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} - y^{(i)} h_{\theta}(x^{(i)})  - h_{\theta}(x^{(i)}) + y^{(i)} h_{\theta}(x^{(i)}) \right) x^{(i)} \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \cancel{- y^{(i)} h_{\theta}(x^{(i)})}  - h_{\theta}(x^{(i)}) \cancel{+ y^{(i)} h_{\theta}(x^{(i)})} \right) x^{(i)} \\
&= -\frac{1}{m} \sum_{i=1}^{m} ( y^{(i)} - h_{\theta}(x^{(i)}) ) x^{(i)}   \\
&= \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ) x^{(i)}.  \end{align} $$    

Therefore, the _gradient_ of **logistic regression** model with 1 variable, $x$ and 2 parameters, $\theta_0$ dan $\theta_1$ is

$$ \begin{equation} \frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} )  \end{equation} $$ 

and    

$$ \begin{equation} \frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ) x^{(i)} . \end{equation} $$ 

In general, _gradient_ of **logistic regression** model dengan $n$ variables, $x_1, x_2, \ldots, x_n$ and $n+1$ parameters, $\theta_0, \theta_1, \ldots, \theta_n$ is

$$ $$ \begin{equation} \frac{\partial J}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ) x_{j}^{(i)}.  \end{equation} $$ 
 $$

Additionally, in case $j=0$, we have $x_0^{(i)} = 1$ for $i = 1, 2, \ldots, m$.
