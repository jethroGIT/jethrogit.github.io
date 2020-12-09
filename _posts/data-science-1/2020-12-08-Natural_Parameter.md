---
layout: post
title: Showing Binomial is an Exponential Family with a Natural Parameter
category: Data-Science-1
lang: EN
description: This is an exercise from BDA on page 37
sticky: false
---

This post shows that the binomial is indeed an **exponential family** with **natural parameter** $\text{logit}(\theta)$. Specifically, this exercise comes from Chapter 2 of [_**Bayesian Data Analysis (BDA) 3rd Edition**_](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf) on page 37.    
    
Recall that a binomial distribution whose **likelihood** $\Pr(y \mid \theta, n ) = \text{Bin}(y \mid n, \theta)$ with $n$ known, the **conjugate prior distribution** on $\theta$ is a **beta distribution**. Particularly, the **likelihood** (a _binomial distribution_) is

$$ \begin{equation}
  \Pr( y \mid \theta ) \propto \theta^y (1 - \theta)^{n-y} \tag{1}\label{eq:likelihood}
\end{equation}$$    
with $\theta$ denotes a probability of a head occurrence, $n$ is a number of trials, and $y$ expresses a number of head occurences. Additionally, the prior (a _beta distribution_) is

$$ \begin{equation}
  \Pr( \theta ) \propto \theta^{\alpha - 1} (1 - \theta)^{\beta - 1} \tag{2}\label{eq:prior}
\end{equation}$$    
with $\alpha$ and $\beta$ denote a number of head and tail occurrences respectively. 

We will show that 

$$ \begin{equation}
  \Pr(\theta \mid y ) \propto g(\theta)^{\eta + n} \exp{\left( \phi(\theta)^T (\nu + t(y)) \right)} \tag{3}\label{eq:posterior-density}
\end{equation}$$

Actually, Equation \eqref{eq:posterior-density} is a general form which holds for vector $\phi(\theta)$ and both $\eta$ and $\nu$ are constants. Let's start computing the posterior density as follows:

$$ \begin{align}
  \Pr(\theta \mid y ) &\propto \Pr(y \mid \theta) \Pr( \theta )  \tag{4}\label{eq:posterior-start}  && \text{by Bayes Rule} \\
                      &\propto \theta^y (1- \theta)^{n-y} \, \theta^{\alpha - 1} (1 - \theta)^{\beta - 1} \\ 
                      &= \theta^{y+\alpha-1} (1 - \theta)^{n - y + \beta - 1} \\
                      &= \theta^{y+\alpha-1} \,  \frac{1}{(1 - \theta)^{-n+y-\beta +1}} \\
                      &= \frac{\theta^{\alpha-1}}{(1 - \theta)^{-n-\beta+1}} \, \frac{\theta^y}{(1-\theta)^y} && \text{by rearranging} \\
                      &= \frac{\theta^{\alpha-1}}{(1 - \theta)^{-n-\beta+1}} \, \exp{\left( \log{ \left( \frac{\theta}{1-\theta} \right)^y } \right)} \\
                      &= \theta^{\alpha-1} (1 - \theta)^{\beta-1} (1 - \theta)^n \, \exp{( y \; \text{logit}{ (\theta) } )} \\
                      &= \left( \theta^{\frac{\alpha - 1}{n}} (1 - \theta)^{\frac{\beta-1}{n}} (1-\theta)  \right)^n \, \exp{( \text{logit}{ (\theta) } \; y )} \\ 
                      &= g(\theta)^n \exp{( \phi(\theta) \; t(y) )} && \text{by referring to Equation }\eqref{eq:posterior-density}
\end{align}$$

with $g(\theta) = \left( \theta^{\frac{\alpha - 1}{n}} (1 - \theta)^{\frac{\beta-1}{n}+1} \right)$, $t(y) = y$, and $\phi(\theta) = \text{logit}(\theta)$.    
Finally, we have shown that the binomial is indeed an **exponential family** with **natural parameter** $\text{logit}(\theta)$.
 