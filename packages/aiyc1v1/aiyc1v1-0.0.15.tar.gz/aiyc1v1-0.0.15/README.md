# Bornforthis Library Python 1v1

## What?

带编程一对一学员类基础练习所创建的代码，功能主要有：传入英文文本「.txt」，并调用，生成词云。

## Install

如果你换源了，请用下面的命令获取最新版本：

```python
pip install aiy1v1 -i https://pypi.org/simple
```

国内镜像源同步，比较缓慢，一般需要一天左右才会同步。

```python
pip install aiy1v1
```

## Upgrade

```python
pip3 install --upgrade aiyc1v1 -i https://pypi.org/simple
```

```python
pip3 install --upgrade aiyc1v1
```



## Github

[https://github.com/AndersonHJB/aiyc1v1](https://github.com/AndersonHJB/aiyc1v1)



## 已有功能代码

- [x] SimpleNLP：简单的自然语言处理代码「仅仅支持英文」——词频分析、词云生成
- [ ] GameBase：基础文字对话游戏
- [ ] 

## Error

### 2022年08月20日

```python
numpy.core._exceptions.UFuncTypeError: ufunc 'add' did not contain a loop with signature matching types (dtype('float64'), dtype('<U1')) -> None
```

预测是 dataframe to str 的错误，直接把读取到的结果，强制转换成 str

```python
self.content = str(pd.read_csv(self.path))
elf.content = str(pd.read_excel(self.path))
```

## 公众号：AI悦创【二维码】

欢迎关注我公众号：AI悦创，有更多更好玩的等你发现！

![](https://bornforthis.cn/gzh.jpg)

## info AI悦创·编程一对一

AI悦创·推出辅导班啦，包括「Python 语言辅导班、C++ 辅导班、java 辅导班、算法/数据结构辅导班、少儿编程、pygame 游戏开发」，全部都是一对一教学：一对一辅导 + 一对一答疑 + 布置作业 + 项目实践等。当然，还有线下线上摄影课程、Photoshop、Premiere 一对一教学、QQ、微信在线，随时响应！微信：Jiabcdefh

C++ 信息奥赛题解，长期更新！长期招收一对一中小学信息奥赛集训，莆田、厦门地区有机会线下上门，其他地区线上。微信：Jiabcdefh

方法一：[QQ](http://wpa.qq.com/msgrd?v=3&uin=1432803776&site=qq&menu=yes)

方法二：微信：Jiabcdefh


![](https://bornforthis.cn/zsxq.jpg)