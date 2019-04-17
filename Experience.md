1. python function返回的东西越多，整个函数运行速度越慢.
2. # python class 
   # def python __del__ func
   class Point:
      def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
      def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"
  #--------------------------- result ----------------------#
  pt1 = Point()
  pt2 = pt1
  pt3 = pt1
  print id(pt1), id(pt2), id(pt3) # 打印对象的id
  del pt1
  del pt2
  del pt3
  #--------------------------- result ----------------------#
  3083401324 3083401324 3083401324
  Point destroyed
3. 单下划线、双下划线、头尾双下划线说明：
  __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。 
  _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
  __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
4. 
