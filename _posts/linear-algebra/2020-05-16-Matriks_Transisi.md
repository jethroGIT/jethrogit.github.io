---
layout: post
title: Matriks Transisi Antara 2 Basis di Suatu Ruang Vektor 
category: Linear-Algebra
lang: ID
description: Matriks transisi antara 2 basis
---

Artikel ini hendak memberikan penjelasan yang lebih detil tentang **Teorema 4.21** yang berjudul _Transition Matrix from_ $B$ _to_ $B^{\prime}$ dari buku [Larson](https://www.amazon.com/Elementary-Linear-Algebra-Ron-Larson/dp/1305658000/) (2016) di halaman 212. 

Diketahui 2 basis bagi $R^n$, yaitu 
$$ 
B = \{ \pmb{v}_1, \pmb{v}_2, \ldots, \pmb{v}_n \}  $$ dan 
$$ B^{\prime} = \{ \pmb{u}_1, \pmb{u}_2, \ldots, \pmb{u}_n \} $$ dengan

$$\pmb{v}_1 = \begin{bmatrix} v_{11} \\ 
v_{21} \\ 
\vdots \\
v_{n1} \end{bmatrix}, \; \pmb{v}_2 = \begin{bmatrix} v_{12} \\ 
v_{22} \\ 
\vdots \\
v_{n2} \end{bmatrix}, \; \ldots,  \text{ dan } \pmb{v}_n = \begin{bmatrix} v_{1n} \\ 
v_{2n} \\ 
\vdots \\
v_{nn} \end{bmatrix} $$ 

dan

$$\pmb{u}_1 = \begin{bmatrix} u_{11} \\ 
u_{21} \\ 
\vdots \\
u_{n1} \end{bmatrix}, \; \pmb{u}_2 = \begin{bmatrix} u_{12} \\ 
u_{22} \\ 
\vdots \\
u_{n2} \end{bmatrix}, \; \ldots,  \text{ dan } \pmb{u}_n = \begin{bmatrix} u_{1n} \\ 
u_{2n} \\ 
\vdots \\
u_{nn} \end{bmatrix}. $$

Langkah pertama adalah menulis setiap vektor di $B$ sebagai kombinasi linier dari setiap vektor di $B^{\prime}$ sebagai berikut:

$$
\begin{align}
	\pmb{v}_1 &= d_{11} \pmb{u}_1 + d_{21} \pmb{u}_2 + \cdots + d_{n1} \pmb{u}_n \tag{1}\label{eq:definisi-v}  \\
	\pmb{v}_2 &= d_{12} \pmb{u}_1 + d_{22} \pmb{u}_2 + \cdots + d_{n2} \pmb{u}_n \\
	   \vdots &=  \vdots \\
	\pmb{v}_n &= d_{1n} \pmb{u}_1 + d_{2n} \pmb{u}_2 + \cdots + d_{nn} \pmb{u}_n 
\end{align}
$$

Selanjutnya, matriks transisi dari basis $B$ ke basis $B^{\prime} $adalah $Q$ sedemikian sehingga

$$
	\begin{bmatrix}
		d_{11} \\
		d_{21} \\
		\vdots \\
		d_{n1} 
	\end{bmatrix} = Q \pmb{v}_1, \; 	\begin{bmatrix}
		d_{12} \\
		d_{22} \\
		\vdots \\
		d_{n2} 
	\end{bmatrix} = Q \pmb{v}_2, \ldots, \begin{bmatrix}
		d_{1n} \\
		d_{2n} \\
		\vdots \\
		d_{nn} 
	\end{bmatrix} = Q \pmb{v}_n \tag{2}\label{eq:q-awal}
$$

Dengan menggunakan notasi [Larson](https://www.amazon.com/Elementary-Linear-Algebra-Ron-Larson/dp/1305658000/) (2016) di **Subbab 4.7** _Coordinate Representation Relative to a Basis_ pada halaman 208, Persamaan \eqref{eq:q-awal} dapat ditulis menjadi

$$
	[\pmb{v}_1]_{B^{\prime}} = Q \pmb{v}_1, \; 
	[\pmb{v}_2]_{B^{\prime}} = Q \pmb{v}_2, \ldots, [\pmb{v}_n]_{B^{\prime}} = Q \pmb{v}_n \tag{3}\label{eq:q-akhir}
$$

Persamaan \eqref{eq:q-akhir} memperlihatkan bahwa perubahan $$\pmb{v}_1$$ yang merupakan vektor di basis $$B$$ menjadi $$[\pmb{v}_1]_{B^{\prime}}$$ dilakukan dengan cara mengalikan $$\pmb{v}_1$$ dengan $$Q$$. Dengan kata lain, perubahan dari basis $$B$$ menjadi basis $B^{\prime}$ dilakukan dengan mengalikan vektor di basis $$B$$ dengan matriks transisi $$Q$$.

> Selanjutnya, kita akan mencari matriks transisi $$Q$$ tersebut.    

Kita mulai dengan Persamaan \eqref{eq:definisi-v}, yaitu

$$
\begin{align}
	\pmb{v}_1 &= d_{11} \pmb{u}_1 + d_{21} \pmb{u}_2 + \cdots + d_{n1} \pmb{u}_n \\
	\Leftrightarrow  \begin{bmatrix} v_{11} \\
		v_{21}  \\
		\vdots \\
		v_{n1}  
	 \end{bmatrix} &= d_{11}  \begin{bmatrix} u_{11} \\
	 	u_{21} \\
	 	\vdots \\
	 	u_{n1}	\end{bmatrix} + d_{21}  \begin{bmatrix} u_{12} \\
	 	u_{22} \\
	 	\vdots \\
	 	u_{n2}	\end{bmatrix} + \cdots + d_{n1}  \begin{bmatrix} u_{1n} \\
	 	u_{2n} \\
	 	\vdots \\
	 	u_{nn}	\end{bmatrix} \\
	\Leftrightarrow  \begin{bmatrix} v_{11} \\
		v_{21}  \\
		\vdots \\
		v_{n1}  
	 \end{bmatrix} &= \begin{bmatrix} u_{11} & u_{12} & \cdots & u_{1n} \\
	 	u_{21} & u_{22}   & \cdots & u_{2n} \\
	 	\vdots &   \vdots & \cdots & \vdots \\
	 	u_{n1} & u_{n2}   & \cdots & u_{nn}	 	 
	 \end{bmatrix} \begin{bmatrix} 
	 	d_{11} \\
	 	d_{21} \\
	 	\vdots \\
	 	d_{n1}
	 \end{bmatrix}	& \text{Menggunakan bentuk matriks} \\
\Leftrightarrow  \begin{bmatrix} d_{11} \\
		d_{21}  \\
		\vdots \\
		d_{n1}  
	 \end{bmatrix} &= \underbrace{\begin{bmatrix} u_{11} & u_{12} & \cdots & u_{1n} \\
	 	u_{21} & u_{22}   & \cdots & u_{2n} \\
	 	\vdots &   \vdots & \cdots & \vdots \\
	 	u_{n1} & u_{n2}   & \cdots & u_{nn}	 	 
	 \end{bmatrix}^{-1}}_{Q}  \underbrace{\begin{bmatrix} 
	 	v_{11} \\
	 	v_{21} \\
	 	\vdots \\
	 	v_{n1}
	 \end{bmatrix}}_{\pmb{v}_1} & \text{Cari solusi SPL dengan teknik invers} \\
\Leftrightarrow  [\pmb{v}_1]_{B^{\prime}} &= Q \pmb{v}_1
\end{align}
$$

Untuk $$\pmb{v}_2$$, $$\pmb{v}_3$$ $$\ldots$$, $$\pmb{v}_n$$, dengan cara yang sama juga akan diperoleh bahwa

$$
	Q = \begin{bmatrix} u_{11} & u_{12} & \cdots & u_{1n} \\
	 	u_{21} & u_{22}   & \cdots & u_{2n} \\
	 	\vdots &   \vdots & \cdots & \vdots \\
	 	u_{n1} & u_{n2}   & \cdots & u_{nn}	 	 
	 \end{bmatrix}^{-1}
$$ 

Jadi kesimpulannya adalah
> _Matriks transisi dari_ $$B$$ _ke_ $$B^{\prime}$$, yaitu $$Q$$ _adalah invers dari matriks yang setiap kolom-kolomnya merupakan vektor-vektor dari basis_ $$B^{\prime}$$ atau
$$Q = \begin{bmatrix} \pmb{u}_1 & \pmb{u}_2 & \pmb{u}_3 & \cdots & \pmb{u}_n \end{bmatrix}^{-1}$$.

