# YaXin-ISA

### 介绍

emmm，一个设想中的多核架构。模版核心还在开发

### 架构

架构说明

基础的部分如图所示：

![image](https://github.com/IsaacMaxwell80686/YaXIn-ISA/assets/123815501/758f43e5-15b0-4d01-a406-f13722e2a1a0)


**P-COS**起到类似于**BIOS**的作用，但其本质上是一个**内嵌式的微内核操作系统**，通过深度定制绑定下半部分的硬件，**P-COS**起到软硬件兼容层的效果--用户只需要对**P-COS**进行编程就可以了。**P-COS** 通过 **线程指导器** 直接调度 **核心集群** ，最后作用于 **核心簇** 内的每一个核心。换言之，只要合理改进 **P-COS** 的软件，就可以在一定程度上提升多任务的处理速度。

以下是设计的汇编代码与对应数字指令：

| First Family | 00 Computing |  |  | 01 UnComputing |  |
| --- | --- | --- | --- | --- | --- |
| Second Family | 0011 Basic | 0001 Addition | 0010 Vector | 010 Ram | 011 Logic |
| Instruction Name | add 001100 | x 000100 | V1 001000 | write 010000 | PureE(=) 011000 |
|  | sub 001101 | / 000101 | V2 001001 | copy 010001 | PureB(>) 011001 |
|  |  |  |  | cut 010010 | PureN 011010 |
|  |  |  |  | clean 010011 | PC_jump 010011 |

举个例子，将X1和X2内存的两个数加起来，用的就是：

```swift
add X1 X2 #汇编
```

转换之后就是：

```makefile
001100 0000000000000 0000000000001 #机器码
```

# Part-2:编程语言

很显然，用户面向P-COS编程的时候需要使用到高级语言，但是因为目前核心尚不完善，所以我在python原有的函数中遴选9个开发了 **Micro-Py** 语言，使用Micro-Py语言可以将编程者从复杂的汇编代码编写中脱身而出。在这里是我刚开发的0.1版本，接下来我会将其独立成为一个全新的开源项目，并且使其支持原先开发的几款处理器架构。下面这是0.1版本的介绍.

## 1.if函数：

与python相同，if函数使用如下：

```python
if La true:
    print("HelloWorld")
#这个一句的意思是，若条件变量Xa中存储的值为真(1)则执行下面的打印命令，否则直接跳过下面的打印命令
```

经过编译后，会变成如下代码：

```python
load Xj K #在Xj变量中载入跳转步数K，K的值取决于后面验证为真请款下汇编代码条数，使得pc的内存数值+k后可以正好跳过真情况下的最后一条指令。在这个例子中，k=1
pureE La XB Xp #通过pureE汇编代码对条件Xa进行真伪检验，若真，则在Xp变量存入数值1，若假则存入0
PC_jump Xp #通过PC_jump，在计数器里加入Xp的数值：若数值为0，则直接执行下一步的转跳指令；若为1，则会直接跳过下一条指令
PC_jump Xj #给pc加上Xj中的数值，使其跳过真情况
load Cache-Screen0("Helloworld") #真情况执行
```

## 2.if+else函数：

if+else函数使用如下：

```python
if La true:
    print("HelloWorld")
else:
    print("no")
```

经过编译后，会变成如下代码：

```python
load Xj K #在Xj变量中载入跳转步数K，K的值取决于后面验证为真请款下汇编代码条数，使得pc的内存数值+k后可以正好跳过真情况下的最后一条指令。在这个例子中，k=1
pureE La XB Xp #通过pureE汇编代码对条件Xa进行真伪检验，若真，则在Xp变量存入数值1，若假则存入0
PC_jump Xp #通过PC_jump，在计数器里加入Xp的数值：若数值为0，则直接执行下一步的转跳指令；若为1，则会直接跳过下一条指令
PC_jump Xj #给pc加上Xj中的数值，使其跳过真情况
load Cache-Screen0("Helloworld") #真情况执行
load Cache-Screen0("no") #假情况执行
```

## 3.for函数：

for函数使用如下：

```python
for time in (y): #执行下面代码y次
    print("HelloWorld")
    print("no")
```

经过编译后，会变成如下代码：

```python
#直接将内容代码复制5次即可
#第一轮循环
load Cache-Screen0("Helloworld")
load Cache-Screen0("no")
#第二轮循环
load Cache-Screen0("Helloworld")
load Cache-Screen0("no")
#第三轮循环
load Cache-Screen0("Helloworld")
load Cache-Screen0("no")
#第四轮循环
load Cache-Screen0("Helloworld")
load Cache-Screen0("no")
#第五轮循环
load Cache-Screen0("Helloworld")
load Cache-Screen0("no")
```

## 4.while函数：

while函数使用如下：

```python
while Xa ture:
     print("hellowowrld")
else:
    print("NO")
```

经过编译后，会变成如下代码：

```python
load Xl V #在Xl载入V值，V是判断为假后执行的步数，此处为2
load Xj K #在Xj变量中载入跳转步数K，K的值取决于后面验证为真请款下汇编代码条数，使得pc的内存数值+k后可以正好跳过真情况下的最后一条指令。在这个例子中，k=2
load Xc J #在Xc变量加载J值，J是从pureE开始直到调用J专跳的指令条数的负值
pureE La XB Xp #通过pureE汇编代码对条件Xa进行真伪检验，若真，则在Xp变量存入数值1，若假则存入0
PC_jump Xp #通过PC_jump，在计数器里加入Xp的数值：若数值为0，则直接执行下一步的转跳指令；若为1，则会直接跳过下一条指令
PC_jump Xj #给pc加上Xj中的数值，使其跳过真情况
load Cache-Screen0("Helloworld") #真情况执行
PC_jump Xl
load Cache-Screen0("no") #假情况执行
PC_jump Xc #跳回pureE处
```
