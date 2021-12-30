---
layout: post
title: The Posterior Mode of Beta Distribution
category: Data-Science-2
lang: EN
description: Exercise 4.14 from Bayes Rules!
sticky: true
---

This article answers **Exercise 4.14** from the _highly recommended_ [**Bayes Rules!**](https://www.bayesrulesbook.com/chapter-4.html#practice-balancing-the-data-prior) book.     

[![img1]({{ site.baseurl }}/assets/images/bechdel-test.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/bechdel-test.png)*<center>$\pmb{\text{Figure 1}}$: The Bechdel Test. Image taken from <a href="https://commons.wikimedia.org/wiki/File:Bechdel_test.png">Wikipedia</a>.</center>*    

In [Chapter 4 of the book](https://www.bayesrulesbook.com/chapter-4.html#ch4-priors), recall that the **Bechdel test** is satisfied by a movie whose conditions are as follows:
-  the movie has at least two women in it,
-  these two women talk to each other, and 
-  the two women also talk about something other than a man.
    
$\text{Figure 1}$ summarizes the three rules mentioned before.     
    
Suppose that we review a sample of $n$ recent movies and record $Y$, the number of movies that pass the Bechdel test. Considering $Y$ as the number of "successes" in a fixed number of independence trials, $Y$ can be specified as a Binomial model with $\pi$ as its parameter. Moreover, $\pi$ can also be described as Beta distribution with prior hyperparameters $\alpha$ and $\beta$:

$$\begin{align}
    Y \mid \pi &\sim \text{Bin}(n,\pi)  \\
    \pi        &\sim \text{Beta}(\alpha, \beta).
\end{align}$$    
   
Thus, the posterior of Beta-Binomial model of $\pi$ is given by

$$\begin{equation}
    \pi \mid (Y = y) \sim \text{Beta}(\alpha + y, \beta + n - y). \tag{1}\label{eq:the-posterior}
\end{equation}$$      
     

**The Question:**
> In the Beta-Binomial setting, show that we can write the posterior mode of $\pi$ as the weighted average of the prior mode and observed sample success rate:
$$\begin{equation}
    \text{Mode}(\pi \mid Y = y) = \frac{\alpha + \beta - 2}{\alpha + \beta + n - 2} \cdot \text{Mode}(\pi) + \frac{n}{\alpha + \beta + n - 2} \cdot \frac{y}{n} \tag{2}\label{eq:the-problem} 
\end{equation}$$      

**Answer**:     
Recall that mode of the prior is      

$$\begin{equation}
    \text{Mode}(\pi) = \frac{\alpha - 1}{\alpha + \beta - 2} \tag{3}\label{eq:mode-prior} 
\end{equation}$$ 

and mode of the posterior is    

$$\begin{equation}
    \text{Mode}(\pi \mid Y = y) = \frac{\alpha + y - 1}{\alpha + \beta + n -2}. \tag{4}\label{eq:mode-posterior} 
\end{equation}$$

Next, we show that Equation \eqref{eq:mode-posterior} can be written as Equation \eqref{eq:the-problem} as follows:

$$\begin{align}
    \text{Mode}(\pi \mid Y = y) &= \frac{\alpha + y - 1}{\alpha + \beta + n -2} \\
                                &= \frac{\alpha - 1}{\alpha + \beta + n - 2} + \frac{y}{\alpha + \beta + n - 2}  \\
                                &= \frac{\alpha - 1}{\alpha + \beta + n - 2} \cdot \frac{\alpha + \beta -2}{\alpha + \beta -2} + \frac{y}{\alpha + \beta + n - 2} \cdot \frac{n}{n} \\
                                &= \frac{\alpha + \beta -2}{\alpha + \beta + n - 2} \cdot \frac{\alpha - 1}{\alpha + \beta -2} + \frac{n}{\alpha + \beta + n - 2} \cdot \frac{y}{n}  && \text{Rearrange the terms} \\
                                &= \frac{\alpha + \beta -2}{\alpha + \beta + n - 2} \cdot \text{Mode}(\pi) + \frac{n}{\alpha + \beta + n - 2} \cdot \frac{y}{n}. && \text{Utilize Equation }\eqref{eq:mode-prior}
\end{align}$$
    
At last, we have shown that Equation \eqref{eq:the-problem} is indeed true.