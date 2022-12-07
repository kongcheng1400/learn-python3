# 使用 REGEXP

```python
import re

p = re.compile('ab*')
#
p = re.compile('ab*', re.IGNORECASE) #带一个参数
p.match('abcd')

m = re.search(r'(?<=-)\w+', 'spam-egg')

```