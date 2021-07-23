import psutil
import cpuinfo
import asyncio

async def hardwareInfo():
    print("-" * 20 + " Hardware Info " + "-" * 20)
    print(f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}")
    print(f"Cores: {psutil.cpu_count(logical = False)}")
    print(f"Usage: {psutil.cpu_percent()} %")
    print(f'RAM: {str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"}')

asyncio.get_event_loop().run_until_complete(hardwareInfo())