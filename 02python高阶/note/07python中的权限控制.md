# 面向对象的三大特征


| 封装                             | 继承                                                                                      | 多态                                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 隐藏内部细节<br>对外提供操作方式 | 是在函数调用是时，使用`形参名称=值`<br>的方式进行传参，传递参数顺序可以与定义时的顺序不同 | 是在函数`定义`时直接对形参进行赋值，在调用时如果该参数不传值，将使用默认值，如果该参数传值，则使用传递的值 |

## 权限控制

- 方式 : 是通过对属性或方法添加单下划线、双下划线以及首尾双下划线来实现
- 区分方式


  | 开头方式     | 含义                                                                                                                                          |
  | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  | 单下划线开头 | 以单下划线开头的属性或方法表示protected受保护的成员，<br />这类成员被视为仅供内部使用，允许类本身和子类进行访问，但实际上它可以被外部代码访问 |
  | 双下划线开头 | 表示private私有成员，这类成员只允许定义该属性或方法的类本身进行访问                                                                           |
  | 首位双下划线 | 一般表示特殊方法                                                                                                                              |

### <bl>注意：<bl> 
私有属性和私有方法并非真正不可以被外部访问，只是访问方式不是普通的方式，
如果想要访问，语法如下
`实例对象名._类名__要访问的私有属性/方法`