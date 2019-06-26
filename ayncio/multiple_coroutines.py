import asyncio
import time

# In this example two coroutine will run together,
# as soons as coroutine1 execution is suspended by
# the await asyncio.sleep command, coroutine2 continues 
async def coroutine(cid, sleep):
	start = time.perf_counter()
	print('[coroutine-%d] is active on the event loop' % cid)
	print('[coroutine-%d] yielding control. Going to be blocked for %d secs' % (cid, sleep))
	await asyncio.sleep(sleep)
	print('[coroutine-%d] resumed' % cid)
	elapsed = time.perf_counter() - start
	print('[coroutine-%d] completed in %0.2f seconds' % (cid, elapsed))

if __name__ == '__main__':
	start = time.perf_counter()
	print('[main] started')
	loop = asyncio.get_event_loop()
	loop.run_until_complete(asyncio.gather(coroutine(1, 5), coroutine(2, 4)))
	elapsed = time.perf_counter() - start
	print('[main] completed in %0.2f seconds' % elapsed)
	loop.close()