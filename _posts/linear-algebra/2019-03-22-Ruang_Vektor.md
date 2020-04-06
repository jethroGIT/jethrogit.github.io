---
layout: post
title: Contoh Pembuktian Ruang Vektor dengan sangat Detil
category: Linear-Algebra
lang: ID
description: Contoh pembuktikan suatu himpunan merupakan ruang vektor
---

Tunjukkan bahwa himpunan dari semua matriks berukuran $2 \times 3$ beserta operasi _matrix addition_ dan _scalar multiplication_ merupakan sebuah **ruang vektor**.    
       
**Bukti**:   
Misalkan himpunan dari semua matriks berukuran $2 \times 3$ beserta operasi _matrix addition_ dan _scalar multiplication_ adalah $V$.      

Diketahui juga $A$, $B$, dan $C$ adalah matriks berukuran $2 \times 3$ dan $k$, $l$ adalah skalar dengan spesifikasi sebagai berikut:   

$$ A = \begin{bmatrix}a_{11} & a_{12} & a_{13}\\a_{21} & a_{22} & a_{23}\end{bmatrix}$$, $$B = \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23}\end{bmatrix}$$, dan $$C = \begin{bmatrix} 	c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22} & c_{23} \end{bmatrix} $$.    

[Larson](https://www.amazon.com/Elementary-Linear-Algebra-Ron-Larson/dp/1305658000/) (2016) subbab 4.2 hlm. 161 menyatakan bahwa pembuktian suatu himpunan merupakan ruang vektor harus memenuhi 10 aksioma. Berikut akan dibuktikan untuk 10 aksioma tersebut.
1. Apakah $A+B$ juga ada di dalam $V$?    
Ya karena     
$$
\begin{align}
    A + B &= \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix} + \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23} \end{bmatrix}  \\
          &= \begin{bmatrix} 	a_{11}+b_{11} & a_{12}+b_{12} & a_{13}+b_{13} \\ a_{21}+b_{21} & a_{22}+b_{22} & a_{23}+b_{23}	 \end{bmatrix}.
\end{align}
$$    
<br/>
$$\begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} & a_{13}+b_{13} \\
	a_{21}+b_{21} & a_{22}+b_{22} & a_{23}+b_{23} \end{bmatrix}$$ merupakan matriks berukuran $2 \times 3 $, berarti $A+B$ juga ada di dalam $V$.    
<br/>
2. Apakah $A+B = B+A$?    
Ya karena    
$$\begin{align} A+B &= \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} +  \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\
	b_{21} & b_{22} & b_{23} \end{bmatrix} \\
                    &= \begin{bmatrix}  a_{11}+b_{11} & a_{12}+b_{12} & a_{13}+b_{13} \\
	a_{21}+b_{21} & a_{22}+b_{22} & a_{23}+b_{23}	
 \end{bmatrix} \\
                    &= \begin{bmatrix} 	b_{11}+a_{11} & b_{12}+a_{12} & b_{13}+a_{13} \\
	b_{21}+a_{21} & b_{22}+a_{22} & b_{23}+a_{23} \end{bmatrix} \\
                    &= \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\
	b_{21} & b_{22} & b_{23} \end{bmatrix} + \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} \\
                    &= B + A.
\end{align}$$        
<br/>
3. Apakah $A + (B + C) = (A+B) + C$?    
Ya karena    
$$ \begin{align} A+(B+C) &= \begin{bmatrix} a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \left( \begin{bmatrix} b_{11} & b_{12} & b_{13} \\
	b_{21} & b_{22} & b_{23} \end{bmatrix} + \begin{bmatrix} c_{11} & c_{12} & c_{13} \\
	c_{21} & c_{22} & c_{23} \end{bmatrix} \right) \\
                         &= \begin{bmatrix} a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \left( \begin{bmatrix} b_{11} + c_{11} & b_{12} + c_{12} & b_{13} + c_{13} \\
	b_{21} + c_{21} & b_{22} + c_{22} & b_{23} + c_{23}	\end{bmatrix} \right) \\
	                     &= \begin{bmatrix} a_{11} + b_{11} + c_{11}  & a_{12} + b_{12} + c_{12} & a_{13} + b_{13} + c_{13} \\
	a_{21} + b_{21} + c_{21}  & a_{22} + b_{22} + c_{22} & a_{23} + b_{23} + c_{23} \end{bmatrix} \\
	                     &= \begin{bmatrix} a_{11} + b_{11} & a_{12} + b_{12} & a_{13} + b_{13} \\
	a_{21} + b_{21} & a_{22} + b_{22} & a_{23} + b_{23} \end{bmatrix} + \begin{bmatrix} 	 c_{11} &  c_{12} &  c_{13} \\
	c_{21} & c_{22} & c_{23} \end{bmatrix} \\
	                     &= \left( \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\
	b_{21} & b_{22} & b_{23}	  \end{bmatrix} \right) + \begin{bmatrix} 	c_{11} & c_{12} & c_{13} \\
	c_{21} & c_{22} & c_{23}	  \end{bmatrix} \\
	                     &= (A+B)+C.
	 \end{align}
$$     
<br/>     
4. Apakah $V$ mempunyai **matriks nol** $\textbf{0}$ sedemikian sehingga untuk setiap matriks $A$ di $V$, $A + \textbf{0} = A$?    
Ada, matriks $\mathbf{0}$ tersebut adalah    
$$  \begin{bmatrix} 0 & 0 & 0 \\
		0 & 0 & 0 \end{bmatrix}$$ karena
		$$ 	A + \mathbf{0} = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \begin{bmatrix} 0 & 0 & 0 \\
		0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} = A.
		$$    
<br/>
5. Untuk setiap matriks $A$ di dalam $V$, apakah $V$ mempunyai matriks yang dilambangkan dengan $-A$ sedemikian sehingga $A + (-A) = \mathbf{0}$?   
Ada, matriks $-A$ tersebut adalah 
$$ \begin{bmatrix} -a_{11} & -a_{12} & -a_{13} \\
	-a_{21} & -a_{22} & -a_{23} \end{bmatrix}$$	karena
	$$ \begin{align} A + (-A) &= \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \begin{bmatrix} 	-a_{11} & -a_{12} & -a_{13} \\
	-a_{21} & -a_{22} & -a_{23} \end{bmatrix} \\
	                          &= \begin{bmatrix} 	a_{11}-a_{11} & a_{12}-a_{12} & a_{13}-a_{13} \\
	a_{21}-a_{21} & a_{22}-a_{22} & a_{23}-a_{23} \end{bmatrix} \\
	                          &= \begin{bmatrix} 		0 & 0 & 0 \\
		0 & 0 & 0 \end{bmatrix} \\
		                      &= \mathbf{0}.
	\end{align}
	$$	  
<br/>	
6. Apakah $kA$ juga ada di dalam $V$?    
Ya, karena
$$ kA = k \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23}
 \end{bmatrix} = \begin{bmatrix} 	ka_{11} & ka_{12} & ka_{13} \\
	ka_{21} & ka_{22} & ka_{23} \end{bmatrix}.
$$    
<br/>
$$\begin{bmatrix} 	ka_{11} & ka_{12} & ka_{13} \\
	ka_{21} & ka_{22} & ka_{23} \end{bmatrix}$$ adalah matriks berukuran $2 \times 3$ sehingga $cA$ juga berada di dalam $V$.   
<br/>
7. Apakah $k(A+B) = kA + kB$?    
Ya karena   
$$ \begin{align} k(A+B) &= k \left( \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\
	b_{21} & b_{22} & b_{23} \end{bmatrix} \right) \\
	                    &= k \left( \begin{bmatrix} 	a_{11} + b_{11} & a_{12} + b_{12} & a_{13} + b_{13} \\
	a_{21} + b_{21} & a_{22} + b_{22} & a_{23} + b_{23} \end{bmatrix} \right) \\
	                    &= \begin{bmatrix} 	k(a_{11} + b_{11}) & k(a_{12} + b_{12}) & k(a_{13} + b_{13}) \\
	k(a_{21} + b_{21}) & k(a_{22} + b_{22}) & k(a_{23} + b_{23}) \end{bmatrix} \\
	                    &= \begin{bmatrix} 	ka_{11} + kb_{11} & ka_{12} + kb_{12} & ka_{13} + kb_{13} \\
	ka_{21} + kb_{21} & ka_{22} + kb_{22} & ka_{23} + kb_{23} \end{bmatrix} \\
	                    &= \begin{bmatrix} 	ka_{11} & ka_{12} & ka_{13}  \\
	ka_{21} & ka_{22} & ka_{23}  \end{bmatrix} + \begin{bmatrix} 	kb_{11} & kb_{12} & kb_{13} \\
	kb_{21} & kb_{22} & kb_{23} \end{bmatrix} \\
	                    &= k \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23}  \end{bmatrix} + k \begin{bmatrix} 	b_{11} & b_{12} & b_{13}  \\
	b_{21} & b_{22} & b_{23}  \end{bmatrix} \\
	                    &= kA + kB.
\end{align}$$    
<br/>
8. Apakah $(k+l)A = kA + lA$?    
Ya karena    
$$ \begin{align} (k+l) A &= (k+l) \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} \\ 		
\end{bmatrix}  \\
                         &= \begin{bmatrix} (k+l) a_{11} & (k+l) a_{12} & (k+l) a_{13}  \\
	(k+l) a_{21} & (k+l) a_{22} & (k+l) a_{23} 	 \end{bmatrix} \\
	                     &= \begin{bmatrix} 	k a_{11} + l a_{11} & k a_{12} + l a_{12} & k a_{13} + l a_{13}  \\
	k a_{21} + l a_{21} & k a_{22} + l a_{22} & k a_{23} + l a_{23} 	\end{bmatrix} \\
	                     &= \begin{bmatrix} 	k a_{11} & k a_{12}  & k a_{13}   \\
	k a_{21} & k a_{22}  & k a_{23}  \end{bmatrix} + \begin{bmatrix} 	l a_{11} & l a_{12} & l a_{13}  \\
	l a_{21} & l a_{22} & l a_{23} \end{bmatrix} \\
	                     &= k \begin{bmatrix} 	a_{11} & a_{12}  & a_{13}   \\
	a_{21} & a_{22}  & a_{23} \end{bmatrix} + l \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} 	\end{bmatrix} \\
	                     &= kA + lA.
\end{align} $$    
<br/>
9. Apakah $k(lA) = (kl)A$?   
Ya karena   
$$ \begin{align} k(l A) &= k \left( l \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23}  \end{bmatrix} \right)  \\
	                   &= k \left( \begin{bmatrix} 	l a_{11} & l a_{12} & l a_{13}  \\
	l a_{21} & l a_{22} & l a_{23} \end{bmatrix} \right)  \\
	                   &= k \begin{bmatrix} 	l a_{11} & l a_{12} & l a_{13}  \\
	l a_{21} & l a_{22} & l a_{23} \end{bmatrix}  \\
	                   &= \begin{bmatrix} 	kl a_{11} & kl a_{12} & kl a_{13}  \\
	kl a_{21} & kl a_{22} & kl a_{23} \end{bmatrix} \\
	                   &= \begin{bmatrix} 	(kl)a_{11} & (kl)a_{12} & (kl)a_{13}  \\
	(kl)a_{21} & (kl)a_{22} & (kl)a_{23} \end{bmatrix} \\
	                   &= (kl) \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} \\
	                   &= (kl) A. 
\end{align} $$   
<br/>
10. Apakah $1(A) = A$?   
Ya karena    
$$ \begin{align} 1(A) &= 1 \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} \\
	                  &= \begin{bmatrix} 	1a_{11} & 1a_{12} & 1a_{13}  \\
	1a_{21} & 1a_{22} & 1a_{23} \end{bmatrix} \\
	                  &= \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} \end{bmatrix}  \\
	                  &= A.
	\end{align}
$$    
<br/>


Karena $V$ memenuhi 10 aksioma dari definisi suatu ruang vektor, $V$ atau himpunan dari semua matriks berukuran $2 \times 3$ beserta operasi _matrix addition_ dan _scalar multiplication_ merupakan sebuah **ruang vektor**.   $\square$


