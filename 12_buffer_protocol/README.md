# 缓冲区协议
- bytes, bytearray, array.array, memoryview.

## memoryview
class memoryview(object)
- object必须支持缓冲区协议, bytes, bytearray.

### 概念
- 元素, bytes, bytearray,一个元素是一个字节, 其他类型: array.array有更大的元素.

切片及索引访问