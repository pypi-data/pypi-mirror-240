# PythonXlsxManger

由于工作中偶尔需要编写一些表格数据处理脚本，而其中大部分代码都是重复的，所以为了更好的开发效率，我决定将日常表格管理脚本中用到的基础功能集合起来并使用开源都方式共享，同时也希望有更多人能够一起完善。

## 简介

[PythonXlsxManger Gitee项目](https://gitee.com/liumou_site/pxm)（Python Linux基础模块: `pxm`）是使用Python3基于现有`openpyxl`模块编写的表格读写基础模块，实现常用功能。
在模块设计上，借鉴了Shell语言`管道`的特性,可一步步截取`列`、`行`数据(`Cut`开头的函数)


## 特色

* 使用全中文注释，即使小白也能轻松上手
* 完全开源、永久免费

# 使用方法

## 安装

具体可以访问Pypi项目地址[https://pypi.org/project/pxm](https://pypi.org/project/pxm)

```shell
pip3 install --upgrade pxm-liuyi778-Stable
```



# Demo

## 读取

```python
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   demo.py
@Time    :   2023-02-17 23:36
@Author  :   坐公交也用券
@Version :   1.0
@Contact :   faith01238@hotmail.com
@Homepage : https://liumou.site
@Desc    :   当前文件作用
"""
from ColorInfo import ColorLogger

from pxm_liuyi778_Stable import Read


class Demo:
	def __init__(self, filename="xls/demo.xlsx"):
		"""

        :param filename:
        """
		self.filename = filename
		self.logger = ColorLogger(class_name=self.__class__.__name__)
		self.r = Read(filename=self.filename)  # 读取文件
		self.r.set(sheet_index=1)  # 设置Sheet索引值1（也就是第二个Sheet)
		self.r.get_all()  # 获取所有数据

	def all(self):
		if self.r.Err:
			self.logger.error("读取失败: ", r.Err)
		else:
			self.logger.info("数据读取成功")
			print(self.r.DataR)

	def line(self):
		data = self.r.cut_line(0)  # 截取第一行并获取最终结果
		print("第一行的数据: ", data.DataR)

	def start(self):
		self.all()
		self.line()
		self.info()

	def info(self):
		print(f"当前工作簿数据总列数: {self.r.InfoCols}")
		print(f"当前工作簿数据总行数: {self.r.InfoRows}")
		print(f"当前工作簿索引值: {self.r.InfoSheet}")
		print(f"当前工作簿名称: {self.r.InfoSheetName}")


if __name__ == "__main__":
	d = Demo()
	d.start()

```

效果


```shell
2023-02-21 11:17:14 demo.py  line: 33 - Class: Demo Function: all - INFO : 数据读取成功
[['专业', '人数'], ['网络', 3], ['安全', 3]]
第一行的数据:  ['专业', '人数']
当前工作簿数据总列数: 2
当前工作簿数据总行数: 3
当前工作簿索引值: 1
当前工作簿名称: Sheet2
```
# 更新日志

* `1.0.5`: 更换日志管理器

# 问题反馈

点击链接加入QQ群聊【[坐公交也用券](https://jq.qq.com/?_wv=1027&k=FEeLQ6tz)】
