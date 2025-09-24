#!/usr/bin/env python3
import os, asyncio, aiohttp, time, csv

API_URL = os.getenv("API_URL", "https://postman-echo.com/post")
SESSIONS = int(os.getenv("SESSIONS", 50))
CONCURRENCY = int(os.getenv("CONCURRENCY", 10))
MESSAGES_PER_SESSION = int(os.getenv("MESSAGES_PER_SESSION", 5))
THINK_TIME = float(os.getenv("THINK_TIME", 0.1))
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/content/Day28_LoadTest_PilotPack/results")

os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_payload(session_id, msg_id):
    return {"session": session_id, "message_id": msg_id, "text": "Hello"}

async def send_request(session, payload):
    t0 = time.time()
    try:
        async with session.post(API_URL, json=payload) as resp:
            await resp.text()
            return time.time() - t0, resp.status
    except:
        return time.time() - t0, None

async def run_session(session_id):
    async with aiohttp.ClientSession() as s:
        results = []
        for m in range(MESSAGES_PER_SESSION):
            payload = create_payload(session_id, m)
            elapsed, status = await send_request(s, payload)
            results.append((elapsed, status))
            await asyncio.sleep(THINK_TIME)
        return results

async def main():
    tasks = [run_session(i) for i in range(SESSIONS)]
    all_results = await asyncio.gather(*tasks)
    rows = [(sid, i, r[0], r[1]) for sid, session in enumerate(all_results) for i, r in enumerate(session)]
    csv_file = os.path.join(OUTPUT_DIR, "results.csv")
    with open(csv_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["session_id","msg_id","elapsed_sec","status"])
        w.writerows(rows)
    print("✅ Results saved to", csv_file)

if __name__ == "__main__":
    asyncio.run(main())
