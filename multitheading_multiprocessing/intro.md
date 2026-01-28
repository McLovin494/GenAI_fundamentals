### Concurrency

- Doing multiple tasks at once, like making tea and chatting
- The switching is actually fast
- the response is returned directly
- threading.Thread
- asyncio

### Parallelism

- Running multiple tasks at once
- if one worker is busy everything gets stuck response is not returned directly
- multiprocessing.Process
- concurrent.features.ProcessPollExecutor
