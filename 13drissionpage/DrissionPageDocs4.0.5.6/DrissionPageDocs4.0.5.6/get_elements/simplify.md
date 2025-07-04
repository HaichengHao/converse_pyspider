---
id: simplify
title: '🔦 简化写法'
---

<div class="wwads-cn wwads-horizontal" data-id="317"></div><br/>

为进一步精简代码，定位语法都可以用简化形式来表示，使语句更短，链式操作时更清晰。

## ✅️ 定位符语法简化

- 定位语法都有其简化形式
- 页面和元素对象都实现了`__call__()`方法，所以`page.ele('****')`可简化为`page('****')`
- 查找方法都支持链式操作

示例：

```python
# 查找tag为div的元素
ele = tab.ele('tag:div')  # 原写法
ele = tab('t:div')  # 简化写法

# 用xpath查找元素
ele = tab.ele('xpath://****')  # 原写法
ele = tab('x://****')  # 简化写法

# 查找text为'something'的元素
ele = tab.ele('text=something')  # 原写法
ele = tab('tx=something')  # 简化写法
```

简化写法对应列表

|    原写法    |  简化写法   |               说明                |
|:---------:|:-------:|:-------------------------------:|
|   `@id`   |   `#`   |  表示 id 属性，简化写法只在语句最前面且单独使用时生效   |
| `@class`  |   `.`   | 表示 class 属性，简化写法只在语句最前面且单独使用时生效 |
|  `text`   |  `tx`   |              按文本匹配              |
| `@text()` | `@tx()` |      按文本查找，与 @ 或 @@ 配合使用时       |
|   `tag`   |   `t`   |             按标签类型匹配             |
| `@tag()`  | `@t()`  |      按元素名查找，与 @ 或 @@ 配合使用时      |
|  `xpath`  |   `x`   |         用 xpath 方式查找元素          |
|   `css`   |   `c`   |      用 css selector 方式查找元素      |

---

## ✅️ shadow root 简化

一般获取元素的 shadow root 元素，用`ele.shadow_root`属性。

由于此属性经常用于大量链式操作，名字太长影响可读性，因此可简化为`ele.sr`

**示例：**

```python
txt = ele.sr('t:div').text
```

---

## ✅️ 相对定位参数简化

相对定位时，有时需要获取当前元素后某个元素，而不关心该元素是什么类型，一般是这样写：`ele.next(index=2)`。

但有一种简化的写法，可以直接写作`ele.next(2)`。

当第一个参数`filter_loc`接收数字时，会自动将其视作序号，替代`index`参数。因此书写可以稍微精简一些。

**示例：**

```python
ele2 = ele1.parent(2)
ele2 = ele1.next(2)('tx=****')
ele2 = ele1.before(2)
# 如此类推
```
