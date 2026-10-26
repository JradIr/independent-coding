import asyncio
import time
from typing import Callable, Any, List

#This is the asyncratelimiter class
class AsyncRateLimiter:
    def __init__(self, max_concurrent: int, rate_limit_delay: float):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.rate_limit_delay = rate_limit_delay
        self._last_execution_time = 0.0
        self._lock = asyncio.Lock()

    async def _wait_for_rate_limit(self):
        async with self._lock:
            now = time.monotonic()
            elapsed = now - self._last_execution_time
            if elapsed < self.rate_limit_delay:
                await asyncio.sleep(self.rate_limit_delay - elapsed)
            self._last_execution_time = time.monotonic()

    async def run(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        async with self.semaphore:
            await self._wait_for_rate_limit()
            return await func(*args, **kwargs)


async def mock_api_call(request_id: int, payload: str) -> dict:
    print(f"[{time.strftime('%H:%M:%S')}] Starting Request {request_id} ('{payload}')...")
    await asyncio.sleep(0.5)  # Simulate I/O latency
    print(f"[{time.strftime('%H:%M:%S')}] Completed Request {request_id}")
    return {"id": request_id, "status": "success", "payload": payload}


def get_user_inputs() -> tuple[int, float, List[str]]:
    print("=== Async Rate Limiter Tester ===\n")
    
    while True:
        try:
            max_concurrent = int(input("Enter max concurrent tasks (e.g., 2): "))
            if max_concurrent > 0:
                break
            print("Must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            delay = float(input("Enter delay between task starts in seconds (e.g., 0.5): "))
            if delay >= 0:
                break
            print("Delay cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    raw_items = input("Enter payload items separated by commas (or press Enter for defaults): ").strip()
    
    if raw_items:
        items = [item.strip() for item in raw_items.split(",") if item.strip()]
    else:
        items = [f"item_{i}" for i in range(1, 6)]
        print(f"Using default payloads: {items}")

    return max_concurrent, delay, items


async def main():
    max_concurrent, rate_limit_delay, items = get_user_inputs()
    
    limiter = AsyncRateLimiter(max_concurrent=max_concurrent, rate_limit_delay=rate_limit_delay)
    
    print(f"\n--- Running {len(items)} tasks (Max Concurrent: {max_concurrent}, Delay: {rate_limit_delay}s) ---\n")
    start_time = time.time()

    tasks = [
        limiter.run(mock_api_call, request_id=idx, payload=item)
        for idx, item in enumerate(items, start=1)
    ]
    
    results: List[dict] = await asyncio.gather(*tasks)
    total_time = time.time() - start_time

    print("\n--- Execution Summary ---")
    print(f"Processed: {len(results)} items")
    print(f"Total time elapsed: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())