---
layout: post
title: Membangun Model Logistic Regression dari Linear Regression
category: Machine-Learning
lang: ID
description: Hubungan logistic regression dan linear regression
sticky: false
---

Dalam perkuliahan [_Machine Learning_ yang dibawakan oleh Andrew Ng](https://www.coursera.org/learn/machine-learning/home/welcome) di minggu ke-4 dibahas mengenai sebuah model yang bernama model **logistic regression**. Tulisan ini hendak menjelaskan bagaimana memperoleh model **logistic regression** tersebut dari model **linear regression** yang dijelaskan di minggu ke-1 dan ke-2.

Seperti yang dijelaskan di minggu ke-1 bahwa model _linear regression_ merupakan model untuk menyelesaikan masalah klasifikasi (_classification problem_) dengan model prediksi (_hypothesis_) adalah   

$$ \begin{equation} \bbox[5px,border:2px solid blue] {h_\theta(x) = \theta^T x} \tag{1}\label{eq:linear-regression} \end{equation} $$

dengan $$ \theta = \begin{bmatrix} \theta_0 & \theta_1 & \theta_2 & \cdots & \theta_n \end{bmatrix}^T $$ adalah parameter model dan $$ x = \begin{bmatrix} 1 & x_1 & x_2 & \cdots & x_n \end{bmatrix}^T $$ adalah _instance_ atau data yang hendak diprediksi $$y$$-nya.    

Bagaimanakah model **logistic regression** dapat diperoleh dari model _linear regression_ ini?     
Seperti yang kita ketahui $ h_\theta(x) $ dalam **logistic regression** memiliki range nilai antara $0$ dan $1$ sedangkan $ h_\theta(x) $ dalam _linear regression_ memiliki range nilai antara $-\infty$ dan $\infty$. Oleh karena itu, $ h_\theta(x) $ kepunyaan **logistic regression** perlu dikonversi menjadi $-\infty < h_\theta(x) < \infty$ dan disubstitusi ke dalam Persamaan \eqref{eq:linear-regression}.   

Marilah kita memulai mengkonversi $ h_\theta(x) $ kepunyaan **logistic regression** dan kemudian mensubstitusi $ h_\theta(x) $ yang sudah dikonversi ke Persamaan \eqref{eq:linear-regression}.    

$$ \begin{align}  0 < h_\theta(x) < 1 &\Longleftrightarrow  0 < \frac{h_\theta(x)}{1-h_\theta(x)} <  \infty \tag{2}\label{eq:odds-ratio} \\ 
	                    &\Longleftrightarrow  -\infty < \log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right) < \infty \tag{3}\label{eq:logit}.  \end{align} $$

$\frac{h_\theta(x)}{1-h_\theta(x)}$ di Persamaan \eqref{eq:odds-ratio} disebut **odds ratio** dan $\log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right)$ di Persamaan \eqref{eq:logit} disebut fungsi **logit** [(Raschka & Mirjalili, 2017)](https://www.packtpub.com/big-data-and-business-intelligence/python-machine-learning-second-edition).    

Oleh karena $ h_\theta(x) $ kepunyaan **logistic regression** sekarang sudah memiliki range antara $-\infty < h_\theta(x) < \infty$, $ h_\theta(x) $ ini dapat disubstitusi ke Persamaan \eqref{eq:linear-regression} menjadi

$$ \begin{align} \log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right) = \theta^T x &\Longleftrightarrow e^{\log \left( \frac{h_\theta(x)}{1-h_\theta(x)} \right)} = e^{\theta^T x}   \\
	     &\Longleftrightarrow  \frac{h_\theta(x)}{1-h_\theta(x)} = e^{\theta^T x} \\
	     &\Longleftrightarrow  h_\theta(x) = e^{\theta^T x} - h_\theta(x) e^{\theta^T x}  \\
	     &\Longleftrightarrow  h_\theta(x) + h_\theta(x) e^{\theta^T x} = e^{\theta^T x}   \\ 
	     &\Longleftrightarrow  h_\theta(x) \left( 1 + e^{\theta^T x} \right) = e^{\theta^T x} \\
	     &\Longleftrightarrow  h_\theta(x) = \frac{e^{\theta^T x}}{1 + e^{\theta^T x}}  \\
	     &\Longleftrightarrow  h_\theta(x) = \frac{e^{\theta^T x}}{1 + e^{\theta^T x}}  \times \frac{e^{-\theta^T x}}{e^{-\theta^T x}} \\
	     &\Longleftrightarrow h_\theta(x) = \frac{1}{1+e^{-\theta^T x}}.
	\end{align} $$

Jadi model **logistic regression** yang diperoleh adalah   

$$ \begin{equation} \bbox[5px,border:2px solid blue] {h_\theta(x) = \frac{1}{1+e^{-\theta^T x}}} \tag{4}\label{eq:sigmoid} \end{equation} $$

Model **logistic regression** pada Persamaan \eqref{eq:sigmoid} juga disebut **fungsi sigmoid**. Akhirnya, kita berhasil memperoleh model **logistic regression** (Persamaan \eqref{eq:sigmoid}) dari model _linear regression_ (Persamaan \eqref{eq:linear-regression}).
