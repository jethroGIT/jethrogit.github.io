---
layout: post
title: Hasil Kali Titik dan Sudut Antara 2 Vektor
category: Linear-Algebra
lang: ID
description: Hubungan Hasil Kali Titik dan Sudut
sticky: false
---

Artikel ini hendak memberikan penjelasan yang lebih detil mengenai hubungan antara **hasil kali titik** (_dot product_) dengan **sudut** antara 2 vektor. Buku [Larson](https://www.amazon.com/Elementary-Linear-Algebra-Ron-Larson/dp/1305658000/) (2016) pada halaman 235 kembali direkomendasikan menjadi referensi utama. 

Diketahui dua buah vektor $\mathbf{u} = (u_1, u_2)$ dan $\mathbf{v} = (v_1, v_2)$ dan sudut $\theta$ adalah sudut yang dibentuk oleh vektor $\mathbf{u}$ dan $\mathbf{v}$ seperti pada gambar berikut:

[![img1]({{ site.baseurl }}/assets/images/angle-between-two-vectors.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/angle-between-two-vectors.png)

Gambar di atas sepenuhnya merupakan hak cipta dari [Larson](https://www.amazon.com/Elementary-Linear-Algebra-Ron-Larson/dp/1305658000/) (2016). _For your information, buku [Larson](https://www.amazon.com/Elementary-Linear-Algebra-Ron-Larson/dp/1305658000/) (2016) is highly recommended_. 

Berdasarkan konsep yang bernama [Aturan Kosinus](https://www.khanacademy.org/math/geometry/hs-geo-trig/hs-geo-law-of-cosines/v/law-of-cosines-example) (_The Law of Cosines_), diperoleh

$$ \require{cancel} \begin{align} \lVert \mathbf{v} - \mathbf{u} \rVert^2 &= \lVert \mathbf{u} \rVert^2 + \lVert \mathbf{v} \rVert^2 - 2 \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos \theta \\
\Longleftrightarrow  (v_1 - u_1)^2 + (v_2 - u_2)^2 &= u_1^2 + u_2^2 + v_1^2 + v_2^2 - 2 \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos \theta \\
\Longleftrightarrow \cancel{v_1^2} - 2 v_1 u_1 + \cancel{u_1^2} + \cancel{v_2^2} - 2 v_2 u_2 + \cancel{u_2^2} &=  \cancel{u_1^2} + \cancel{u_2^2} + \cancel{v_1^2} + \cancel{v_2^2} - 2 \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos \theta \\
\Longleftrightarrow u_1 v_1 + u_2 v_2 &= \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos \theta \\
\Longleftrightarrow \cos \theta &= \frac{u_1 v_1 + u_2 v_2}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}. \tag{1}\label{eq:final-eq}
\end{align}
$$

Pembilang dari pecahan di ruas kanan dari Persamaan \eqref{eq:final-eq} merupakan **hasil kali titik** (_dot product_) dari $\mathbf{u}$ dan $\mathbf{v}$ sehingga Persamaan \eqref{eq:final-eq} dapat ditulis menjadi

$$ \begin{equation} \cos \theta = \frac{\mathbf{u} \centerdot \mathbf{v}}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}. 
\end{equation} \tag{2}\label{eq:dot-product}$$

Jadi dapat disimpulkan bahwa Persamaan \eqref{eq:dot-product} menjelaskan hubungan antara **hasil kali titik** (_dot product_) antara 2 vektor dan sudut yang dibentuk oleh keduanya.  
