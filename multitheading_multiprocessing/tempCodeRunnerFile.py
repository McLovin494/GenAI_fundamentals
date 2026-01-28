import asyncio


async def brewchai():
    print("Brewing chai")
    await asyncio.sleep(2)
    print("chai ready")


asyncio.run(brewchai())
