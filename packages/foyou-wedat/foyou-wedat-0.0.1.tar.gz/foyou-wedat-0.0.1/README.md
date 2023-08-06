# foyou-wedat
微信 dat 文件解密


## 设计一下

```shell
wedat --version 打印版本信息

wedat --help 显示帮助信息

wedat <file1.dat> <file2.dat> ... [-o/--out <输出目录>(默认 .)]

wedat -d/--dir <源目录> [-o/--out <输出目录>(默认 ., 只处理 .dat 文件)]
```