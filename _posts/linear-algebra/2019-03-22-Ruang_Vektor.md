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
<br/>
Diketahui juga $A$, $B$, dan $C$ adalah matriks berukuran $2 \times 3$ dan $c$, $d$ adalah skalar dengan spesifikasi sebagai berikut:   
$$A = \begin{bmatrix}a_{11} & a_{12} & a_{13}\\a_{21} & a_{22} & a_{23}\end{bmatrix}$$, $$B = \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\ b_{21} & b_{22} & b_{23}\end{bmatrix}$$, dan $$C = \begin{bmatrix} 	c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22} & c_{23} \end{bmatrix}$$.    
<br/>
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
6. Apakah $cA$ juga ada di dalam $V$?    
Ya, karena
$$ cA = c \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23}
 \end{bmatrix} = \begin{bmatrix} 	ca_{11} & ca_{12} & ca_{13} \\
	ca_{21} & ca_{22} & ca_{23} \end{bmatrix}.
$$    
<br/>
$$\begin{bmatrix} 	ca_{11} & ca_{12} & ca_{13} \\
	ca_{21} & ca_{22} & ca_{23} \end{bmatrix}$$ adalah matriks berukuran $2 \times 3$ sehingga $cA$ juga berada di dalam $V$.   
<br/>
7. Apakah $c(A+B) = cA + cB$?    
Ya karena   
$$ \begin{align} c(A+B) &= c \left( \begin{bmatrix} 	a_{11} & a_{12} & a_{13} \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} + \begin{bmatrix} 	b_{11} & b_{12} & b_{13} \\
	b_{21} & b_{22} & b_{23} \end{bmatrix} \right) \\
	                    &= c \left( \begin{bmatrix} 	a_{11} + b_{11} & a_{12} + b_{12} & a_{13} + b_{13} \\
	a_{21} + b_{21} & a_{22} + b_{22} & a_{23} + b_{23} \end{bmatrix} \right) \\
	                    &= \begin{bmatrix} 	c(a_{11} + b_{11}) & c(a_{12} + b_{12}) & c(a_{13} + b_{13}) \\
	c(a_{21} + b_{21}) & c(a_{22} + b_{22}) & c(a_{23} + b_{23}) \end{bmatrix} \\
	                    &= \begin{bmatrix} 	ca_{11} + cb_{11} & ca_{12} + cb_{12} & ca_{13} + cb_{13} \\
	ca_{21} + cb_{21} & ca_{22} + cb_{22} & ca_{23} + cb_{23} \end{bmatrix} \\
	                    &= \begin{bmatrix} 	ca_{11} & ca_{12} & ca_{13}  \\
	ca_{21} & ca_{22} & ca_{23}  \end{bmatrix} + \begin{bmatrix} 	cb_{11} & cb_{12} & cb_{13} \\
	cb_{21} & cb_{22} & cb_{23} \end{bmatrix} \\
	                    &= c \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23}  \end{bmatrix} + c \begin{bmatrix} 	b_{11} & b_{12} & b_{13}  \\
	b_{21} & b_{22} & b_{23}  \end{bmatrix} \\
	                    &= cA + cB.
\end{align}$$    
<br/>
8. Apakah $(c+d)A = cA + dA$?    
Ya karena    
$$ \begin{align} (c+d) A &= (c+d) \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} \\ 		
\end{bmatrix}  \\
                         &= \begin{bmatrix} (c+d) a_{11} & (c+d) a_{12} & (c+d) a_{13}  \\
	(c+d) a_{21} & (c+d) a_{22} & (c+d) a_{23} 	 \end{bmatrix} \\
	                     &= \begin{bmatrix} 	c a_{11} +d a_{11} & c a_{12} + d a_{12} & c a_{13} +d a_{13}  \\
	c a_{21} +d a_{21} & c a_{22} + d a_{22} & c a_{23} +d a_{23} 	\end{bmatrix} \\
	                     &= \begin{bmatrix} 	c a_{11} & c a_{12}  & c a_{13}   \\
	c a_{21} & c a_{22}  & c a_{23}  \end{bmatrix} + \begin{bmatrix} 	d a_{11} & d a_{12} & d a_{13}  \\
	d a_{21} & d a_{22} & d a_{23} \end{bmatrix} \\
	                     &= c \begin{bmatrix} 	a_{11} & a_{12}  & a_{13}   \\
	a_{21} & a_{22}  & a_{23} \end{bmatrix} + d \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} 	\end{bmatrix} \\
	                     &= cA + dA.
\end{align} $$    
<br/>
9. Apakah $c(dA) = (cd)A$?   
Ya karena   
$$ \begin{align} c(dA) &= c \left( d \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23}  \end{bmatrix} \right)  \\
	                   &= c \left( \begin{bmatrix} 	da_{11} & da_{12} & da_{13}  \\
	da_{21} & da_{22} & da_{23} \end{bmatrix} \right)  \\
	                   &= c \begin{bmatrix} 	da_{11} & da_{12} & da_{13}  \\
	da_{21} & da_{22} & da_{23} \end{bmatrix}  \\
	                   &= \begin{bmatrix} 	cda_{11} & cda_{12} & cda_{13}  \\
	cda_{21} & cda_{22} & cda_{23} \end{bmatrix} \\
	                   &= \begin{bmatrix} 	(cd)a_{11} & (cd)a_{12} & (cd)a_{13}  \\
	(cd)a_{21} & (cd)a_{22} & (cd)a_{23} \end{bmatrix} \\
	                   &= (cd) \begin{bmatrix} 	a_{11} & a_{12} & a_{13}  \\
	a_{21} & a_{22} & a_{23} \end{bmatrix} \\
	                   &= (cd) A. 
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





