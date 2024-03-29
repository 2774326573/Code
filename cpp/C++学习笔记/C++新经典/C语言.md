# C语言

## 1. 数据类型、运算符与表达式

   要学造句先学词汇，要学词汇先学文学，同理，要写C语言代码，首选要了解C语言代码的组成部分，在这些组成部分中，总少不了最基本的概念和元素，所以，常量、变量、类型、运算符、表达式等，这些最基本的编程元素，要最优先掌握。

###  1.1 常量、变量、整型、实型和字符型

#### 1.1.1 C语言的数据类型

   下图是C语言数据类型图，也许不太全面，但作为参考借鉴已经足够，其中所示的数据类型后续都会慢慢讲到。这些数据类型不必死记硬背，随着使用次数增多，慢慢就会熟悉。
   ```mermaid
    graph LR
    A(C语言数据类型)-->B1(基本类型)
    A-->B2(构造类型)
    A-->B3(指针类型)
    A-->B4(void空类型)

    B1-->C1(数值类型)
    B1-->C2(字符类型/char)

    B2-->D1(数组)
    B2-->D2(结构体/struct)
    B2-->D3(共用题/union)
    B2-->D4(枚举类型/enum)

    C1-->C11(整型)
    C1-->C12(浮点型)
    
    C11-->C111(短整型/short)
    C11-->C112(短整型/int)
    C11-->C113(短整型/long)
    
    C12-->C121(单精度型/float)
    C12-->C122(双精度型/double)
   ```
<center>数据类型图</center>

##### 1.每种数据类型所占内存大小

   既然在C语言中有多种数据类型，计算机在保存不同类型数据时所占用的内存大小是不同的，如表所示。从中可以了解常用数据类型所占用的内存大小(单位：字节)。

   <center>1.1表 常用类型所占用的内存大小(单位：字节)</center>

   |  数据类型               |  32位系统  |  64位系统 |
   |  --                     |  :--:      |  :--: |
   |  char                   |  1         |  1 |
   |  short(unsigned short)  |  2         |  2 |
   |  int(unsigned int)      |  4         |  4 |
   |  float                  |  4         |  4 |
   |  double                 |  8         |  8 |
   |  long                   |  4         |  8 |
   |  long long              |  4         |  8 |

##### 2.每种数据类型的取值范围

   可以这样认为，占用内存越多的数据类型，所保存数据的取值范围就越大。如下表所示为每种数据类型能够取值的范围。

   <center>2.2表 每种数据类型能够取值的范围(可能不全)</center>

   |  数据类型             |  最小值                |  最大值                |  所占字节 |
   |  --                   |  :--:                  |  :--:                  |  -- |
   |  char                 |  -128                  |  127                   |  1 |
   |  short                |  -32767                |  32768                 |  2 |
   |  unsigned short       |  0                     |  65536                 |  2 |
   |  int                  |  -2147483648           |  2147483647            |  4 |
   |  unsigned int         |  0                     |  4294967295            |  4 |
   |  long                 |  -2147483648           |  2147483647            |  4 |
   |  long  long           |  -9223372036854775807  |  9223372036854775808   |  8 |
   |  unsigned long  long  |  0                     |  18446744073709551615  |  8 |

#### 1.1.2 常量和变量
  常量：在程序运行过程中，其值不能改变的量。常量也分为不同类型：
  (1) 整型常量，如150。
  (2) 浮点型常量，如12.3(也称为实型常量)。
  (3) 字符常量：用一对单引号包含起来的一个字符，如'a'。
  这里用printf语句输出一个结果信息作为演示，是C语言中用于输出结果信息的语句，能将双引号中的内容进行输出，但当在双引号所含的内容中遇到%d时，会用后面的和值进行替换(%d是一个格式符，专门用来显示一个十进制整数)，因此，如下语句：`printf("35+48的值是%d\n",35+48);`输出的结果信息是：`35+48的值是83`

   下面将逐步引入变量的概念，在此之前，首先引入标识符、保留字这两个概念。

   (1) **<font color=red>标识符：</font>**好像人的名字(如张三、李四)，由字母、数字、下画线三种字符组成，并且第一个字符为字母或者下画线。例如，test 、icount、_myclass都是合法的标识符。

   (2) **<font color=red>保留字：</font>**系统保留起来，有特殊的用途，所以不能将保留字作为标识符来使用，否则会出现语法错误。保留字如图所示，这些保留字不必死记硬背，随着使用次数增多，慢慢就会熟悉。

   <center>C/C++中的保留字</center>

   | and               | asm           | auto         | bool    | break     |
   | --                | --            | --           | --      | --        |
   | case              | catch         | char         | class   | const     |
   | const_cast        | continue      | default      | delete  | do        |
   | double            | dynamic_cast  | else         | enum    | explicit  |
   | extern            | flase         | float        | for     | friend    |
   | goto              | if            | inline       | int     | long      |
   | mutable           | namespace     | new          | not     | operator  |
   | or                | private       | protected    | pulic   | register  |
   | reinterpret_cast  | return        | short        | signed  | struct    |
   | sizeof            | static        | static_cast  | throw   | switch    |
   | template          | this          | typeid       | true    | try       |
   | typedef           | using         | typename     | union   | unsigned  |
   | virtual           | void          | volatile     | while   | xor       |

<center>C/C++中的保留字</center>

   变量遵循先定义后使用的原则，定义变量时遵循如下格式：`类型名 变量名[=变量初值];`
其中，[]中的内容可以省，在格式表达中，凡被[]括起来的内容都表示可以省略。如下范例定义了两个不同的变量，因为这两个变量最后一个字符大小写不同：

  `int _myclass;`
  `int _myclasS;`

  变量名的长度没有具体标准，即便是几十上百个字符也可以，但一般10～20个字符长度就足够了。变量如何起名字呢？参考如下变量的命名方法：

  `iMemberCount;`

  在这个变量名，第一个字符表示类型，这里i表示int类型，然后用几个单词的组合，每个单词首字母大写，这样以后见到变量名就知道该变量表达的含义。

#### 1.1.3 整型数据

​	整型数据如下：

​	(1) 十进制数：如123、-456、0。

​	(2) 八进制数：以0开头的数字是八进制数，八进制数并不常用，对其粗略掌握即可。

```c
int abc;
abc = 012;	//八进制的12
printf("012的十进制数是：%d\n",abc);
```

​	输出的结果信息是：`012的十进制数是：10`

​	(3) 十六进制数：以0x开头的数是十六进制数，如0x123。十六进制数比较常用，需要对其进行一定的掌握，下面的范例演示0x12的十进制数。

```c
int abc;
abc = 0x12;
printf("0x12的十进制数是：%d\n",abc);
```

​	输出的结果信息为：`0x12的十进制数是：18`

​	那么，八进制、十六进制数如何转换为十进制数：只需要乘以2，再相加、取整就是对应的十进制数。简单看一下范例：

* 八进制数 012 = (2X$8^0$) + (1X$8^1$) = 2+8 = 十进制数10
* 十六进制数 0x12 = (2X$16^0$) + (1X$16^1$) = 2+16 =十进制数18

##### 1. 整型变量的分类

<font color=blue>**基本型：**</font>int

<font color=blue>**短整型：**</font>short int(简写为short)

<font color=blue>**长整型：**</font>long int(简写为long)

<font color=blue>**无符号型：**</font>unsigned int、unsigned short、unsigned long，<font color=red>**只能存放不带符号的数字(正数和零)，不能存放负数，所以，一个无符号整型变量存放的数字范围比带符号整型变量存放的数字范围大一倍，**</font>这一点从表1.2中可以看到。

​	如果无法确定某个变量或者某种数据类型所占用的内存大小(单位：字节)，可以使用sizeof运算符获得。但需要特别注意的是，用sizeof运算符获得某个变量所占用的内存大小时，和该变量中保存的数值内容没有任何关系。

​	演示范例如下：

```c
int abc;
printf("abc变量占用的内存字节数是：%d字节\n",sizeof(abc));
```

​	输出结果：`abc变量占用的内存字节数是：4字节`

​	该结果和表1.2所示的int型变量所占用的内存字节数一致。

##### 2. 整型变量的定义

````c
int a,b,c;
unsigned short d,e,f;
````

##### 3. 常量的类型

前面提到过，常量是分类型的，不过换个角度来看，常量也可以认为不分类型，如189是什么类型的常量呢？取决于该值附给什么类型的变量。演示范例如下：

```c
int abc = 189;	//这不是赋值语句，这是定义abc变量时顺带初始化，值为189
short def = 189;	//这依旧不是赋值语句，也是定义def变量时顺带初始化，值为189
def = 190;	//这才是赋值语句，这行带 = 的语句开头没有类型名,因此是赋值语句。
```

​	有一些特殊写法需要额外介绍：

​	(1) 在一个常数后面加一个字母U或u，表示该常数用无符号整型方式存储，相当于unsigned int。

​	(2) 在一个常数后面加一个字符L或l，表示该常数用长整型方式存储，相当于long。

​	(3) 在一个常数后面加一个字母F或f，表示该常数用浮点方式存储，相当于float。

​	整体感觉，这种写法的意义不大，因为这些常量一般都会赋值给一些变量，实际的类型取决于这些变量的类型。之所以介绍这种写法，是因为在阅读他人代码时，可能会遇到。演示范例如下：

```c
long int test3 = 189L;
int a= 23.12F;	//变量a依旧是int型
unsigned abc = 23U;
```

#### 1.1.4 实型数据

​	实型数据据简称实数，在C语言中称为浮点数(带小数部分的数)

##### 1.实型常量的两种表示形式

​	(1) 十进制数表示形式：0.12、3.14159。

​	(2) 指数表示形式：168E2，等价于168x$10^2$=16800.00，这种表示形式不太常用，但要有所了解，其中字母E可以大写也可以小写，再如如下表示形式：168E+2等价于168x$10^2$；168E-8等价于168x$10^{-8}$。

##### 2. 实型变量的分类

​	C语言中，实型变量分为单精度和双精度两种类型。

​	(1) float：单精度变量。

​	(2) double：双精度变量。

##### 3. 实型变量的定义

​	下面两行代码都是定义实型变量：

```c
float d,e,f;
double i,k;
```

​	上面两行代码有什么区别？float型变量一般在内存中占4字节，double型变量一般在内存中占8字节，这意味着double型变量所能保存的数据范围比float型变量所能保存的数据范围大得多，并且精度高得多(精度后面会详细解释)。

​	浮点数在内存中都是以指数形式存储的，所以能够存储的数据范围大到超乎想象：

​	(1) 单精度float：取值范围为(1.17549e-038)~(3.40282e+038)。

​	(2) 双精度double：取值范围为(2.22507e-308)~(1.79769e+308)。

​	如何区分float和double这两种浮点类型实数呢？

​	<font color=blue>它们的精度不同，float类型实数提供7位有效数字(考虑到四舍五入问题，保守算6位)，double类型实数提供15~16位有效数字(考虑到四舍五入问题，保守算15位)，到底多少位有效数字，随机器系统而异。</font>

​	有效数字又是什么意思呢？

​	<font color=blue>如数字12345.678，如果精度是1位有效数字，则实际只能存储为10000.0，也就是说，只能把最高位这个值存下，其余位全部都是0。<br/>	如果精度是2位有效数字，则存储为12000.0，也就是能存下最高的两位数值。<br/>	如果精度是3位有效数字，则存储为12300.0，也就是能存下最高的三位数值。</font>

<center>..........</center>

​	<font color=blue>如果精度是7位有效数字，则存储为12345.67X，X表示该位置的数字值并不确定。再看看数字0.1234，如果精度是1位有效数字，则存储的可能为0.1XXXXX，如果精度是2位有效数字，则存储的可能是0.12XXXX，以此类推。</font>

##### 4. 调试

​	调试对于日后顺利进行程序开发起到极其重要的作用，所以必须掌握好调试的方法。

​	(1) 快捷键F9(对应<kbd>调试</kbd>$\rightarrow$<kbd>切换断点</kbd>命令)，用于给光标所在的行增加断点或取消该行断点(俗称设置断点)，断点行最前面如果有一个红色小圆球表示该行有一个断点，可以通过将光标定位到多个行并每次都按F9键为多个行增加断点。

​	(2) 快捷键F5(对应<kbd>调试</kbd>$\rightarrow$<kbd>开始调试</kbd>命令)，用于开始执行程序，并且遇到第一个断点行就会停下，程序执行流程停到了第8行代码，红色小圆球中间多了一个向右指向的黄色小箭头，表示程序执行流程停止到了这一行(但此刻这行还没执行)。

​	(3) 此时，因为程序执行流程已经停了下来，可以人工介入来控制程序的执行，所以，此刻可以多次使用快捷键F10(对应<kbd>调试</kbd>$\rightarrow$<kbd>逐过程</kbd>命令)，从当前停止的代码行开始，一行一行继续让代码执行下去，边逐行执行，边观察程序的执行走向及各种变量的当前值，从而达到调试的目的。

示例：

```c
float af;
double bf;
af = 1111111.111;	//赋值给af变量
bf = 1111111.111;	//赋值给bf变量
printf("断点停留到这里!");
```
    当断点停到printf这一语句时，分别放到af和bf变量名上观察其值，<font color=blue>注意观察结果，af变量的实际结果为1111111.13，而bf变量的实际结果为1111111.1110000000，从这个范例中能感受到精度问题，af小数点后面从第2位开始，这进一步证明了double数据类型比float数据类型所能保存的数据精度要高很多。</font>

继续看如下范例：
```c
float af1 = 0.5;    //显示0.50000000
float af2 = 0.51;   //显示0.509999990，它为什么显示的不是0.51000000，丢失了精度。
```
  通过设置断点观察这两个变量，能够发现，明明给af2的值是0.51，但显示出来的却是0.509999990，为什么？
    <font face="楷体" size=4 color=red>原来，当把一个十进制数值赋给一个实型变量时，计算机会把该十进制数转换成二进制数保存，当程序执行流程在断点上，用鼠标查看该变量值时，计算机实际上是把它保存的二进制数再转换成十进制数显示出来，这个步骤-->"十进制数$\rightarrow$二进制数，二进制数$\rightarrow$十进制数"中,存在着一些除法运算，这些除法运算因无法整除的原因，会导致从二进制转换回十进制数时丢失精度。</font>例如日常生活中用10除以3，那么结果将会是3.33333...，永远无法整除，是一样的道理。

#### 1.1.5字符型数据

##### 1. 字符常量



