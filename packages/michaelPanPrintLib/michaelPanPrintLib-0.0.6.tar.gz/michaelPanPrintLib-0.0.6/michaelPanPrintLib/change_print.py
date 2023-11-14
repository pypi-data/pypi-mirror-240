# ***************************************************************
# Maintainers:
#     chuntong pan <panzhang1314@gmail.com>
# Date:
#     2023.6 ~ 2023.11
# ***************************************************************
import os
import sys
import inspect
import datetime
import numpy as np
"""
	1.改变原有python的控制台打印样式
	2.旨在简单高效  	✅  ⚠️  🚀
	3.更新记录：
		0.0.1 初始测试版本
		0.0.2 正式版本，没有修改内容
		0.0.3 增加了对循环打印显示的支持，增加了对多个打印参数的支持，增加了ndarray的显示支持
		0.0.4 增加了是否使用颜色的开关
		0.0.5 增加了库检测和自动安装功能
		0.0.6 增加了方法调用时的固定输出
"""
args = "🚀欢迎使用改变打印样式功能，本程序作者是michaelPan，如果有任何问题请联系：panzhang1314@gmail.com🚀"
print(f"{os.path.basename(__file__)}:24 【{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】 {args}")


def print_with_style(*args, no_color=False, color='red', flush=False, switch_line=False):
	"""
	:param args: 要打印的字符串
	:param no_color: 不使用颜色
	:param color: 打印字体颜色
	:param flush: 是否在同一行刷新显示
	:param switch_line: 是否在打印完成后切换一行，主要在同一行输出时使用
	:return: 无返回值
	"""
	# ---------增加对多个参数的支持,更换字符串----------
	temp_str = ''
	for a_str in args:
		if isinstance(a_str, np.ndarray):  # 当为numpy数组时增加换行
			temp_str += '\n'
		temp_str += str(a_str)
	args = temp_str
	# ---------------------------------------------
	if not no_color:  # 改变颜色的情况
		from colorama import Fore, Style
		if color == "red":
			color = Fore.RED
		elif color == "black":
			color = Fore.BLACK
		elif color == "white":
			color = Fore.WHITE
		elif color == "magenta":
			color = Fore.MAGENTA
		elif color == "green":
			color = Fore.GREEN
		elif color == "yellow":
			color = Fore.YELLOW
		elif color == "blue":
			color = Fore.BLUE
		elif color == "cyan":
			color = Fore.CYAN
		else:
			raise Exception("未找到该颜色")
		args = f"{color}{Style.BRIGHT}{args}{Style.RESET_ALL}"
	frame = inspect.stack()[1]  # 获取代码位置
	info = inspect.getframeinfo(frame[0])
	# 打印代码位置和要输出的内容
	if flush:  # 是否在同一行显示
		print(f"\r{os.path.basename(info.filename)}:{info.lineno}【{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】 {args}", end="")
		sys.stdout.flush()
	else:
		print(f"{os.path.basename(info.filename)}:{info.lineno}【{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}】 {args}")
	if switch_line:
		print()  # 换行用
