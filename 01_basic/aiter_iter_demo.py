# using aiter example 1:
import asyncio
async def numbers(nums):
    for i in range(nums):
        yield i
        await asyncio.sleep(0.5)

async def main():
    # 隐式使用
    async for i in numbers(10):
            print(i, end = ' ')
    # 显式使用
    print([i async for i in aiter(numbers(10)) if i % 2 == 0])
    # [0, 2, 4, 6, 8]

a = aiter(numbers(10))
dir(a)

if __name__ == "__main__":
    asyncio.run(main())


# example 2
# https://stackoverflow.com/questions/69984638/how-to-use-asynchronous-iterator-using-aiter-and-anext-builtins
async def get_range():
    for i in range(10):
        print(f"start {i}")
        await asyncio.sleep(1)
        print(f"end {i}")
        yield i

class AIter:
    def __init__(self, N):
        self.i = 0
        self.N = N

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        print(f"start {i}")
        await asyncio.sleep(1)
        print(f"end {i}")
        if i >= self.N:
            raise StopAsyncIteration
        self.i += 1
        return i

async def main():
    async for p in AIter(10):
        print(f"finally {p}")

async def pairwise(aiterable,default = None):
    ait = aiter(aiterable)
    async for x in ait:
        yield x, await next(ait, default) #get an extra value,yield a 2-tuple

    print('\n\nAIter')
    await pairwise(AIter(10))

if __name__ == "__main__":
    asyncio.run(main())

