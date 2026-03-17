# Git相关指令

# [**如何优雅的删除子模块(submodule)或修改Submodule URL**](https://www.cnblogs.com/wangshuyi/p/13764717.html)

**1. 优雅的删除子模块[#](https://www.cnblogs.com/wangshuyi/p/13764717.html#1.-%E4%BC%98%E9%9B%85%E7%9A%84%E5%88%A0%E9%99%A4%E5%AD%90%E6%A8%A1%E5%9D%97)**

`*# 逆初始化模块，其中{MOD_NAME}为模块目录，执行后可发现模块目录被清空*
git submodule deinit {MOD_NAME} 
*# 删除.gitmodules中记录的模块信息（--cached选项清除.git/modules中的缓存）*
git rm --cached {MOD_NAME} 
*# 提交更改到代码库，可观察到'.gitmodules'内容发生变更*
git commit -am "Remove a submodule."` 

**2. 修改某模块URL[#](https://www.cnblogs.com/wangshuyi/p/13764717.html#2.-%E4%BF%AE%E6%94%B9%E6%9F%90%E6%A8%A1%E5%9D%97url)**
1. 修改'.gitmodules'文件中对应模块的”url“属性;
2. 使用`git submodule sync`命令，将新的URL更新到文件`.git/config`；

`thinker-g@localhost: ~/app$ git submodule sync 
Synchronizing submodule url for 'gitmods/thinker_g/Helpers'
thinker-g@localhost: ~/app$ *# 运行后可观察到'.git/config'中对应模块的url属性被更新*
thinker-g@localhost: ~/app$ git commit -am "Update submodule url." *# 提交变更*`

git submodule update --init --recursive

git submodule deinit -f rscommon