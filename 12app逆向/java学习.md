# Java学习  

- java需要先编译后执行  

- ``` cmd
  javac demo.java  
  java demo
  ```

- 注意:java文件的名称要和类名一致

- 如果有多个类，那么要和公有的类的名称一致

- 如果src文件中有多个.java文件，注意其中的类名不能够重复使用否则会报错

- 关于主函数

  - ```java
    public class Hello {
        public static void main(String[] args) {
            System.out.println("hello world");
        }
    }
    //这是.java文件中声明的主函数
    ```

  - ```python
    if __name__ == '__main__':
        pass #这是python文件中的主函数
    ```

  - 

## 00 java初体验  

### 用java实现helloworld 

```java
//用java实现helloword  
public class Hello{
    public static void main(String[] args){
        System.out.println("hello world")
    }
}
```

### java中的静态方法与绑定方法  

- 这里利用python与java实现对比  

  ```python
  class Mytest:
      # 绑定方法，需要创建实例对象，然后通过实例对象调用
      def f1(self):
          print("f1被调用了")
      # 静态方法,不需要创建实例对象就可以直接调用
      @staticmethod
      def f2():
          print("f2被调用了")
      def f3(self):
          return "f3被调用咯"
  
  if __name__ == '__main__':
  
      # 创建实例对象调用绑定方法
      obj = Mytest()
      obj.f1()
      # 尝试不通过实例对象调用类方法
      try:
          Mytest.f1()
      except BaseException as e:
          print(e)
      # '绑定方法是不能直接被类名.方法名调用的哦!!!'
      # 静态方法可以直接通过类名调用
      Mytest.f2()
      f3_runtimeresult = obj.f3()
      print(f3_runtimeresult)
  
  '''
  f1被调用了
  Mytest.f1() missing 1 required positional argument: 'self'
  f2被调用了''' 
  ```

  ```java
  public class Main {
      // important   静态方法
      public static void main(String[] args) {
          //   实例化方法
          Mytest obj = new Mytest();   //也就是创建一个实例对象绑定对应的类
  //    之后再调用这个创建的实例对象执行方法
          obj.f1();
          Mytest.f2();
          String f3_runtimeresult = obj.f3(); //tips:创建一个对象接收f3的返回值
          System.out.println(f3_runtimeresult); //tips:打印返回的结果
      }
  
  }
  
  class Mytest {
      public void f1() {//非静态方法，作为绑定方法
          System.out.println("f1被调用了");
      }
  
      public static void f2() {//静态方法可以不创建实例对象直接调用
          System.out.println("f2被调用了");
      }
  
      //    tips:如果带有返回值，那么要指定返回值类型，没有返回值的话就写void
      public String f3() {
          return "f3被调用咯";
      }
  
  }
  ```

  

### java中的参数传递  

```java
public class Hello {
    public static void main(String[] args) {
        Mytest1 obj = new Mytest1(); //创建实例对象
        int v1 = obj.f1(1, 2); //通过实例对象调用方法f1,传入两个整数1和2然后v1接收结果
        System.out.println(v1); //打印输出结果
    }
}
//创建一个类，名字为Mytest1,实现一个方法f1,能够返回两个整数相加的结果
class Mytest1 {
    public int f1(int a1, int a2) { //因为返回值是int类型，所以要将返回值类型设置为int
        int result = a1 + a2;
        return result;
    }
}
```

用python来理解就是

```python
def func1(a, b):
    result = a + b
    return result


if __name__ == '__main__':
    a = 1
    b = 2
    reslut = func1(a,b)
    print(reslut)
```

## 01Java基础

### 01.0 注释

```java
//单行注释 
/*多行注释*/
public class Hello {
    /**  敲进去一个/**之后回车,然后会出现如下可以指定parama和 args
     * 
     * @param args
     */
    public static void main(String[] args) {
        Mytest1 obj = new Mytest1();
        int v1 = obj.f1(1, 2);
        System.out.println(v1);
    }
}

class Mytest1 {
    public int f1(int a1, int a2) {
        int result = a1 + a2;
        return result;
    }
}
```

### 01.1  变量与常量  

```java
public class Demo {
    public static void main(String[] args){
        String name1 = "donny"; //声明变量
        name1 = "wiki"; //修改变量
        int age = 19; //同上
        age = 20;

        final int size = 10;  //前面加上final就是表示声明的是常量

    }
}

```



