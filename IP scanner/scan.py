import os

def check_ping(ip, start, end):
    with open("result.txt", "a") as f:
        for hostname in range(start, end):
            response = os.system(f"ping -n 1 {ip}.{hostname}")
            # and then check the response...
            if response == 0:
                f.write(f"{ip}.{hostname}\n")
            else:
                continue

ip = str(input("First 3 part of IP:"))
start = int(input("START:"))
end = int(input("END:"))
check_ping(ip, start, end)
