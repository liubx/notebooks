# Ubuntu下vi输入i不进入insert插入模式

修改/etc/vim/vimrc.tiny 文件，将set compatible 设置成set nocompatible . 保存退出即可。这是因为有时候系统会默认vim兼容vi，所以使用vi的命令