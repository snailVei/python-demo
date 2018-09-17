# 模块（module）

# 在Python中一个py文件就是一个模块，要想创建模块，实际上就是创建一个python文件
# 注意：模块名要符号标识符的规范

# 在一个模块中引入外部模块
# ① import 模块名 （模块名，就是python文件的名字，注意不要py）
# ② import 模块名 as 模块别名
#   - 可以引入同一个模块多次，但是模块的实例只会创建一个
#   - import可以在程序的任意位置调用，但是一般情况下，import语句都会统一写在程序的开头
#   - 在每一个模块内部都有一个__name__属性，通过这个属性可以获取到模块的名字
#   - __name__属性值为 __main__的模块是主模块，一个程序中只会有一个主模块
#       主模块就是我们直接通过 python 执行的模块
import test_module as test

# test_module
# __main__
print(test.__name__)
print(__name__)


