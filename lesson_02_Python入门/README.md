# 第二章 Python入门（视频11-38）

## 编译型语言和解释型语言
    根据转换时机的不同，语言分成了两大类：
        编译型语言
            - C语言
            - 编译型语言，会在代码执行前将代码编译为机器码，然后将机器码交由计算机执行
            - a(源码) --编译--> b(编译后的机器码)
            - 特点：执行速度特别快,跨平台性比较差
        解释型语言 
            - Python JS Java
            - 解释型语言，不会在执行前对代码进行编译，而是在执行的同时一边执行一边编译
            - a（源码）--解释器--> 解释执行  
            - 特点： 执行速度比较慢,跨平台性比较好   
## Python的介绍   
    Python是解释型语言  
    Python的用途：WEB应用 爬虫程序 科学计算 自动化运维 大数据（数据清洗） 云计算 桌面软件/游戏 人工智能 。。。     
## Python的交互界面
    CMD中：
        版本和版权声明：
        Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        命令提示符：>>>
    IDLE：
        安装Python的同时，会自动安装一个Python的开发工具IDLE，通过IDLE也可以进入到交互模式
        但是不同的是，在IDLE中可以通过TAB键来查看语句的提示，可以有一些简单的提示，并且可以将代码保存，f5执行python代码 
## Python和Sublime的整合
    1.在Sublime中执行Python代码，ctrl + b 自动在Sublime内置的控制台中执行  
        这种执行方式，在某些版本的Sublime中对中文支持不好，并且不能使用input()函数
    2.使用SublimeREPL来运行python代码    
        安装完成，设置快捷键，希望按f5则自动执行当前的Python代码
        { "keys": ["f5"], "caption": "SublimeREPL:Python","command": "run_existing_window_command", "args":{"id": "repl_python_run","file": "config/Python/Main.sublime-menu"}},
## 基本语法
    1.在Python中严格区分大小写
    2.Python中的每一行就是一条语句，每条语句以换行结束
    3.Python中每一行语句不要过长（规范中建议每行不要超过80个字符）
        "rulers":[80],
    4.一条语句可以分多行编写，多行编写时语句后边以\结尾  
    5.Python是缩进严格的语言，所以在Python中不要随便写缩进  
    6.在Python中使用#来表示注释
## 快捷键
    快速注释代码 ctrl+/
    换行 ctrl+enter
## 数据类型   
    在Python数值分成了三种：整数、浮点数（小数）、复数
    在Python中所有的整数都是int类型
    Python中的整数的大小没有限制，可以是一个无限大的整数
    如果数字的长度过大，可以使用下划线作为分隔符 c = 123_456_789
    d = 0123 10进制的数字不能以0开头
    d = 0b10 # 二进制 0b开头
    d = 0o10 # 八进制 0o开头
    d = 0x10 # 十六进制 0x开头
## 变量和对象
    - 对象并没有直接存储到变量中，在Python中变量更像是给对象起了一个别名
    - 变量中存储的不是对象的值，而是对象的id（内存地址），
        当我们使用变量时，实际上就是在通过对象id在查找对象
    - 变量中保存的对象，只有在为变量重新赋值时才会改变
    - 变量和变量之间是相互独立的，修改一个变量不会影响另一个变量

    - 参考 图3

## 类型转换
    - 类型转换不是改变对象本身的类型，而是根据当前对象的值创建一个新对象

