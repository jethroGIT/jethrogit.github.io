---
layout: post
title: A Quantum of the Fisher Information Derivation
category: Data-Science-1
lang: EN
description: Equation (2.20) from BDA on page 53
sticky: true
---

This post elaborates a derivation of Equation (2.20) on page 53 of [**Bayesian Data Analysis Third Edition**](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf).    

[![img1]({{ site.baseurl }}/assets/images/Youngronaldfisher2.JPG){:class="img-responsive"}]({{ site.baseurl }}/assets/images/Youngronaldfisher2.JPG)*<center>$\pmb{\text{Figure 1}}$: Sir Ronald Aylmer Fisher (17 February 1890 - 29 July 1962). One of his many great contributions to Statistics is <a href="https://en.wikipedia.org/wiki/Fisher_information">Fisher Information</a>. Image taken from <a href="https://en.wikipedia.org/wiki/Ronald_Fisher">Wikipedia</a>, some rights reserved.</center>*   

Concretely, we want to show the derivation $J(\theta)$, the _Fisher Information_, from

$$ \begin{equation}
	J(\theta) = \text{E}\left( \left( \frac{d \log \Pr(y \mid \theta )}{d\theta} \right)^2 \, \middle| \, \theta \right) \tag{1}\label{eq:start-point}
\end{equation}$$

to

$$ \begin{equation}
	J(\theta) = - \text{E}\left( \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} \, \middle| \, \theta \right). \tag{2}\label{eq:end-point}
\end{equation}$$

The idea of this derivation comes from a [**lecture note by John Duchi from Stanford Statistics class**](https://web.stanford.edu/class/stats311/Lectures/lec-09.pdf). The difference between this post and the lecture note is that the lecture note deals with _multi-variables_ which employs second derivatives for multi-values ([_Hessian matrix_](https://en.wikipedia.org/wiki/Hessian_matrix)); on the other hand, this post deals with a single variable and employs a second derivative for just one value.     

Let's start with computing 
$$\begin{equation} 
	\text{E} \left( \frac{d \log \Pr(y \mid \theta)}{d\theta} \, \middle| \, \theta \right)
\end{equation}$$.   
  
  
$$ \require{cancel} \begin{align}
	\text{E}\left( \frac{d \log \Pr(y \mid \theta)}{d\theta} \, \middle| \, \theta \right) &= \int \frac{d \log \Pr(y \mid \theta)}{d\theta} \Pr(y \mid \theta) d\theta  && \text{definition of expectation} \tag{3}\label{eq:dlog-1} \\
	&= \int \frac{d \Pr(y \mid \theta)}{d\theta} \frac{1}{\Pr(y \mid \theta)} \; \Pr(y \mid \theta) d\theta  && \text{derivation of }\frac{d \log \Pr(y \mid \theta)}{d\theta} \tag{4}\label{eq:dlog-2} \\
	&= \int \frac{d \Pr(y \mid \theta)}{d\theta} \frac{1}{\cancel{\Pr(y \mid \theta)}} \; \cancel{\Pr(y \mid \theta)}  d\theta \tag{5}\label{eq:dlog-3}	 \\
	&= \int \frac{d \Pr(y \mid \theta)}{d\theta} d\theta  \tag{6}\label{eq:dlog-4}	 \\
	&= \frac{d}{d\theta} \int \Pr(y \mid \theta) d\theta && \text{exchange }\frac{d}{d\theta} \text{ and } \int \tag{7}\label{eq:dlog-5} \\
	&= \frac{d}{d\theta} \underbrace{\int \Pr(y \mid \theta) d\theta}_{1} && \text{property of a pdf}\tag{8}\label{eq:dlog-6} \\
	&= \frac{d}{d\theta} (1) \tag{9}\label{eq:dlog-7} 	\\
	&= 0. \tag{10}\label{eq:dlog-8}
\end{align}$$

Consider Equation \eqref{eq:dlog-5}, we shall utilize this exchangeability between _integral_ and _differentiation_ again later.

Equation \eqref{eq:dlog-2} states that

$$\begin{equation}
	\frac{d \log \Pr(y \mid \theta)}{d\theta} = \underbrace{\frac{1}{\Pr(y \mid \theta)}}_{u}  \underbrace{\frac{d \Pr(y \mid \theta)}{d\theta}}_{v}. \tag{11}\label{eq:first-order-derivation}
\end{equation}$$

Therefore,  
  
$$\begin{align}
	\frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} &= \underbrace{- \frac{1}{\Pr( y \mid \theta )^2} \frac{d \Pr(y \mid \theta)}{d\theta}}_{u^{\prime}} \underbrace{\frac{d \Pr(y \mid \theta)}{d\theta}}_{v}  + \underbrace{\frac{1}{\Pr(y \mid \theta)}}_{u} \underbrace{\frac{d^2 \Pr(y \mid \theta)}{d\theta^2}}_{v^{\prime}} &&  \text{based on } u^{\prime} v + u v^{\prime} \tag{12}\label{eq:second-order-1} \\
	&= \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} - \left( \frac{d\Pr(y \mid \theta)}{d\theta} \frac{1}{\Pr(y \mid \theta)}  \right) \left( \frac{d\Pr(y \mid \theta)}{d\theta} \frac{1}{\Pr(y \mid \theta)}  \right) && \text{just rearranging} \tag{13}\label{eq:second-order-2} \\
	&= \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} - \left(  \frac{d \log \Pr( y \mid \theta)}{d\theta} \right) \left( \frac{d \log \Pr( y \mid \theta)}{d\theta} \right) && \text{based on Equation }\eqref{eq:first-order-derivation} \tag{14}\label{eq:second-order-3} \\	
	&= \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} - \left(  \frac{d \log \Pr( y \mid \theta)}{d\theta} \right)^{2} \tag{15}\label{eq:second-order-4}		
\end{align}$$

From Equation \eqref{eq:second-order-4} we obtain  

$$\begin{align}
	\frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} = \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} - \left(  \frac{d \log \Pr( y \mid \theta)}{d\theta} \right)^{2} &\Longleftrightarrow \left(  \frac{d \log \Pr( y \mid \theta)}{d\theta} \right)^{2} = - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} + \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} \tag{16}\label{eq:second-order-last}
\end{align}$$

Now we are ready to calculate
$$\begin{equation}
	\text{E}\left( \left( \frac{d \log \Pr(y \mid \theta )}{d\theta} \right)^2 \, \middle| \, \theta \right).
\end{equation}$$

$$ \require{cancel} \begin{align}
	\text{E}\left( \left( \frac{d \log \Pr(y \mid \theta )}{d\theta} \right)^2 \, \middle| \, \theta \right) &= \int \left( \frac{d \log \Pr(y \mid \theta )}{d\theta} \right)^2 \Pr(y \mid \theta) d\theta && \text{by definition} \tag{17}\label{eq:final-showdown-1}\\
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} + \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} \right) \Pr(y \mid \theta) d\theta && \text{by Equation }\eqref{eq:second-order-last} \tag{18}\label{eq:final-showdown-2}\\
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta + \int \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\Pr(y \mid \theta)} \Pr(y \mid \theta) d\theta && \text{by distributive} \tag{19}\label{eq:final-showdown-3}\\
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta + \int \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} \frac{1}{\cancel{\Pr(y \mid \theta)}} \cancel{\Pr(y \mid \theta)} d\theta  \tag{20}\label{eq:final-showdown-4}\\		
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta + \int \frac{d^2 \Pr(y \mid \theta)}{d\theta^2} d\theta  \tag{21}\label{eq:final-showdown-5}\\
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta + \frac{d^2}{d\theta^2} \left( \int \Pr(y \mid \theta) d\theta \right) && \text{by exchangeability again}  \tag{22}\label{eq:final-showdown-6}\\	
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta + \underbrace{\frac{d^2}{d\theta^2} \left( \int \Pr(y \mid \theta) d\theta \right)}_{0} && \text{similar to Equation }\eqref{eq:dlog-8}  \tag{23}\label{eq:final-showdown-7}\\					
	&= \int \left( - \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta \tag{24}\label{eq:final-showdown-8}\\
	&= - \int \left( \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2}  \right) \Pr(y \mid \theta) d\theta \tag{25}\label{eq:final-showdown-9}\\											
	&= - \text{E}\left( \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} \, \middle| \, \theta  \right). && \text{by definition} \tag{26}\label{eq:final-showdown-10}					
\end{align}$$

At last, we have finally shown that

$$ \begin{equation}
	J(\theta) = \text{E}\left( \left( \frac{d \log \Pr(y \mid \theta )}{d\theta} \right)^2 \, \middle| \, \theta \right)  = - \text{E}\left( \frac{d^2 \log \Pr(y \mid \theta)}{d\theta^2} \, \middle| \, \theta \right)
\end{equation}$$

as it is explained by Equation (2.20) on page 53 of the [**book**](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf).