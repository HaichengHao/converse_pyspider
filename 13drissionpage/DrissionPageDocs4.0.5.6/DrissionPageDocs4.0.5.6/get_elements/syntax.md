---
id: syntax
title: '🔦 定位语法'
---

本节介绍 DrissionPage 自创的查找元素语法。

查找语法能用于指明以哪种方式去查找指定元素，定位语法简洁明了，熟练使用可大幅提高程序可读性。

所有涉及获取元素的操作都可以使用定位语法，如`ele()`、`actions.move_to()`、`wait.eles_loaded()`、`get_frame()`等等。

查找语法用于简化代码，提高可读性，但并不覆盖所有复杂场景。很复杂的场景可直接用 xpath 查找。

以下使用这个页面进行讲解。

```html
<html>
<body>
<div id="one">
    <p class="p_cls" id="row1" data="a">第一行</p>
    <p class="p_cls" id="row2" data="b">第二行</p>
    <p class="p_cls">第三行</p>
</div>
<div id="two">
    第二个div
</div>
</body>
</html>
```

## ✅️️ 基本概念

几乎所有查找方法都是基于元素属性进行。

元素属性包括以下三种：

|    写法     |说明| 示例                                   |
|:---------:|:---:|--------------------------------------|
| `@tag()`  |标签名| 即`<div id="one">`中的`div`             |
|  `@****`  |标签体中的属性| 如`<div id="one">`中的`id`，写作`'@id'`      |
| `@text()` |元素文本| 即`<p class="p_cls">第三行</p>`中的`'第三行'` |

查找语法就是按需要对这三种属性进行组合，达到查找指定元素的目的。

:::info 说明
    `@tag()`和`@text()`后面加上`'()'`，是为了避免和普通属性冲突。
:::

### 📌 简单示例

```python
tab.ele('@id=one')  # 获取第一个id为one的元素
tab.ele('@tag()=div')  # 获取第一个div元素
tab.ele('@text()=第一行')  # 获取第一个文本为“第一行”的元素
```

---

## ✅️️ 基本逻辑

### 📌 单属性匹配符 `@`

这种方式只有一个匹配条件，以`'@'`开头，后面跟属性名称。

上面简单示例中就是这种方式：`tab.ele('@id=one')`。

如果`@`后面只有属性名而没有属性值，查找有这个属性的元素，如`'tab.ele(@id)'`。

:::warning 注意
    如果属性中包含特殊字符（如包含`@`），用这个方式不能正确匹配到，需使用 css selector 方式查找。且特殊字符要用`\`转义。
:::

---

### 📌 多属性与匹配符 `@@`

当需要多个条件同时确定一个元素时，每个属性用`'@@'`开头。

:::warning 注意
    - 匹配文本或属性中出现`@@`、`@|`、`@!`时，不能使用多属性匹配，需改用 xpath 的方式。
    - 如果属性中包含特殊字符（如包含`@`），用这个方式不能正确匹配到，需使用 css selector 方式查找。且特殊字符要用`\`转义。
:::

**示例：**

```python
ele = tab.ele('@@class=p_cls@@text()=第三行')  # 查找class为p_cls且文本为“第三行”的元素
```

---

### 📌 多属性或匹配符 `@|`

当需要以或关系条件查找元素时，每个属性用`'@|'`开头。

:::warning 注意
    - 匹配文本或属性中出现`@@`、`@|`、`@!`时，不能使用多属性匹配，需改用 xpath 的方式。
    - 如果属性中包含特殊字符（如包含`@`），用这个方式不能正确匹配到，需使用 css selector 方式查找。且特殊字符要用`\`转义。
:::

**示例：**

```python
eles = tab.eles('@|id=row1@|id=row2')  # 查找所有id为row1或id为row2的元素
```

---

### 📌 否定匹配符 `@!`

用于否定某个条件。

如果`@!`后面只有属性名而没有属性值，查找没有这个属性的元素。

**示例：**

```python
ele = tab.ele('@!id=one')  # 获取第一个id等于“one”的元素
ele = tab.ele('@!class')  # 匹配没有class属性的元素
```

---

### 📌 混合使用

`@@`和`@|`不能同时出现的查找语句中，即一个查找语句只能是与关系或者或关系。

`@!`则可与两者混合使用。混用时，与还是或关系视`@@`还是`@|`而定。

:::info 说明
    当语句中有多个`tag()`时，如果全部都没有被`@!`修饰，它们是与关系；如有任一个被`@!`修饰，它们是或关系。
    `tag()`与其他属性之间是与关系。
:::

**示例：**

```python
# 匹配class等于p_cls且id不等于row1的元素
tab.ele('@@class=p_cls@!id=row1')

# 匹配class等于p_cls或id不等于row1的元素
tab.ele('@|class=p_cls@!id=row1')
```

---

## ✅️️ 匹配模式

匹配模式指某个查询中匹配条件的方式，有精确匹配、模糊匹配、匹配开头、匹配结尾四种。

:::warning 注意
    `tag()`属性无论用哪种匹配模式，都会视作`=`。
:::

### 📌 精确匹配 `=`

表示精确匹配，匹配完全符合的文本或属性。

```python
ele = tab.ele('@id=row1')  # 获取id属性为'row1'的元素
```

---

### 📌 模糊匹配 `:`

表示模糊匹配，匹配含有指定字符串的文本或属性。

```python
ele = tab.ele('@id:ow')  # 获取id属性包含'ow'的元素
```

---

### 📌 匹配开头 `^`

表示匹配开头，匹配开头为指定字符串的文本或属性。

```python
ele = tab.ele('@id^row')  # 获取id属性以'row'开头的元素
```

---

### 📌 匹配结尾 `$`

表示匹配结尾，匹配结尾为指定字符串的文本或属性。

```python
ele = tab.ele('@id$w1')  # 获取id属性以'w1'结尾的元素
```

---

## ✅️️ 常用语法

基于上述基本逻辑，本库提供了一些更已于使用和阅读的语法。

### 📌 id 匹配符 `#`

用于匹配`id`属性，**只在语句最前面且单独使用时生效**。相当于单属性查找`@id=****`。

可与匹配模式配合使用。

```python
ele = tab.ele('#one')  # 查找id为one的元素
ele = tab.ele('#=one')  # 和上面一行一致
ele = tab.ele('#:ne')  # 查找id属性包含ne的元素
ele = tab.ele('#^on')  # 查找id属性以on开头的元素
ele = tab.ele('#$ne')  # 查找id属性以ne结尾的元素
```

---

### 📌 class 匹配符 `.`

用于匹配`class`属性，**只在语句最前面且单独使用时生效**，相当于单属性查找`@class=****`。

可配合匹配模式使用。

:::info 说明
    在面对多个 class 的元素时，DrissionPage 与 selenium 处理方式不一样，无需将空格替换成`'.'`。
    而是将整个 class 视作普通字符串，空格视作普通字符对待，会比较直观。
:::

```python
ele = tab.ele('.p_cls')  # 查找class属性为p_cls的元素
ele = tab.ele('.=p_cls')  # 与上一行一致
ele = tab.ele('.:_cls')  # 查找class属性包含_cls的元素
ele = tab.ele('.^p_')  # 查找class属性以p_开头的元素
ele = tab.ele('.$_cls')  # 查找class属性以_cls结尾的元素
```

---

### 📌 文本匹配符 `text`

用于匹配元素文本。**只在语句最前面且单独使用时生效**，相当于单属性查找`@text()=****`。

可配合匹配模式使用。

如果元素内有多个直接的文本节点，精确查找时可匹配所有文本节点拼成的字符串，模糊查找时可匹配每个文本节点。

如果查找语句没有任何本节介绍的匹配符，默认模糊匹配文本。即`ele('第三行')`相当于`ele('text:第三行')`。

:::warning 注意
    如果要匹配的文本包含特殊字符（如`'&nbsp;'`、`'&gt;'`），需将其转换为十六进制形式，详见《语法速查表》一节。
:::

```python
ele = tab.ele('text=第二行')  # 查找文本为“第二行”的元素
ele = tab.ele('text:第二')  # 查找文本包含“第二”的元素
ele = tab.ele('第二')  # 与上一行一致
ele = tab.ele('第\u00A0二')  # 匹配包含&nbsp;文本的元素，需将&nbsp;转为\u00A0
```

:::tip Tips
    若要查找的文本包含`text:` ，可下面这样写，即第一个`text:` 为关键字，第二个是要查找的内容：
    ```python
    ele2 = tab.ele('text:text:')
    ```
:::

---

### 📌 类型匹配符 `tag`

用于匹配某类型元素。**只在语句最前面且单独使用时生效**，相当于单属性查找`@tag()=****`。

可与单属性查找或多属性配合使用。`tag:`与`tag=`效果一致，没有`tag^`和`tag$`语法。

```python
ele = tab.ele('tag:div')  # 查找第一个div元素
ele = tab.ele('tag:p@class=p_cls')  # 与单属性查找配合使用
ele = tab.ele('tag:p@@class=p_cls@@text()=第二行')  # 与多属性查找配合使用
```

:::warning 注意
    `tag:div@text():abc` 和 `tag:div@@text():abc` 是有区别的，前者只在`div`的直接文本节点搜索，后者搜索`div`的整个内部。
:::

---

### 📌 css selector 匹配符 `css`

表示用 css selector 方式查找元素。**只在语句最前面且单独使用时生效**。

`css:`与`css=`效果一致，没有`css^`和`css$`语法。

```python
ele = tab.ele('css:.div')  # 查找 div 元素
ele = tab.ele('css:>div')  # 查找 div 子元素元素，这个写法是本库特有，原生不支持
```

---

### 📌 xpath 匹配符 `xpath`

表示用 xpath 方式查找元素。**只在语句最前面且单独使用时生效**。

`xpath:`与`xpath=`效果一致，没有`xpath^`和`xpath$`语法。  

:::tip Tips
    **元素对象**的`ele()`支持完整的 xpath 语法，如能使用 xpath 直接获取元素属性（字符串类型）。
:::

```python
ele2 = ele1.ele('xpath:.//div')  # 查找后代中第一个 div 元素
ele2 = ele1.ele('xpath://div')  # 和上面一行一样，查找元素的后代时，// 前面的 . 可以省略
ele_class_str = ele1.ele('xpath://div/@class')  # 使用xpath获取div元素的class属性（页面元素无此功能）
```

:::tip 说明
    查找元素的后代时，selenium 原生代码要求 xpath 前面必须加`.`，否则会变成在全个页面中查找。
    作者觉得这个设计是画蛇添足，既然已经通过元素查找了，自然应该只查找这个元素内部的元素。
    所以，用 xpath 在元素下查找时，最前面`//`或`/`前面的`.`可以省略。
:::

---

### 📌 selenium 的 loc 元组

查找方法能直接接收 selenium 原生定位元组进行查找，便于项目迁移。

```python
from DrissionPage.common import By

# 查找id为one的元素
loc1 = (By.ID, 'one')
ele = tab.ele(loc1)

# 按 xpath 查找
loc2 = (By.XPATH, '//p[@class="p_cls"]')
ele = tab.ele(loc2)  
```

---

## ✅️️ `@@text()`的技巧

值得一提的是，`text()`配合`@@`或`@|`能实现一种很便利的按查找方式。

网页种经常会出现元素和文本混排的情况，比如：

```html
<li class="explore-categories__item">
    <a href="/explore/new-tech" class="">
        <i class="explore"></i>
        前沿技术
    </a>
</li>
<li class="explore-categories__item">
    <a href="/explore/program-develop" class="">
        <i class="explore"></i>
        程序开发
    </a>
</li>
```

示例中，如果要用文本获取`'前沿技术'`的`<a>`元素，可以这样写：

```python
ele = tab.ele('text:前沿技术')
# 或
ele = tab.ele('@text():前沿技术')
```

这两种写法都能获取到包含直接文本的元素。

但如果要用文本获取`<li>`元素，就获取不到，因为文本不是`<li>`的直接内容。

我们可以这样写：

```python
ele = tab.ele('tag:li@@text():前沿技术')
```

`@@text()`与`@text()`不同之处在于，前者可以搜索整个元素内所有文本，而不仅仅是直接文本，因此能实现一些非常灵活的查找。

:::warning 注意
    需要注意的是，使用`@@`或`@|`时，`text()`不要作为唯一的查询条件，否则会定位到整个文档最高层的元素。

    ❌ 错误做法：
    ```python
    ele = tab.ele('@@text():前沿技术')
    ele = tab.ele('@|text():前沿技术@|text():程序开发')
    ```
    
    ⭕ 正确做法：
    ```python
    ele = tab.ele('tag:li@|text():前沿技术@|text():程序开发')
    ```
:::

--- 