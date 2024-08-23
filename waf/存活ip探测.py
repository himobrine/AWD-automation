import asyncio
import aiohttp

async def check_ip(ip):
    url = f"http://{ip}"
    try:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=1)) as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    print(ip)
    except:
        pass

async def main():
    tasks = []
    # 构造要扫描的 IP 列表
    ips = [f"10.102.47.{i}" for i in range(2, 255)]
    for ip in ips:
        tasks.append(asyncio.create_task(check_ip(ip)))

    # 等待所有任务完成
    await asyncio.gather(*tasks)

asyncio.run(main())