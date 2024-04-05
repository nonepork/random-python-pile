import itertools
import subprocess

def check_ping(ip, *args):
    with open("result.txt", "a") as f:
        if len(args) == 0:
            print(f"[ CHECKING ] {ip}")
            # and then check the response...
            response = subprocess.Popen(f"ping -n 1 {ip}", stdout=subprocess.PIPE)
            response.wait()
            if response.poll() == 0:
                f.write(f"{ip}\n")
        else:
            for combination in itertools.product(*args):
                # combination contains one value from each range
                temp = ip
                for i in combination:
                    temp += "." + str(i)
                temp.rstrip(".")

                # and then check the response...
                print(f"[ CHECKING ] {temp}")
                response = subprocess.Popen(f"ping -n 1 {temp}", stdout=subprocess.PIP)
                response.wait()
                if response.poll() == 0:
                    f.write(f"{temp}\n")
                else:
                    continue


def format_input(input: str):
    unsplit_ip = input.split('.')
    ip = ""
    ranges = []
    for part in unsplit_ip:
        if "-" not in part:
            ip += part + "."
        else:
            ranges.append(range(int(part.split("-")[0]), int(part.split("-")[1])+1)) # I know this looks scary and I'm sorry xD
    ip = ip.rstrip(".")

    return ip, ranges

unsplit_ip = str(input("Enter the IP range you want to scan: "))
ip, ranges = format_input(unsplit_ip)
check_ping(ip, *ranges)
