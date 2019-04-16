---
layout: post
title: Menghitung Gradient dari Cost Function Logistic Regression
category: Machine-Learning
lang: ID
description: Menghitung turunan parsial cost function dari Logistic Regression 
sticky: true
---

Diberikan suatu _design matrix_ $X$ yang berbentuk

$$ \begin{equation} X = \begin{bmatrix} 1 & x^{(1)} \\
1      & x^{(2)} \\
\vdots & \vdots  \\
1      & x^{(m)}   \end{bmatrix}.  \end{equation} \tag{1}\label{eq:x-dataset}$$

Jadi _design matrix_ $X$ memiliki $m$ _training examples_ dan 1 _feature_, $x$.    

Model **logistic regression** akan dilatih terhadap dataset $X$ ini. Perkuliahan [_Machine Learning_](https://www.coursera.org/learn/machine-learning/home/welcome) di minggu ke-4 membahas model **logistic regression** yang memiliki bentuk

$$ \require{cancel} \begin{equation} h_{\theta}(x^{(i)}) = \frac{1}{1 + e^{-\theta_0 - \theta_1 x^{(i)}}}. \tag{2}\label{eq:model-logistic}\end{equation} $$

Lebih lanjut, model **logistic regression** memiliki _cost function_ $J(\theta)$ sebagai berikut:

$$ \begin{equation} J(\theta) = \frac{1}{m} \sum_{i=1}^{m} \text{Cost}(h_{\theta}(x^{(i)}), y^{(i)}) \tag{3}\label{eq:cost-function} \end{equation}  $$    

dengan 

$$ \begin{equation} \text{Cost}(h_{\theta}(x^{(i)}), y^{(i)}) = -y^{(i)} \log( h_{\theta}(x^{(i)}) ) - (1-y^{(i)}) \log(1-h_{\theta}(x^{(i)})) \end{equation} \tag{4}\label{eq:cost-logistic} $$   

dan diketahui juga bahwa $x^{(i)}$ adalah _training example_ ke-$i$, dan $y^{(i)}$ adalah label atau class dari _training example_ $x^{(i)}$.   
Tulisan ini hendak menjelaskan bagaimana menghitung turunan parsial dari _cost function_ model **logistic regression** terhadap $\theta_0$ dan $\theta_1$. Turunan parsial ini juga sering disebut dengan _gradient_, $\frac{\partial J}{\partial \theta}$.    
<br/>
#### **Bentuk Komplit _Cost Function_ dari Model Logistic Regression**
Dengan menggabungkan Persamaan \eqref{eq:cost-function} dan \eqref{eq:cost-logistic} diperoleh _cost function_ yang detil sebagai berikut: 

$$ \begin{align} J(\theta) &= \frac{1}{m} \sum_{i=1}^{m} \text{Cost}(h_{\theta}(x^{(i)}), y^{(i)}) \\
                           &= \frac{1}{m} \sum_{i=1}^{m} \left( -y^{(i)} \log (h_{\theta}(x^{(i)})) - (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \\
                           &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right). \tag{5}\label{eq:cost-function-complete} \end{align} $$

Selanjutnya, akan dicari $\frac{\partial J}{\partial \theta_0}$ dan $\frac{\partial J}{\partial \theta_1}$ tetapi sebelumnya, kita perlu menghitung $\frac{\partial h_{\theta}}{ \partial \theta_0 }$ dan $\frac{\partial h_{\theta}}{ \partial \theta_1 }$.   
Sekarang kita akan menghitung turunan partial dari $h_{\theta}(x)$ terhadap $\theta_0$ atau $\frac{\partial h_{\theta}}{ \partial \theta_0 }$.   
Dari pelajaran **Kalkulus**, diketahui bahwa turunan dari $\frac{u(x)}{v(x)}$  dengan masing-masing $u(x)$ dan $v(x)$ merupakan fungsi dari $x$ adalah 

$$ \begin{equation} \frac{u^{\prime} v - u v^{\prime} }{ v^2 }. \tag{6}\label{eq:formula-derivatif} \end{equation}$$

dengan $u^{\prime}$ adalah turunan pertama fungsi $u$ dan $v^{\prime}$ adalah turunan pertama fungsi $v$.   
Kita akan menggunakan formula turunan di Persamaan \eqref{eq:formula-derivatif} untuk menghitung $\frac{\partial h_{\theta}}{ \partial \theta_0 }$ dan $\frac{\partial h_{\theta}}{ \partial \theta_1 }$ sebagai berikut:

$$ \begin{align} \frac{\partial h_{\theta}}{ \partial \theta_0 } &= \frac{0 + e^{-\theta_0 - \theta_1 x}}{(1 + e^{-\theta_0 - \theta_1 x})^2} = \frac{e^{-\theta_0 - \theta_1 x}}{(1 + e^{-\theta_0 - \theta_1 x})^2} \\ 
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( \frac{e^{-\theta_0 - \theta_1 x}}{1 + e^{-\theta_0 - \theta_1 x}} \right)  \\
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( 1 - \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \\
 &= h_\theta(x) (1 - h_\theta(x)) \tag{7}\label{eq:formula-derivatif-theta0}
  \end{align}$$

dan 

$$ \begin{align} \frac{\partial h_{\theta}}{ \partial \theta_1 } &= \frac{0 + e^{-\theta_0 - \theta_1 x} x}{(1 + e^{-\theta_0 - \theta_1 x})^2} = \frac{e^{-\theta_0 - \theta_1 x} x}{(1 + e^{-\theta_0 - \theta_1 x})^2} \\ 
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( \frac{e^{-\theta_0 - \theta_1 x}}{1 + e^{-\theta_0 - \theta_1 x}} \right)x  \\
 &= \left( \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right) \left( 1 - \frac{1}{1 + e^{-\theta_0 - \theta_1 x}} \right)x \\
 &= h_\theta(x) (1 - h_\theta(x)) x. \tag{8}\label{eq:formula-derivatif-theta1}
  \end{align} $$    
<br/>
#### **Menghitung $\frac{\partial J}{\partial \theta_0}$**    
Turunan parsial $\frac{\partial J}{\partial \theta_0}$ dapat dihitung sbb:

$$ \begin{align} \frac{\partial J}{\partial \theta_0} &= \frac{\partial }{\partial \theta_0} \left( -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \frac{\partial }{\partial \theta_0} \left( \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_0} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Bagian I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_0} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Bagian II}} \right). \tag{9}\label{eq:bagian2-theta0} \end{align} $$

 Bagian I dari Persamaan \eqref{eq:bagian2-theta0} dihitung dengan teknik aturan rantai (_chain rule_) dan hasil Persamaan \eqref{eq:formula-derivatif-theta0} menjadi sebagai berikut:

 $$ \begin{align} \frac{\partial }{\partial \theta_0} \left( \log (h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log (h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_0} \\
 &= \frac{1}{h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) \\
 &= \frac{1}{ \cancel{h_{\theta}(x^{(i)})} } \cancel{h_\theta(x^{(i)})} (1 - h_\theta(x^{(i)}))  \\
 &= (1 - h_\theta(x^{(i)})). \tag{10}\label{eq:bagian-I-theta0} \end{align} $$

Bagian II dari Persamaan \eqref{eq:bagian2-theta0} juga dihitung dengan teknik aturan rantai dan hasil Persamaan \eqref{eq:formula-derivatif-theta0}menjadi sebagai berikut:

 $$ \begin{align} \frac{\partial }{\partial \theta_0} \left( \log (1 - h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log ( 1- h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_0} \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} (1 - h_\theta(x^{(i)})) h_\theta(x^{(i)})  \\
 &= - \frac{1}{ \cancel{1 - h_{\theta}(x^{(i)})} } \cancel{(1- h_\theta(x^{(i)}))} h_\theta(x^{(i)})  \\
 &= -h_\theta(x^{(i)}). \tag{11}\label{eq:bagian-II-theta0} \end{align} $$

 Dengan mensubstitusi Persamaan \eqref{eq:bagian-I-theta0} dan Persamaan \eqref{eq:bagian-II-theta0} ke Persamaan \eqref{eq:bagian2-theta0} diperoleh

$$ \begin{align} \frac{\partial J}{\partial \theta_0} &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_0} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Bagian I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_0} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Bagian II}} \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} (1 - h_{\theta}(x^{(i)}))  - (1-y^{(i)}) h_{\theta}(x^{(i)}) \right)  \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} - y^{(i)} h_{\theta}(x^{(i)})  - h_{\theta}(x^{(i)}) + y^{(i)} h_{\theta}(x^{(i)}) \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \cancel{- y^{(i)} h_{\theta}(x^{(i)})}  - h_{\theta}(x^{(i)}) \cancel{+ y^{(i)} h_{\theta}(x^{(i)})} \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} ( y^{(i)} - h_{\theta}(x^{(i)}) )  \\
&= \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ). \end{align} $$    
<br/>
#### **Menghitung $\frac{\partial J}{\partial \theta_1}$**    
Turunan parsial $\frac{\partial J}{\partial \theta_1}$ dapat dihitung dengan cara yang sama sbb:

$$ \begin{align} \frac{\partial J}{\partial \theta_1} &= \frac{\partial }{\partial \theta_1} \left( -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \frac{\partial }{\partial \theta_1} \left( \sum_{i=1}^{m} \left( y^{(i)} \log (h_{\theta}(x^{(i)})) + (1-y^{(i)}) \log (1 - h_{\theta}(x^{(i)})) \right) \right) \\
 &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_1} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Bagian I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_1} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Bagian II}} \right). \tag{12}\label{eq:bagian2-theta1} \end{align} $$

 Bagian I dari Persamaan \eqref{eq:bagian2-theta1} dihitung dengan teknik aturan rantai (_chain rule_) dan hasil Persamaan \eqref{eq:formula-derivatif-theta1} menjadi sebagai berikut:

 $$ \begin{align} \frac{\partial }{\partial \theta_1} \left( \log (h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log (h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_1} \\
 &= \frac{1}{h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) x^{(i)} \\
 &= \frac{1}{ \cancel{h_{\theta}(x^{(i)})} } \cancel{h_\theta(x^{(i)})} (1 - h_\theta(x^{(i)})) x^{(i)} \\
 &= (1 - h_\theta(x^{(i)})) x^{(i)}. \tag{13}\label{eq:bagian-I-theta1} \end{align} $$

Bagian II dari Persamaan \eqref{eq:bagian2-theta1} juga dihitung dengan teknik aturan rantai dan hasil Persamaan \eqref{eq:formula-derivatif-theta1}menjadi sebagai berikut:

 $$ \begin{align} \frac{\partial }{\partial \theta_1} \left( \log (1 - h_{\theta}(x^{(i)})) \right) &= \frac{\partial }{\partial h_{\theta} } \left( \log ( 1- h_{\theta}(x^{(i)})) \right) \frac{\partial h_{\theta}}{\partial \theta_1} \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) x^{(i)} \\
 &= - \frac{1}{1 - h_{\theta}(x^{(i)})} (1 - h_\theta(x^{(i)})) h_\theta(x^{(i)}) x^{(i)}  \\
 &= - \frac{1}{ \cancel{1 - h_{\theta}(x^{(i)})} } \cancel{(1- h_\theta(x^{(i)}))} h_\theta(x^{(i)}) x^{(i)}  \\
 &= -h_\theta(x^{(i)}) x^{(i)}. \tag{14}\label{eq:bagian-II-theta1} \end{align} $$

Kembali dengan mensubstitusi Persamaan \eqref{eq:bagian-I-theta1} dan Persamaan \eqref{eq:bagian-II-theta1} ke Persamaan \eqref{eq:bagian2-theta1} diperoleh

$$ \begin{align} \frac{\partial J}{\partial \theta_1} &= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \underbrace{\frac{\partial }{\partial \theta_1} \left( \log (h_{\theta}(x^{(i)})) \right)}_{\text{Bagian I}}  + (1-y^{(i)}) \underbrace{\frac{\partial }{\partial \theta_1} \left(\log (1 - h_{\theta}(x^{(i)})) \right)}_{\text{Bagian II}} \right) \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} (1 - h_{\theta}(x^{(i)})) x^{(i)}  - (1-y^{(i)}) h_{\theta}(x^{(i)}) x^{(i)} \right)  \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} - y^{(i)} h_{\theta}(x^{(i)})  - h_{\theta}(x^{(i)}) + y^{(i)} h_{\theta}(x^{(i)}) \right) x^{(i)} \\
&= -\frac{1}{m} \sum_{i=1}^{m} \left( y^{(i)} \cancel{- y^{(i)} h_{\theta}(x^{(i)})}  - h_{\theta}(x^{(i)}) \cancel{+ y^{(i)} h_{\theta}(x^{(i)})} \right) x^{(i)} \\
&= -\frac{1}{m} \sum_{i=1}^{m} ( y^{(i)} - h_{\theta}(x^{(i)}) ) x^{(i)}   \\
&= \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ) x^{(i)}.  \end{align} $$    

Jadi _gradient_ untuk model **logistic regression** dengan 1 variabel, $x$ dan 2 parameter, $\theta_0$ dan $\theta_1$ adalah

$$ \begin{equation} \frac{\partial J}{\partial \theta_0} = \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} )  \end{equation} $$ 

dan 

$$ \begin{equation} \frac{\partial J}{\partial \theta_1} = \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ) x^{(i)} . \end{equation} $$ 

Secara umum, _gradient_ untuk model **logistic regression** dengan $n$ variabel, $x_1, x_2, \ldots, x_n$ dan $n+1$ parameter, $\theta_0, \theta_1, \ldots, \theta_n$ adalah

$$ $$ \begin{equation} \frac{\partial J}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} ( h_{\theta}(x^{(i)}) - y^{(i)} ) x_{j}^{(i)}  \end{equation} $$ 
 $$

dengan ketika $j=0$, $x_0^{(i)} = 1$ untuk $i = 1, 2, \ldots, m$.
