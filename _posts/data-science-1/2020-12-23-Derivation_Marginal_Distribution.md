---
layout: post
title: Deriving Marginal Distribution from Poisson & Gamma Conjugate Pair
category: Data-Science-1
lang: EN
description: Deriving Neg-bin from BDA on page 49
sticky: true
---

This post shows the derivation of _marginal distribution_ from a **Poisson** model with **Gamma** prior distribution. Specifically, the idea comes from Chapter 2 of [_**Bayesian Data Analysis (BDA) 3rd Edition**_](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf) on page 49.    

[![img1]({{ site.baseurl }}/assets/images/highest-cancer-death-rate.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/highest-cancer-death-rate.png)*<center>$\pmb{\text{Figure 1}}$: The counties of the United States with the highest 10% age-standardized death rates for cancer of kidney/ureter for U.S. white males, 1980-1989. Image taken from <a href="http://www.stat.columbia.edu/~gelman/book/BDA3.pdf">BDA 3rd Edition</a>, some rights reserved.</center>*
     
$\text{Figure 1}$ shows that most of the shaded counties are located in the middle of the country ([**Great Plains**](https://en.wikipedia.org/wiki/Great_Plains)). 

[![img1]({{ site.baseurl }}/assets/images/lowest-cancer-death-rate.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/lowest-cancer-death-rate.png)*<center>$\pmb{\text{Figure 2}}$: The counties of the United States with the lowest 10% age-standardized death rates for cancer of kidney/ureter for U.S. white males, 1980-1989. Interestingly, the pattern is somewhat similar to the map of the highest rates in $\text{Figure 1}$. Image taken from <a href="http://www.stat.columbia.edu/~gelman/book/BDA3.pdf">BDA 3rd Edition</a>, some rights reserved.</center>*
    
Both $\text{Figure 1}$ and $\text{Figure 2}$ show that the _Great Plains_ has both the highest and lowest rates. Recall that the reason of this issue is _sample size_. _Great Plains_ has many low-population counties; therefore rare cancer death rates, such as kidney cancer, are represented in both maps. There is no evidence from both maps that cancer rates are high (please read page 47 of the [excellent book](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf) for more details). 
    
This misleading patterns in the maps of raw death rates suggest that a Poisson model-based approach to estimating the true underlying rates might be helpful. Let's construct a _likelihood_ from a Poisson distribution.
   
$$ \begin{equation}
  y_k \sim \text{Poisson}(10 \, n_j \, \theta_j) \tag{1}\label{eq:likelihood}
\end{equation}$$  
   
with $y_j$ denotes the number of kidney cancer deaths in county $j$ from 1980-1989, $n_j$ is the population of the county, and $\theta_j$ is the underlying rate in units of deaths per person per year. 

The conjugate prior for _Poisson_ model is _Gamma_ distribution with parameters $\alpha$ and $\beta$:

$$ \begin{equation}
  \theta_j \sim \text{Gamma}(\alpha, \beta). \tag{2}\label{eq:prior}
\end{equation}$$

By multiplying Equation \eqref{eq:likelihood} and \eqref{eq:prior}, we obtain the posterior

$$ \begin{equation}
  \theta_j \mid y_j \sim \text{Gamma}(\alpha + y_j, \beta + 10 \, n_j). \tag{3}\label{eq:posterior}
\end{equation}$$

