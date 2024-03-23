# markdown数学语法

## 1. 基本格式

### 1. 行内公式

以$开始，以$结尾。例如：<font color=red>`$a^b$`</font>

$$
a^b
$$

### 2. 块级公式-行间公式

以$$开头，$$结尾。l例如：\$$a^b+d+dddddd\$$
$$
a^b+d+dddddd
$$

### 3. 角标

上标：^ 表示后面的内容的右上角$a^b$
$$
a^b
$$
下标：_表示后面的内容的右下角$$a_b$$
$$
a_b
$$
常用公式总结：

| 数学公式                 | Markdown语法              |
| ------------------------ | ------------------------- |
| $a^b$                    | \$a^b$                    |
| $\sum_{n=1}^N{6y^n}$     | \$\sum_{n=1}^N{6y^n}$     |
| $\prod_{n=1}^N{6x^n}$    | \$\prod_{n=1}^N{6x^n}$    |
| $\int^6_0{f(x)}{\rm d}x$ | \$\int^6_0{f(x)}{\rm d}x$ |
| $\lim_{x\to+\infty}x$    | \$\lim_{x\to+\infty}x$    |

如果角标不明显，可以在大括号内叠加一个角标增强。

| —            | 正常上标 | 上标偏上缩小 | 上标偏小缩小 | 正常下标 | 下标偏上缩小 | 下标偏小缩小 |
| ------------ | -------- | ------------ | ------------ | -------- | ------------ | ------------ |
| 数学公式     | $y^N$    | $y^{^N}$     | $y^{_N}$     | $y_2$    | \$y_{^N}$    | \$y_{_N}$    |
| Markdown格式 | \$y^N$   | \$y^{^N}$    | \$y^{_N}$    | \$y_2$   | \\$y_{^N}$   | \$y_{\_N}$   |

### 4.整体内容

数据的运算的多项式写在{}中

\$\frac{e^x+1}{arctanx+lnf(x)}$
$$
\frac{e^x+1}{arctanx+lnf(x)}
$$

### 5.多行公式

格式如下：公式显示在中间

```markdown
$$
	\begin{split}
	x=&a-b-d \\
	y=&f-s-h \\
	\end{split}
$$
```

$$
	\begin{split}
	x=&a-b-d \\
	y=&f-s-h \\
	\end{split}
$$

> 解释：
>
> > 1. <font color=red>\\\\</font>：表示换行
> > 2. <font color=red>&</font>：表示上下哪个位置<font color=red>对齐</font>，需要在两行需要对齐的位置都加上这个符号。
> > 3. <font color=red>\\tag{1}</font>：表示对公式的<font color=red>手动编号</font>是1
> > 4. <font color=red>split</font>：是一个公式环境，用于一个公式拆分成多行的情形，类似的还有<font color=red>align</font>。
> > 5. <font color=red>\*</font>：表示不自动编号，不加星号会自动编号。

```markdown
$$
	\begin{align*}
    &x = a + b + c\\        
    &y = a + b     
    \end{align*}
$$
```


$$
\begin{align*}     
	&x = a + b + c\\    
	&y = a + b 
	\end{align*}
$$

### 6.分段函数

基本格式：

```markdown
$$
	y=\begin{cases}
    -x,\quad x\leq 0\\
    x, \quad x>0
  	\end{cases}
$$
```

$$
y=\begin{cases}
    -x,\quad x\leq 0\\
    x, \quad x>0
  \end{cases}
$$

### 7. 定界符

就是<font color=red>()、[]、{}</font>等，可以通过<font color=red>big、Big、bigg、Bingg</font>等调整大小，但是推荐<font color=red>$\left(内容\\right)$</font>调整大小。

```markdown
$$
\left(\frac{a+b}{b-a}\right)
$$
```

$$
\left(\frac{a+b}{b-a}\right)
$$

### 8.矩阵

```markdown
$$
\begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
\end{bmatrix}
$$
```

$$
\begin{bmatrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
\end{bmatrix}
$$

| 数学公式                             | Markdown语法                           | 描述   |
| ------------------------------------ | -------------------------------------- | ------ |
| $\begin{matrix} a\\b \end{matrix}$   | \$\begin{matrix} a\\\b \end{matrix}$   | 无括号 |
| $\begin{bmatrix} a\\b \end{bmatrix}$ | \$\begin{bmatrix} a\\\b \end{bmatrix}$ | 中括号 |
| $\begin{Bmatrix} a\\b \end{Bmatrix}$ | \$\begin{Bmatrix} a\\\b \end{Bmatrix}$ | 大括号 |
| $\begin{vmatrix} a\\b \end{vmatrix}$ | \$\begin{vmatrix} a\\\b \end{vmatrix}$ | 直线   |
| $\begin{Vmatrix} a\\b \end{Vmatrix}$ | \$\begin{Vmatrix} a\\\b \end{Vmatrix}$ | 平行线 |

### 9.空格

| 名称                  | 数学公式    | Markdown语法 |
| --------------------- | ----------- | ------------ |
| 两个空格的宽度        | $a\qquad b$ | \$a\qquad b$ |
| 一个空格的宽度        | $a\quad b$  | \$a\quad b$  |
| 1/3空格宽度           | $a\ b$      | \$a\ b$      |
| 2/7空格宽度           | $a\;b$      | \$a\;b$      |
| 1/6空格宽度           | $a\,b$      | \$a\,b$      |
| 紧贴，缩进1/6空格宽度 | $a\!b$      | \$a\\!b$     |

## 语法汇总

| 描述                    | 数学公式                           | Markdown格式                        |
| ----------------------- | ---------------------------------- | ----------------------------------- |
| 累加                    | $\sum_{n=1}^N {3x^n}$              | \$\sum_{n=1}^N {3x^n}$              |
| 累乘                    | $\prod_{n=1}^N{3x^n}$              | \$\prod_{n=1}^N{3x^n}$              |
| 开方                    | $\sqrt[5]{100}$                    | \$\sqrt[5]{100}$                    |
| 积分                    | $\int^5_1{f(x)}{\rm d}x$           | \$\int^5_1{f(x)}{\rm d}x$           |
| 二重积分                | $\iint^5_1{f(x)}{\rm d}x$          | \$\iint^5_1{f(x)}{\rm d}x$          |
| 无穷                    | \$\infty$                          | \$\infty$                           |
| 极限                    | $\lim_{n\to+\infty}n$              | \$\lim_{n\to+\infty}n$              |
| 加减                    | $\pm$                              | \$\pm$                              |
| 点乘                    | $\cdot$                            | \$\cdot$                            |
| 乘                      | $\times$                           | \$\times$                           |
| 除                      | $\div$                             | \$\div$                             |
| 右箭头                  | $\rightarrow$                      | \$\rightarrow$                      |
| 上箭头                  | $\uparrow$                         | \$\uparrow$                         |
| 左箭头                  | $\leftarrow$                       | \$\leftarrow$                       |
| 下箭头                  | $\downarrow$                       | \$\downarrow$                       |
| 用于带下标序列的省略号  | $\ddots$                           | \$\ddots$                           |
| 省略号                  | $\ddots$                           | \$\ddots$                           |
| 分数                    | $\frac{分子}{分母}$                | \$\frac{分子}{分母}$                |
| alpha                   | $\alpha$                           | \$\alpha$                           |
| beta                    | $\beta$                            | \$\beta$                            |
| gamma                   | $\gamma$                           | \$\gamma$                           |
| lambda                  | $\lambda$                          | \$\lambda$                          |
| theta                   | $\theta$                           | \$\theta$                           |
| pi                      | $\pi$                              | \$\pi$                              |
| Delta                   | $\Delta$                           | \$\Delta$                           |
| Sigma                   | $\Sigma$                           | \$\Sigma$                           |
| 可以通过`\rm`来取消斜体 | $f(x)$` `$\rm f(x)$` `${\rm f}(x)$ | \$f(x)$` `$\rm f(x)$` `${\rm f}(x)$ |

## 2. 分数

```markdown
$$
	\frac{x}{1+x^2} \\

	\frac{\frac{1}{2}+x}{y} \\
	\tfrac{a}{b}
    \frac{a}{b}
$$
```

$$
	\frac{x}{1+x^2}\\
	\frac{\frac{1}{2}+x}{y}\\
	\tfrac{a}{b}
    \frac{a}{b}
$$

## 3. 开根号

```markdown
$$
\sqrt{x} \\
\sqrt[3]{x}
$$
```

$$
\sqrt{x} \\
\sqrt[3]{x}
$$

## 4.组合数

```markdown
$$
\binom{n}{k}
\tbinom{n}{k}
$$
```

$$
\binom{n}{k}
\tbinom{n}{k}
$$

## 5.导数

```markdown
$$
a'
a''
a^{\prime}
$$
```

$$
a'
a''
a^{\prime}
$$

## 6.取模

```markdown
$$
x \pmod a
\\
2\mod{x}
$$
```

$$
x \pmod a
\\
2\mod{x}
$$

## 7.积分

```markdown
$$
	\int_{1}^{2}
	\intop_{2}^{1}
	\oint
	\smallint
	\\
	\iint
	\oiint
	\iiint
	\oiiint
$$
```

$$
\int_{1}^{2}
\intop_{2}^{1}
\oint
\smallint
\\
\iint
\oiint
\iiint
\oiiint
$$

## 8.微分

``` markdown
$$
	\nabla		\\
	\partial x	\\		
	\mathrm{d}x	\\
	\dot x		\\
	\ddot y     \\
	\Delta \\
$$
```

$$
\nabla	\\	
\partial x		\\	
\mathrm{d}x	\\
\dot x		\\
\ddot y     \\
\Delta \\
$$

## 9.累积/类乘/极限

```markdown
$$
\sum_{i=1}^{k}
\displaystyle\sum_{i=1}^n
\textstyle\sum_{i=1}^n
\\
\prod_{i=1}^{k}
\displaystyle\prod_{i=1}^n
\textstyle\prod_{i=1}^n
\\
\lim_{k \to \infty}
\lim\limits_{k \to \infty}
\lim\nolimits_{k \to \infty}]
$$
```

$$
\sum_{i=1}^{k}
\displaystyle\sum_{i=1}^n
\textstyle\sum_{i=1}^n
\\
\prod_{i=1}^{k}
\displaystyle\prod_{i=1}^n
\textstyle\prod_{i=1}^n
\\
\lim_{k \to \infty}
\lim\limits_{k \to \infty}
\lim\nolimits_{k \to \infty}]
$$

# 修饰符号

## 1.简单的帽子

```mariadb
$$
\hat{\theta}
\widehat{AB}
\\
\bar{y}
\overline{AB}
\\
\tilde{a}
\widetilde{ac}
\\
\bar{a}
\acute{a}
\check{a}
\grave{a}
\\
\dot{a}
\ddot{a}
$$
```

$$
\hat{\theta}
\widehat{AB}
\\
\bar{y}
\overline{AB}
\\
\tilde{a}
\widetilde{ac}
\\
\bar{a}
\acute{a}
\check{a}
\grave{a}
\\
\dot{a}
\ddot{a}
$$

## 2.帽子和袜子

```markdown
$$
\overleftarrow{AB}
\overrightarrow{AB}
\overleftrightarrow{AB}
\\
\underleftarrow{AB}
\underrightarrow{AB}
\underleftrightarrow{AB}
\\
\overbrace{AB}
\underbrace{AB}
\\
\overline{AB}
\underline{AB}
$$
```

$$
\overleftarrow{AB}
\overrightarrow{AB}
\overleftrightarrow{AB}
\\
\underleftarrow{AB}
\underrightarrow{AB}
\underleftrightarrow{AB}
\\
\overbrace{AB}
\underbrace{AB}
\\
\overline{AB}
\underline{AB}
$$

## 3.盒子和帽子

```markdown
$$
\overbrace{a+b+c}^{\text{note}}
\\
\underbrace{a+b+c}_{\text{note}}
\\
\boxed{\pi=3.14}
$$
```

$$
\overbrace{a+b+c}^{\text{note}}
\\
\underbrace{a+b+c}_{\text{note}}
\\
\boxed{\pi=3.14}
$$

## 4.各种括号

```markdown
$$
(
\big(
\Big(
\bigg(
\Bigg(
$$
```

$$
(
\big(
\Big(
\bigg(
\Bigg(
$$

```markdown
$$
[]
<>
|-2|
\{\}
$$
```

$$
[]
<>
|-2|
\{\}
$$

```markdown
$$
\lgroup x \rgroup
\lVert a \rVert
\lceil 2.6 \rceil
\lfloor 1.2 \rfloor
$$
```

$$
\lgroup x \rgroup
\lVert a \rVert
\lceil 2.6 \rceil
\lfloor 1.2 \rfloor
$$

```markdown
$$
\ulcorner
\urcorner
\llcorner
\lrcorner
$$
```

$$
\ulcorner
\urcorner
\llcorner
\lrcorner
$$

## 5.各种箭头

```markdown
$$
\gets
\leftarrow
\to
\rightarrow
\leftrightarrow
\\
\uparrow
\downarrow
\updownarrow
$$
```

$$
\gets
\leftarrow
\to
\rightarrow
\leftrightarrow
\\
\uparrow
\downarrow
\updownarrow
$$

```markdown
$$
\Leftarrow
\Rightarrow
\Leftrightarrow
\iff
\\
\Uparrow
\Downarrow
\Updownarrow
$$
```

$$
\Leftarrow
\Rightarrow
\Leftrightarrow
\iff
\\
\Uparrow
\Downarrow
\Updownarrow
$$

```markdown
$$
\nearrow
\searrow
\swarrow
\nwarrow
$$
```

$$
\nearrow
\searrow
\swarrow
\nwarrow
$$

```markdown
$$
\longleftarrow
\longrightarrow
\longleftrightarrow
\Longleftarrow
\Longrightarrow
\Longleftrightarrow
\longmapsto
$$
```

$$
\longleftarrow
\longrightarrow
\longleftrightarrow
\Longleftarrow
\Longrightarrow
\Longleftrightarrow
\longmapsto
$$

```markdown
$$
\xrightarrow{over}
\xrightarrow[over]{}
\xrightarrow[under]{over}
\xleftarrow[]{over}
\xleftarrow[under]{}
\xleftarrow[under]{over}
$$
```

$$
\xrightarrow{over}
\xrightarrow[over]{}
\xrightarrow[under]{over}
\xleftarrow[]{over}
\xleftarrow[under]{}
\xleftarrow[under]{over}
$$

## 6.空间间距

```markdown
$$
A\!B
\\
AB
\\
A\thinspace B
\\
A\:B
\\
A\ B
\\
A \enspace B
\\
A\quad B
\\
A\qquad B
$$
```

$$
A\!B
\\
AB
\\
A\thinspace B
\\
A\:B
\\
A\ B
\\
A \enspace B
\\
A\quad B
\\
A\qquad B
$$

## 7.矩阵

```markdown
$$
A = \begin{matrix}
a & b\\
c & d
\end{matrix}
$$
```

$$
A = \begin{matrix}
a & b\\
c & d
\end{matrix}
$$

```markdown
$$
B = \begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
$$
```

$$
B = \begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
$$

```markdown
$$
C = \begin{vmatrix}
a & b\\
c & d
\end{vmatrix}
$$
```

$$
C = \begin{vmatrix}
a & b\\
c & d
\end{vmatrix}
$$

```mark
$$
	D = \begin{bmatrix}
	a & b\\
	c & d
	\end{bmatrix}
$$
```

$$
D = \begin{bmatrix}
a & b\\
c & d
\end{bmatrix}
$$

```markdown
$$
E = \begin{Vmatrix}
a & b\\
c & d
\end{Vmatrix}
$$
```

$$
E = \begin{Vmatrix}
a & b\\
c & d
\end{Vmatrix}
$$

```markdown
$$
F = \begin{Bmatrix}
a & b\\
c & d
\end{Bmatrix}
$$
```

$$
F = \begin{Bmatrix}
a & b\\
c & d
\end{Bmatrix}
$$

```markdown
$$
[A\ b] = 
\begin{bmatrix}
\begin{array}{c c c|c}
a_{11} & a_{12} & a_{13} & b_1\\
a_{21} & a_{22} & a_{23} & b_2\\
a_{31} & a_{32} & a_{33} & b_3\\
\end{array}
\end{bmatrix}
$$
```

$$
[A\ b] = 
\begin{bmatrix}
\begin{array}{c c c|c}
a_{11} & a_{12} & a_{13} & b_1\\
a_{21} & a_{22} & a_{23} & b_2\\
a_{31} & a_{32} & a_{33} & b_3\\
\end{array}
\end{bmatrix}
$$

```markdown
$$
\begin{array}{c:c:c}
a & b & c \\ 
\hline
d & e & f \\
\hdashline
 g & h & i
\end{array}
$$
```

$$
\begin{array}{c:c:c}
a & b & c \\ 
\hline
d & e & f \\
\hdashline
 g & h & i
\end{array}
$$

```markdown
$$
L_{n\times n} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots &\ddots & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn} \\ 
\end{bmatrix}
$$
```

$$
L_{n\times n} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\ 
a_{21} & a_{22} & \cdots & a_{2n} \\ 
\vdots & \vdots &\ddots & \vdots\\
a_{n1} & a_{n2} & \cdots & a_{nn} \\ 
\end{bmatrix}
$$

## 7.列式/方程组

```markdown
$$
\begin{aligned}
f(x) &= (x+1)^2\\
&= x^2 + 2x + 1
\end{aligned}
$$
```

$$
\begin{aligned}
f(x) &= (x+1)^2\\
&= x^2 + 2x + 1
\end{aligned}
$$

```markdown
$$
f(x) = \begin{cases}
a &\text{if b}\\
b &\text{if a}\\
\end{cases}
$$
```

$$
f(x) = \begin{cases}
a &\text{if b}\\
b &\text{if a}\\
\end{cases}
$$

```markdown
$$
\begin{cases}
\begin{aligned}
x + 2y &= 1\\
3x - y &= 5
\end{aligned}
\end{cases}
$$
```

$$
\begin{cases}
\begin{aligned}
x + 2y &= 1\\
3x - y &= 5
\end{aligned}
\end{cases}
$$

```markdown
$$
g(x,y)=\left\{
\begin{array}{rcl}
\frac{M_g - d}{M_f-b}[f(x,y)-b]+d       &      & {b      \leq  f(x,y)  \leq M_f}\\
F^*_L     &      & {S_L \leq 0 < S_M}\\
F^*_R     &      & {S_M \leq 0 < S_R}\\
F_R       &      & {S_R \leq 0}
\end{array} \right.
$$
```

$$
g(x,y)=\left\{
\begin{array}{rcl}
d       &      & {b      \leq  f(x,y)  \leq M_f}\\
F^*_L     &      & {S_L \leq 0 < S_M}\\
F^*_R     &      & {S_M \leq 0 < S_R}\\
F_R       &      & {S_R \leq 0}
\end{array} \right.
$$

## 8.修改颜色和字体大小

```markdown
$$
\textcolor{blue}{F=ma}
\\
\textcolor{#00ff00}{F=ma}
\\
\textcolor{#ff0000}{F=ma}
\\
\color{blue} one\ line
\\
nothing
$$
```

$$
\textcolor{blue}{F=ma}
\\
\textcolor{#00ff00}{F=ma}
\\
\textcolor{#ff0000}{F=ma}
\\
\color{blue} one\ line
\\
nothing
$$

```markdown
$$
\colorbox{#00ff00}{F=ma}
\\
\colorbox{aqua}{A}
\\
\fcolorbox{red}{aqua}{A}
$$
```

$$
\colorbox{#00ff00}{F=ma}
\\
\colorbox{aqua}{A}
\\
\fcolorbox{red}{aqua}{A}
$$

```markdown
$$
AB
\Huge AB
\huge AB
\\
AB
\LARGE AB
\Large AB
\large AB
\\
AB
\small AB
\tiny AB
$$
```

$$
\Huge AB
\huge AB
\\
AB
\LARGE AB
\Large AB
\large AB
\\
AB
\small AB
\tiny AB
$$

## 9.划掉

```markdown
$$
\cancel{5}
\bcancel{5}
\xcancel{ABC}
\not =
$$
```

$$
\cancel{5}
\bcancel{5}
\xcancel{ABC}
\not =
$$

## 10.常见图形

```markdown
$$
\Box
\square
\blacksquare
\triangle
\triangledown
\blacktriangle
\diamond
\Diamond
\star
\bigstar
\circ
\bullet
\bigcirc
\bigodot
$$
```

$$
\Box
\square
\blacksquare
\triangle
\triangledown
\blacktriangle
\diamond
\Diamond
\star
\bigstar
\circ
\bullet
\bigcirc
\bigodot
$$

```markdown
$$
\diamondsuit
\clubsuit
\heartsuit
\spadesuit
$$
```

$$
\diamondsuit
\clubsuit
\heartsuit
\spadesuit
$$

```markdown
$$
\angle
\measuredangle
\top
\bot
\infty
$$
```

$$
\angle
\measuredangle
\top
\bot
\infty
$$

```mark
$$
	\checkmark
	\dagger
	\ddagger
	\yen
	\$
$$
```

$$
	\checkmark
	\dagger
	\ddagger
	\yen
	\$
$$

## 11.声明宏

对于一些复杂但是只有少许不同的表达式，可以声明一个函数来调用，提高源码的可读性，减少出错

```markdown
\def\macroname#1#2{
your command
}
```

宏允许带任意数量的参数（也可以不带参），必须是`#1,#2,……`这样的命名格式，同时注意再定义宏的时候注意让`#1`与`\`中间隔一个空格，否则会解析成#。再调用的时候格式为`\macroname{x}{y}{z}`，可以参考一下的例子

```markdown
$$
\def\Normal#1#2#3{
\frac{1}{\sqrt{2\pi}\ #3}\exp{[-\frac{(#1 - #2)^2}{2\ #3^2}]}
}
f(x)=\Normal{x}{u_1}{\sigma_1}\\
f(y)=\Normal{y}{u_2}{\sigma_2}\\
$$
```

$$
\def\Normal#1#2#3{
\frac{1}{\sqrt{2\pi}\ #3}\exp{[-\frac{(#1 - #2)^2}{2\ #3^2}]}
}
f(x)=\Normal{x}{u_1}{\sigma_1}\\
f(y)=\Normal{y}{u_2}{\sigma_2}\\
$$

```markdown
$$
\def\EXP{
e^x = 1 + x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3  + \cdots
}
\EXP
$$
```

$$
\def\EXP{
e^x = 1 + x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3  + \cdots
}
\EXP
$$

