# opencv installing  for ubuntu 14.04

步骤：

## 1 downloads

首先，去OpenCV下载相应版本的OpenCV安装包。

## 2 安装一些必要的依赖

包括libgtk2.0-dev和pkg-config.在Ubuntu系的安装方法是sudo apt-get install libgtk2.0-dev pkg-config build-essential

## 3 cmake 

由于OpenCV使用cmake来组织整个项目，所以还必须在你的Linux上安装cmake.安装方法也很简单，在终端中输入sudo apt-get install cmake


进入到刚刚解压出来的目录，可以看到有CMakeLists.txt等一堆文件。将终端cd到这个目录，并执行cmake .（注意，cmake命令后面隔着一个空格，然后带了一个.）

## 4 make && sudo make install

在终端中编译sudo make && sudo make install.
