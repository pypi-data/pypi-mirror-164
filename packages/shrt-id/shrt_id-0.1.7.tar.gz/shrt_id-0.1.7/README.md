# Fastest way to create Short Id

### How we create short id

Under writing

### Install shrt_id

```
pip install shrt_id
```

### Use shrt_id

Simple use

```python
from shrt_id import ShortId
id = ShortId().id()
print(id)
# wiwdhP8Q (default length is 8)
```

Custom length

```python
from shrt_id import ShortId
id = ShortId().id(10)
print(id)
# wiwdhx8V7x
```

### Thanks
