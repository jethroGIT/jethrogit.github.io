---
layout: post
title: Predictive Distributions (BDA 3rd Edition, Chapter 2) 
category: Data-Science-1
lang: EN
description: This post explores Exercise 2 in Chapter 2
sticky: true
---

This post provides an answer for Exercise 2 from Chapter 2 of [_**Bayesian Data Analysis (BDA) 3rd Edition**_](http://www.stat.columbia.edu/~gelman/book/BDA3.pdf). Let's state the problem from the beloved book.   

Consider two coins, $C_1$ and $C_2$, with the following characteristics:     

$$\begin{align}
\text{Pr}(\text{heads}|C_1) &= 0.6, \\
\text{Pr}(\text{head}|C_2) &= 0.4.     
\end{align}$$

Choose one of the coins at random and imagine spinning it repeatedly.     
Here is the question: 

> Given that the **first two spins** from the chosen coin are **tails**, what is the **expectation of the number of additional spins until a head shows up**?

To simply our writing, we denote $\text{head}$ and $\text{tail}$ as $H$ and $T$ respectively. Therefore, we have

$$
  \begin{align*}
    C_1 &\rightarrow \text{Pr}(H|C_1) = 0.6 = \frac{3}{5}, \tag{1}\label{eq:c1}\\
    C_2 &\rightarrow \text{Pr}(H|C_2) = 0.4 = \frac{2}{5}. \tag{2}\label{eq:c2}
  \end{align*}
$$

[![img1]({{ site.baseurl }}/assets/images/the-experiment.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/the-experiment.png)*<center>$\pmb{\text{Figure 1}}$: The problem poses an experiment consisting of two steps. Specifically, $N \sim$ geometric distribution.</center>*
    

If we read the problem carefully, we may find that the problem consists of two steps as depicted in $\pmb{\text{Figure 1}}$. Particularly, random variable $N$ is a geometric distribution which has a _probability mass function_ as follows:

$$
  \begin{equation}
    \text{Pr}(n) = (1-C_i)^{n-1} C_i \tag{3}\label{eq:pmf-geometri}
  \end{equation}
$$
where $C_i$ depends on either $C_1$ or $C_2$.    
    
Now, let us compute
   $$ \begin{equation}
    \text{E}(N|TT) = ? \tag{4}\label{eq:problem} 
   \end{equation}$$
as follows:

$$
  \begin{align}
    \text{E}(N|TT) &= \int N \, \text{Pr}(N|TT) \, dN && \text{by definition} \tag{5}\label{eq:compute-1} \\ 
                   &= \int \int N \, \text{Pr}(N, C|TT) \, dC \, dN && \text{by Bayes rule} \tag{6}\label{eq:compute-2} \\ 
                   &= \int \int N \, \text{Pr}(N|TT,C) \text{Pr}(C|TT) \, dC \, dN && \text{by conditional probability} \tag{7}\label{eq:compute-3} \\ 
                   &= \int \underbrace{\int N \, \text{Pr}(N|TT,C) \, dN}_{\text{E}(N|TT, C)} \, \text{Pr}(C|TT) \, dC && \text{just rearranging} \tag{8}\label{eq:compute-4} \\
                   &= \int \text{E}(N|TT, C) \, \text{Pr}(C|TT) \, dC && \text{by expectation definition} \tag{9}\label{eq:compute-5} \\
                   &= \sum_{i=1}^2 \text{E}(N|TT, C_i) \, \text{Pr}(C_i|TT) && \text{since }C \text{ is discrete .}   \tag{10}\label{eq:compute-6}                   
  \end{align}
$$

Recall that $N \sim$ geometric distribution; therefore, 

$$
  \begin{align}
    \text{E}(N | TT, C_i) &= \text{E}(N | C_i) && \text{whether we have }TT\text{ as conditional or not} \tag{11}\label{eq:expectation-1} \\
                          &= \frac{1}{C_i}         \tag{12}\label{eq:expectation-2}.
  \end{align}
$$

We proceed from Equation \eqref{eq:compute-6} as follows:

$$ \begin{align}
  \text{E}(N | TT) &= \text{E}(N | TT, C_1) \, \text{Pr}(C_1 | TT) +  \text{E}(N | TT, C_2) \, \text{Pr}(C_2 | TT) \tag{13}\label{eq:final-1} \\
                   &= \frac{1}{C_1} \text{Pr}(C_1 | TT) +  \frac{1}{C_2} \text{Pr}(C_2 | TT) \tag{14}\label{eq:final-2}   \\
                   &= \frac{1}{C_1} \underbrace{\frac{\text{Pr}(TT|C_1) \, \text{Pr}(C_1)}{\text{Pr}(TT)}}_{\text{Part 1}} +  \frac{1}{C_2}  \underbrace{\frac{\text{Pr}(TT|C_2) \, \text{Pr}(C_2)}{\text{Pr}(TT)}}_{\text{Part 2}} \tag{15}\label{eq:final-3}   \\
\end{align}
$$

Next, let's compute $\text{Part 1}$ as follows:

$$\begin{align}
  \frac{\text{Pr}(TT|C_1) \, \text{Pr}(C_1)}{\text{Pr}(TT)} &= \frac{\text{Pr}(TT|C_1) \, \text{Pr}(C_1)}{\text{Pr}(TT|C_1) \, \text{Pr}(C_1) + \text{Pr}(TT|C_2) \, \text{Pr}(C_2)} && \text{expanding Pr}(TT) \tag{16}\label{eq:part-1-1} \\
     &= \frac{\left( \frac{2}{5} \right) \left( \frac{2}{5} \right) \left(\frac{1}{2} \right)}{\left( \frac{2}{5} \right) \left( \frac{2}{5} \right) \left( \frac{1}{2} \right) + \left( \frac{3}{5} \right) \left( \frac{3}{5} \right) \left( \frac{1}{2} \right)}. \tag{17}\label{eq:part-1-2} \\
\end{align}$$

Subsequently, we also calculate $\text{Part 2}$ similarly as follows:

$$\begin{align}
  \frac{\text{Pr}(TT|C_2) \, \text{Pr}(C_2)}{\text{Pr}(TT)} &= \frac{\text{Pr}(TT|C_2) \, \text{Pr}(C_2)}{\text{Pr}(TT|C_1) \, \text{Pr}(C_1) + \text{Pr}(TT|C_2) \, \text{Pr}(C_2)} && \text{expanding Pr}(TT) \tag{18}\label{eq:part-2-1} \\
     &= \frac{\left( \frac{3}{5} \right) \left( \frac{3}{5} \right) \left( \frac{1}{2} \right) }{ \left( \frac{2}{5} \right) \left( \frac{2}{5} \right) \left( \frac{1}{2} \right) + \left( \frac{3}{5} \right) \left( \frac{3}{5} \right) \left( \frac{1}{2} \right) }. \tag{19}\label{eq:part-2-2} \\
\end{align}$$

Finally, we are able to compute Equation \eqref{eq:problem} as

$$ \begin{align}
  \text{E}(N|TT) &= \frac{1}{C_1} \, \text{Part 1} + \frac{1}{C_2} \, \text{Part 2} \tag{20}\label{eq:final-answer}\\
                 &= \frac{1}{3/5} \, \text{Part 1} + \frac{1}{2/5} \, \text{Part 2} \\
                 &= 2.2436   && \text{utilizing Eq. }\eqref{eq:part-1-2}\text{ and Eq. }\eqref{eq:part-2-2} \\
                 &\approx 2.
\end{align}$$

This means that in order to find a head after we have two **tails** regardless the coin we choose, we need $2$ more throws on average. 