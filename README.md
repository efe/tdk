# tdk

[![Travis](https://img.shields.io/travis/efe/tdk.svg)](https://travis-ci.org/efe/tdk/)
[![PyPI version](https://img.shields.io/pypi/v/tdk.svg)](https://pypi.org/project/tdk/)
[![codecov](https://codecov.io/gh/efe/tdk/branch/master/graph/badge.svg)](https://codecov.io/gh/efe/tdk)
[![License](https://img.shields.io/pypi/l/tdk.svg)](https://pypi.org/project/tdk/)

A library to query meaning of Turkish word from official dictionary.


## Install
```
$ pip install tdk
```
    
## Requirements
Python +3.4

## Documentation 

### Command Line
```
$ tdk efe
a. 1. Yiğit, özellikle Batı Anadolu köy yiğidi, zeybek. 2. Ağabey. 3. Kabadayı: Düğünevinin avlusuna girerken yeni düze inmiş efeler gibi nara attı. -Ö. Seyfettin. 4. tar. Kaptan.
```

### Library
```python
from tdk.core import TurkishWord

word = TurkishWord('Atatürk')
word.query()
result = word.meaning

print(result)
"Cinsiyet: Erkek1. Türklerin atası. 2. Büyük kurtarıcı Gazi Mustafa Kemal Paşa'ya 1934 yılında yasayla verilmiş soyadı."
```
