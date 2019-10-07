import asyncio

# This is a coroutine
# Is a function that can suspend its execution before 
# reaching the return or its end, and it can indirectly 
# pass control to another coroutine for some time
async def coroutine():
	print('hello')
	await asyncio.sleep(1)
	print('world')
	return

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(coroutine())
	loop.close()
	# The following syntax can be used in Python 3.7 to do the same
	# asyncio.run(coroutine())