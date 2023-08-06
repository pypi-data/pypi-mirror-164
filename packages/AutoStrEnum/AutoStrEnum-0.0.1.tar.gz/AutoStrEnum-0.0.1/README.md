# AutoStrEnum

This project defines an extended `Enum` class.  
It can automatically assign the value to your Enum member, and the value is just the same as the member name!  
And when you print it, you won't see the Enum name in front of the class member.

## Install

```shell
pip install AutoStrEnum
```

## Basic use

```python
from enum import auto
from AutoStrEnum import AutoStrEnum

class Fruit(AutoStrEnum):
    BANANA = auto()
    WATERMELON = auto()
    DURIAN = auto()

if __name__ == '__main__':
    print(Fruit.BANANA, Fruit.WATERMELON, Fruit.DURIAN)
```

```shell
$ python demo.py
BANANA WATERMELON DURIAN
```

You can check all the example at [demo.py](https://github.com/PttCodingMan/AutoStrEnum/blob/main/demo.py)