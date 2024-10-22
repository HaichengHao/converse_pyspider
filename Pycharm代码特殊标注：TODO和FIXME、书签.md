 

本文内容参考  
1、[pycharm代码特殊标注：TODO和FIXME、书签](https://zhuanlan.zhihu.com/p/550883786)  
2、[PyCharm使用技巧：TODO（代码特殊注释技术）](https://blog.csdn.net/xiemanR/article/details/73368440)  
3、[Pycharm 官方文档](https://www.jetbrains.com/help/pycharm/2022.3/bookmarks.html)

### 一、适用情景

1、如果处理大型项目，搜索文件和文件夹可能会很耗时。对于这种情况，PyCharm提供了书签功能，可以收藏必要的代码行。还可以将经常需要的项目文件和文件夹添加为书签。

2、编码时会经常有需要特别标注提醒自己的地方，但是，仅用 **#** 符号太过单一。PyCharm 允许添加特殊类型的注释，这些注释在编辑器中突出显示、已编入索引并在 TODO 工具窗口中列出。这样就可以跟踪需要注意的问题。因此Pycharm里面支持代码特殊注释，包括TODO和FIXME。**注意：此功能在 PyCharm 的教育版中不可用。**

*   **TODO：** ：TODO表示这个地方需要实现一些功能，现在还没来得及做，先做个标记防止遗忘。
*   **FIXME：** ：FIXME表示需要修复的bug，优先级比较高。

* * *

### 二、代码特殊标注

特殊注释TODO和FIXME  
**step1：代码标注**  
**a、** 在所需标注的代码对行，先写#TODO：再写中文注解。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/987000233ae799b9c50bcf280ce6cd32.png)

**b、** 另外一种标注是，先写#FIXME：再写中文注解。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e40b43a255f872d9b2d5171fdbd75581.png)

**step2：TODO查找界面：**  
把鼠标移到PyCharm左下角的矩形内，在弹出的菜单中点击TODO进入TODO界面。TODO界面会列出代码中所有的特殊注释包括TODO和FIXME。在TODO界面中点击某一行可以跳转到对应的代码中。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d21c44f6cca198b074be117f2a62e885.png)

### 三、书签

PyCharm有两种类型的书签：

1.  **匿名书签** 没有标识符，允许您放置任意数量的书签。标有匿名书签的文件和行具有书签图标。
2.  **助记符书签**允许创建带有数字（0 到 9）或字母（A 到 Z）的书签。用助记符书签标记的文件和行在框架中具有相应的字母或数字图标。  
    ![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/a3a98edbfd7a6f0fd8f94d38483edf42.png)

##### 添加匿名行书签

*   在编辑器中，将插入符号放在代码行处，然后按 **F11**
*   或者，右键单击要添加书签的代码行旁边的装订线，然后选择“**添加书签**”。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/eae5ef73a15c09424b1454c1f3e99a32.png)  
    书签图标将显示在书签行旁边的装订线中。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/49295de3514d1d2218c65ea4517e789e.png)

##### 添加助记符行书签

1.  在编辑器中，将插入符号放在代码行处，然后按 **CTRL+F11** 或者，右键单击要添加书签的代码行旁边的装订线，然后选择“添加助记符书签”。
2.  在打开的弹出窗口中，选择要用作此书签标识符的数字或字母。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/0fdb8b5db98ddf55f3827aa6d07b1979.png)
3.  提供新书签的说明(Factorial calculation 处)。（可选）
4.  按下**Enter**或再次单击所选字母或数字以保存书签。  
    \*\* 字母或数字书签图标将显示在书签行旁边的装订线中\*\*
5.  跳转到带有数字的助记书签，按住**Ctrl**和键盘上的助记符数字。例如，要跳转到带有助记符 5 的书签，按 **Ctrl+5**

### 最后

Pycharm官方文档写的很详细，这些是我感觉常见的用法，其实并不完全。大家可以看一下官方的文档，写的很详细且有例图

本文转自 <https://blog.csdn.net/zw_lucky/article/details/129846598>，如有侵权，请联系删除。