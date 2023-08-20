# YaXin-ISA

#### 介绍
emmm，一个设想中的多核架构。模版核心还在开发

#### 架构
架构说明

基础的部分如图所示：
![image](https://github.com/IsaacMaxwell80686/YaXIn-ISA/assets/123815501/9b9b8b1a-7441-4cab-b34a-a7379cea3374)

 **P-COS** 起到类似于 **BIOS** 的作用，但其本质上是一个 **内嵌式的微内核操作系统** ，通过深度定制绑定下半部分的硬件， **P-COS** 起到软硬件兼容层的效果--用户只需要对 **P-COS** 进行编程就可以了。

 **P-COS** 通过 **线程指导器** 直接调度 **核心集群** ，最后作用于 **核心簇** 内的每一个核心。换言之，只要合理改进 **P-COS** 的软件，就可以在一定程度上提升多任务的处理速度。

以下是设计的汇编代码与对应数字指令：
| First Family | 00 Computing |  |  | 01 UnComputing |  |
| --- | --- | --- | --- | --- | --- |
| Second Family | 0011 Basic | 0001 Addition | 0010 Vector | 010 Ram | 011 Logic |
| Instruction Name | add 001100 | x 000100 | V1 001000 | write 010000 | PureE(=) 011000 |
|  | sub 001101 | / 000101 | V2 001001 | copy 010001 | PureB(>) 011001 |
|  |  |  |  | cut 010010 | PureN 011010 |
|  |  |  |  | clean 010011 | jump 010011 |

举个例子，将X1和X2内存的两个数加起来，用的就是：

```
add X1 X2 #汇编
```
转换之后就是：

```
001100 0000000000000 0000000000001 #机器码
```

#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
