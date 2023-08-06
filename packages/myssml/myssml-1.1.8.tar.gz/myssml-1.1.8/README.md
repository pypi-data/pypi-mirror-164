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