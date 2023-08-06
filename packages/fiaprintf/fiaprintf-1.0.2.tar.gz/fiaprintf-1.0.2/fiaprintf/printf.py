import os

os.system("")  # print颜色开启，如果关闭则不能在cmd中显示颜色

# windows仅支持8种颜色
# 黑色、红色、绿色、黄色、蓝色、紫红、靛蓝、白色
__color__ = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "purple-red": "35",
    "cyanine": "36",
    "white": "37",
    "default": "37",
}
# 黑色、红色、绿色、黄色、蓝色、紫红、靛蓝、白色
__background__ = {
    "black": "40;",
    "red": "41;",
    "green": "42;",
    "yellow": "43;",
    "blue": "44;",
    "purple-red": "45;",
    "cyanine": "46;",
    "white": "47;",
    "default": "",
}
# 默认、高亮、下划线、闪烁、反白、不显示
__effect__ = {
    "default": "0",
    "highlight": "1",
    "underline": "4",
    "flash": "5",
    "backwhite": "7",
    "unshow": "8",
}
# 类型：简化设置
__type__ = {
    "error": ["red", "underline", "default"],
    "warning": ["yellow", "default", "default"],
    "success": ["green", "default", "default"],
    "data": ["blue", "default", "default"],
    "system": ["cyanine", "default", "default"],
    "normal": ["default", "default", "default"],
}


class Format:
    def __init__(
            self,
            *values,
            _color="default",
            _effect="default",
            _background="default",
            _type=None,
            _isprint=True,
            sep=' ',
            end='\n',
            file=None,
            flush=False
    ):
        """

        :param values: 要打印的对象，可不输入，在打印函数输入
        :param _color: 打印颜色
        :param _effect: 打印亮度
        :param _background: 打印背景
        :param _type: 打印类型，可使用自定义类
        :param _isprint: 打印控制
        :param sep: 打印间隔
        :param end: 打印结尾
        :param file: 文件
        :param flush: 流
        """
        self.values = values
        self.color = _color
        self.effect = _effect
        self.background = _background
        self.type = _type
        self.isPrint = _isprint
        self.sep = sep
        self.end = end
        self.file = file
        self.flush = flush
        self.error = None

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if value is None or value in __color__:
            self.__color = value or "default"
        else:
            self.__color = "default"
            self.error = f"不存在对应颜色{value}"

    @property
    def effect(self):
        return self.__effect

    @effect.setter
    def effect(self, value):
        if value is None or value in __effect__:
            self.__effect = value or "default"
        else:
            self.__effect = "default"
            self.error = f"不存在对应亮度{value}"

    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, value):
        if value is None or value in __background__:
            self.__background = value or "default"
        else:
            self.__background = "default"
            self.error = f"不存在对应背景{value}"

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:
            self.__type = None
        elif value in __type__:
            self.__type = __type__[value]
        elif isinstance(value, (tuple, list)):
            if (__vLen := len(value)) == 0:
                self.error = "请检查输入的类型长度"
            self.__type = None
            self.color, self.effect, self.background = list(value) + ["default"] * (3 - __vLen)
        elif isinstance(value, dict):
            self.__type = None
            self.color = value.get("color", default="default")
            self.effect = value.get("effect", default="default")
            self.background = value.get("background", default="default")
        else:
            self.error = f"不存在对应背景{value}"

    def reset(self):
        self.color = "default"
        self.effect = "default"
        self.background = "default"
        self.type = None

    @property
    def isPrint(self):
        return self.__isPrint

    @isPrint.setter
    def isPrint(self, value):
        self.__isPrint = bool(value)

    def __str__(self):
        if self.type is not None:
            __c = self.type[0]
            __e = self.type[1]
            __b = self.type[2]
        else:
            __c = self.color
            __e = self.effect
            __b = self.background
        return f"\033[{__effect__[__e]};{__background__[__b]}{__color__[__c]}m" \
               f"{self.sep.join(map(str, self.values))}" \
               f"\033[0m{self.end}"

    def __repr__(self):
        return self.__str__()

    def __call__(
            self,
            *values,
            sep=None,
            end=None,
            file=None,
            flush=None
    ):
        if self.type is not None:
            __c = self.type[0]
            __e = self.type[1]
            __b = self.type[2]
        else:
            __c = self.color
            __e = self.effect
            __b = self.background
        __sep = self.sep if sep is None else sep
        __end = self.end if end is None else end
        __file = self.file if file is None else file
        __flush = self.flush if flush is None else flush
        print(
            f"\033[{__effect__[__e]};{__background__[__b]}{__color__[__c]}m"
            f"{__sep.join(map(str, values or self.values))}"
            f"\033[0m",
            end=__end,
            file=__file,
            flush=__flush
        )

    def __fill(self, fill_width, fill_char=" ", fill_type="L", fill_parameter=0.35):
        if len(fill_char) != 1:
            raise OverflowError("填充字符长度只能为1")
        if self.values:
            __value_temp = [
                str_just(
                    str(__value_i), fill_width, fill_char, _type=fill_type, _parameter=fill_parameter
                ) for __value_i in self.values
            ]
            return self.copy(*__value_temp)
        return self.copy()

    def left_just(self, fill_width, fill_char=" ", fill_parameter=0.60):
        return self.__fill(fill_width, fill_char, fill_type="L", fill_parameter=fill_parameter)

    def right_just(self, fill_width, fill_char=" ", fill_parameter=0.60):
        return self.__fill(fill_width, fill_char, fill_type="R", fill_parameter=fill_parameter)

    def center(self, fill_width, fill_char=" ", fill_parameter=0.60):
        return self.__fill(fill_width, fill_char, fill_type="C", fill_parameter=fill_parameter)

    def copy(self, *values):
        __values = values or self.values

        return Format(
            *__values,
            _color=self.color,
            _effect=self.effect,
            _background=self.background,
            _type=self.type,
            _isprint=self.isPrint,
            sep=self.sep,
            end=self.end,
            file=self.file,
            flush=self.flush
        )


def printf(
        *values,
        _color="default",
        _effect="default",
        _background="default",
        _type=None,
        _isprint=True,
        sep=' ',
        end='\n',
        file=None,
        flush=False
):
    if _type is not None:
        __c = _type[0]
        __e = _type[1]
        __b = _type[2]
    else:
        __c = _color
        __e = _effect
        __b = _background
    print(
        f"\033[{__effect__[__e]};{__background__[__b]}{__color__[__c]}m"
        f"{sep.join(map(str, values))}"
        f"\033[0m",
        end=end,
        file=file,
        flush=flush
    )


def str_just(_string, _length, _fill_char=" ", _type="L", _parameter=0.6):
    """
    中英文混合字符串对齐函数
    str_just(_string, _length[, _type]) -> str


    :param _string:[str]需要对齐的字符串
    :param _length:[int]对齐长度
    :param _fill_char:[str]填充字符
    :param _type:[str]对齐方式（'L'：默认，左对齐；'R'：右对齐；'C'或其他：居中对齐）
    :param _parameter:[float] 长度调节参数
    :return:[str]输出_string的对齐结果
    """
    _str_len = len(_string)
    num = sum('\u2E80' <= _char <= '\uFE4F' for _char in _string)
    _str_len += num * _parameter
    _space = round(_length - _str_len)
    if _type == 'L':
        _left = 0
        _right = _space
    elif _type == 'R':
        _left = _space
        _right = 0
    else:
        _left = _space // 2
        _right = _space - _left
    return f"{_fill_char}" * _left + _string + f"{_fill_char}" * _right


if __name__ == '__main__':
    a = Format("eee", _color="red")
    a()
