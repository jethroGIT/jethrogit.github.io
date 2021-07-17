---
layout: post
title: One of Many Inverse Theorems
category: Linear-Algebra
lang: EN
description: An inverse theorem
sticky: true
---

This article is inspired by [_a website_](http://fourier.eng.hmc.edu/e161/lectures/gaussianprocess/node7.html), which is unfortunately has been down since around July 8, 2021. The website elaborately explained that both **marginal distributions** and **conditional distributions** of _subvector of multivariate normal random variables_ given _the remaining elements_ are indeed **multivariate normal distributions** as well. I feel obliged to write the content of the broken website in a blog which, hopefully, every learner can learn and benefit.       

Before we show the previous statement is indeed true, there is the inverse of a matrix theorem which needs explaining.       

Is that true that      

$$\begin{equation}
	(A + CBD)^{-1} = A^{-1} - A^{-1} C (B^{-1} + DA^{-1} C)^{-1} D A^{-1}?  \tag{1}\label{eq:the-theorem} 
\end{equation}$$    

#### _Proof:_    
We need to prove that     

$$\begin{equation}
	(A + CBD)(A + CBD)^{-1} = I  \tag{2}\label{eq:first-part} 
\end{equation}$$    
   
and    
   
$$\begin{equation}
	(A + CBD)^{-1}(A + CBD) = I  \tag{3}\label{eq:second-part} 
\end{equation}$$    
   
where $I$ is an identity matrix.     
   
> We need to prove both Eq. \eqref{eq:first-part} and Eq. \eqref{eq:second-part}
    
Firstly, let's prove Eq. \eqref{eq:first-part} by using Eq. \eqref{eq:the-theorem} as follows:

$$\begin{align}
	(A + CBD)(A + CBD)^{-1} &= (A + CBD)(A^{-1} - A^{-1} C (B^{-1} + D A^{-1} C)^{-1} D A^{-1}) \\
	                        &= (A + CBD)A^{-1} - (A + CBD) A^{-1} C (B^{-1} + D A^{-1} C)^{-1} D A^{-1} \\
	                        &= I + CBDA^{-1} - (C + CBDA^{-1}C)(B^{-1} + DA^{-1}C)^{-1}DA^{-1} \\
	                        &= I + CBDA^{-1} - CB(B^{-1} + DA^{-1}C)(B^{-1} + DA^{-1}C)^{-1}DA^{-1} \\
	                        &= I + CBDA^{-1} - CBDA^{-1} \\
	                        &= I.	                        
\end{align}$$     
   
Secondly, let's prove Eq. \eqref{eq:second-part} by employing Eq. \eqref{eq:the-theorem},    
   
$$\begin{align}
	(A + CBD)^{-1}(A + CBD) &= (A^{-1} - A^{-1} C (B^{-1} + D A^{-1} C)^{-1} D A^{-1})(A+CBD) \\
	                        &= A^{-1}(A + CBD) - A^{-1} C(B^{-1} + DA^{-1} C)^{-1} DA^{-1} (A + CBD) \\
	                        &= I + A^{-1} CBD - A^{-1} C (B^{-1} + DA^{-1} C)^{-1} (D + DA^{-1} CBD) \\
	                        &= I + A^{-1}CBD - A^{-1}C \underbrace{(B^{-1} + DA^{-1}C)^{-1} (B^{-1} + DA^{-1}C)}_{I} BD \\
	                        &= I + A^{-1}CBD - A^{-1}CBD \\
	                        &= I.
\end{align}$$   
   
Therefore, we have shown that this inverse theorem, Eq. \eqref{eq:the-theorem} is true.    