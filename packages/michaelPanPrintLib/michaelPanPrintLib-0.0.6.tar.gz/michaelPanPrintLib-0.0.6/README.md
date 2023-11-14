# Changing the console output style library

## 1.Introduction

> Hello user, I am the author of this library. Are you still troubled by boring programming, are you used to the colorless black and white console output, are you still at a loss for which part of the code has a bug, using this library can perfectly solve these problems . This library relies on the colorama library and datetime library. When printing the information to be output, it will automatically add the name of the running file and the number of lines of code in front, and change the output color at the same time.

## 2.Use method

```python
# pip install michaelPanPrintLib
"""
	########change print########
	from michaelPanPrintLib.change_print import print_with_style
	# normal
	print_with_style('what you want to output', color=color='red')  # color also have black,white,magenta,green,etc
	# circulation
	for i in range(6):
        if i != 5:
            print_with_style(f"hello world | {i}", color='cyan', flush=True)
        else:
            print_with_style(f"hello world | {i}", color='cyan', flush=True, switch_line=True)
	print_with_style(f"hello world | {6}", color='cyan')
	
	#########check and install lib#########
	from michaelPanPrintLib.install_lib import check_and_install_lib
	check_and_install_lib(['torch', 'numpy'])  # check torch and numpy lib, it will auto install if not exist
"""
```

## 3.Contact information

```python
# ***************************************************************
# Maintainers:
#     chuntong pan <panzhang1314@gmail.com>
# Date:
#     2023.11
# ***************************************************************
```

