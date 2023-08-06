# MySSML

PySSML is an SSML builder for Amazon Alexa inspired by and based on JavaScript project https://github.com/mandnyc/ssml-builder.

MySSML is a new ver based PySSML modify by rdaim

A sample Alexa skill may be found here https://github.com/sumsted/alexa_pyssml.

pySSML can be found here: https://github.com/sumsted/pyssml

thanks for Scott Umsted!

## Installation

```
pip install myssml
```

## Usage

1. Create a MySSML object

    ```
    from myssml.MySSML import MySSML

    s = MySSML()

    # set automark
    #s.automark = True

    # set default speaker with chinese name or english name
    s.defaut_speaker = "晓晓"

    ```

2. Add your speech text

    ```
    s.say('Hello')
    s.s("no voice?")
    # or like this:
    s.voice("hi,我是晓晓")\
        .silence(value="2000ms")\
        .style(style="sad")\
        .mark("fuck")\
        .p("我来测试一下，")\
        .say("这是什么意思？")\
        .s('我的天呀！')\
        .pause("2000ms")\
        .lang("你好")\
        .s("从来没想过会这样!")
    ```

3. Retrieve your SSML

    ```
    res = s.ssml()      # to retrieve ssml with <speak> wrapper
    print(res)
    s.saveXML(res,"test.xml")
    ```

## Version Change Log


1.1.8
    2022-8-21
    完成基础架构


1.1.9
    2022-8-22
    新增是否自动分句
    新增中英文分句功能
    自动标签与自动分句功能相融合


1.1.10
    2022-8-23
    优化中英文分句功能
    新增加获取 marks 列表，并根据静音规则计算 offset 值

1.1.12
    2022-8-24
    修订了正文发音人数据，新增8个
    新增 get_speakers 方法

1.1.13
    2022-8-24
    自动标签模式下，支持对prosody添加标签

1.1.14
    2022-8-24
    修正get_marks中返回文本
    修正BGM层级关系为ROOT，且标注，长视频API模式下不支持背景音乐    

1.1.15
    2022-8-25
    修正元素之间的嵌套关系
    修正prosody中rate的值表达
    修正中文发音人为有效的13人，不包括香港和台湾   