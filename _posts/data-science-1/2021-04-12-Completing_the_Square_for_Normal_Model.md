---
layout: post
title: Completing the Square for Normal Model with Multiple Observations
category: Data-Science-1
lang: EN
description: Equation (2.11) from BDA on page 42
sticky: true
---

The subchapter 2.5 of [**Bayesian Data Analysis Third Edition**](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf) explains how to estimate a normal mean with known variance; particularly, the subchapter extends the development of a normal model with a single observation into the more realistic situation where _a sample of independent and identically distributed observations_ $y = (y_1, \ldots, y_n)$ are available.       
    
[![img1]({{ site.baseurl }}/assets/images/normal-dist.jpg){:class="img-responsive"}]({{ site.baseurl }}/assets/images/normal-dist.jpg)*<center>$\pmb{\text{Figure 1}}$: Example of a normal distribution consisting a horde of rabbits. Image taken from <a href="https://vimeo.com/75089338">Casey Dunn</a>, some rights reserved.</center>*     
        
The _posterior_ density of the normal model consists of a _likelihood_ distribution, $\Pr(y \mid \theta)$, and a _prior_ distribution, $\Pr(\theta)$. Specifically,    
    
$$\begin{align}
	y_i \mid \theta &\sim \text{N}(\theta, \sigma^2) && \text{A normal distribution with mean = }\theta \text{ and variance = }\sigma^2\text{, for }i=1, \ldots, n \\
	\theta          &\sim \text{N}(\mu_0, \tau_0^2)  &&  \text{A normal distribution with mean = }\mu_0 \text{ and variance = }\tau_0^2.
\end{align}$$

Proceeding formally, the posterior density is    

$$\begin{align}
\Pr(\theta \mid y) &\propto \Pr(\theta) \Pr(y \mid \theta) && \text{posterior definition} \tag{1}\label{eq:definition}\\
                   &= \Pr(\theta) \prod_{i=1}^{n} \Pr(y_i \mid \theta) && \text{i.i.d observations} \tag{2}\label{eq:iid} \\
                   &\propto \exp \left( -\frac{1}{2 \tau_0^2} (\theta - \mu_0)^2 \right) \prod_{i=1}^n \exp \left( - \frac{1}{2 \sigma^2} (y_i - \theta)^2 \right) && \text{normal distributions} \tag{3}\label{eq:exposition-normal} \\
                   &= \exp \left( -\frac{1}{2} \left( \frac{1}{\tau_0^2} (\theta - \mu_0)^2 + \frac{1}{\sigma^2} \sum_{i=1}^{n} (y_i - \theta)^2 \right) \right)  && \text{sum all terms} \tag{4}\label{eq:sum-all-terms} \\
                   &= \exp \left( -\frac{1}{2} \left( \frac{1}{\tau_0^2} \theta^2 - \frac{2 \theta \mu_0}{\tau_0^2} + \frac{\mu_0^2}{\tau_0^2} + \frac{1}{\sigma^2} \sum_{i=1}^n (y_i^2 - 2 \theta y_i + \theta^2) \right) \right) && \text{expand all squares} \tag{5}\label{eq:expand-all} \\
                   &= \exp \left( -\frac{1}{2} \left( \frac{1}{\tau_0^2} \theta^2 - \frac{2 \theta \mu_0}{\tau_0^2} + \frac{\mu_0^2}{\tau_0^2} + \frac{\sum_{i=1}^n y_i^2}{\sigma^2} - \frac{2 \theta \sum_{i=1}^n y_i}{\sigma^2} + \frac{n \theta^2}{\sigma^2} \right) \right) && \text{expand the last term} \tag{6}\label{eq:expand-again} \\
                   &= \exp \left( -\frac{1}{2} \left( \frac{\theta^2}{\tau_0^2} + \frac{n \theta^2}{\sigma^2} - 2 \theta \left( \frac{\mu_0}{\tau_0^2} + \frac{\sum_{i=1}^n y_i}{\sigma^2} \right) + \frac{\mu_0^2}{\tau_0^2} + \frac{\sum_{i=1}^n y_i^2}{\sigma^2} \right) \right) && \text{group all }\theta s \text{ & } \theta^2 s \tag{7}\label{eq:collect-all} \\
                   &= \exp \left( -\frac{1}{2} \left( \theta^2 \left( \frac{1}{\tau_0^2} + \frac{n}{\sigma^2} \right) - 2 \theta \left( \frac{\mu_0}{\tau_0^2} + \frac{\sum_{i=1}^n y_i}{\sigma^2} \right) + \frac{\mu_0^2}{\tau_0^2} + \frac{\sum_{i=1}^n y_i^2}{\sigma^2} \right) \times \frac{\frac{1}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}}{\frac{1}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}} \right) && \text{use a trick} \tag{8}\label{eq:multiply-by} \\
                   &= \exp \left( - \frac{1}{2} \frac{  \left( \theta^2 - 2 \theta \frac{ \frac{\mu_0}{\tau_0^2} + \frac{\sum y_i}{\sigma^2}}{ \frac{1}{\tau_0^2} + \frac{n}{\sigma^2}} + \frac{\frac{\mu_0^2}{\tau_0^2}}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}  + \frac{\frac{\sum y_i^2}{\sigma^2}}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}} \right)  }{\frac{1}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}} \right) \tag{9}\label{eq:atas-bawah} \\
                   &= \exp \left( - \frac{1}{2} \frac{\left( \theta - \frac{\frac{\mu_0}{\tau_0^2} + \frac{\sum y_i}{\sigma^2} }{ \frac{1}{\tau_0^2} + \frac{n}{\sigma^2}  }  \right)^2 + C}{\frac{1}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}}   \right) && \text{with }C \text{ is a constant} \tag{10}\label{eq:a-constant} \\
                   &\propto \exp \left( -\frac{1}{2} \frac{(\theta - \mu_n)^2}{\tau_n^2} \right) \tag{10}\label{eq:almost} \\
                   &\propto \text{N}(\mu_n, \tau_n^2)  && \text{a normal distribution}        \tag{11}\label{eq:finally}         
\end{align}$$
with    

$$\begin{align}
	\mu_n &= \frac{\frac{\mu_0}{\tau_0^2} + \frac{\sum_{i=1}^n y_i}{\sigma^2}}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2} } \tag{12}\label{eq:mu-n} \\
	      &= \frac{\frac{\mu_0}{\tau_0^2} + \frac{n \bar{y}}{\sigma^2}}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2} } && \text{because }\bar{y} = \frac{\sum_{i=1}^n y_i}{n} \tag{13}\label{eq:mu-n-2}
\end{align}$$
and   

$$\begin{equation}
	\frac{1}{\tau_n^2} = \frac{1}{\tau_0^2} + \frac{n}{\sigma^2}. \tag{14}\label{eq:sigma-n}
\end{equation}$$


At last, we have shown that the _posterior_ distribution of the normal model is also a normal distribution as it is explained by Equation (2.11) and (2.12) on page 42 of the [**book**](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf).