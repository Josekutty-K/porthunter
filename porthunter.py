import socket
import concurrent.futures

target = input("Enter the target to scan: ")
ip = socket.gethostbyname(target)
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print(r"""
 ________  ________  ________  _________        ___  ___  ___  ___  ________   _________  _______   ________
|\   __  \|\   __  \|\   __  \|\___   ___\     |\  \|\  \|\  \|\  \|\   ___  \|\___   ___\\  ___ \ |\   __  \
\ \  \|\  \ \  \|\  \ \  \|\  \|___ \  \_|     \ \  \\\  \ \  \\\  \ \  \\ \  \|___ \  \_\ \   __/|\ \  \|\  \
 \ \   ____\ \  \\\  \ \   _  _\   \ \  \       \ \   __  \ \  \\\  \ \  \\ \  \   \ \  \ \ \  \_|/_\ \   _  _\
  \ \  \___|\ \  \\\  \ \  \\  \|   \ \  \       \ \  \ \  \ \  \\\  \ \  \\ \  \   \ \  \ \ \  \_|\ \ \  \\  \|
   \ \__\    \ \_______\ \__\\ _\    \ \__\       \ \__\ \__\ \_______\ \__\\ \__\   \ \__\ \ \_______\ \__\\ _\
    \|__|     \|_______|\|__|\|__|    \|__|        \|__|\|__|\|_______|\|__| \|__|    \|__|  \|_______|\|__|\|__|

      created by: https://www.linkedin.com/in/josekutty-kunnelthazhe-binu-9b484429b/


""")

def scan(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))

            if result == 0:
                try:
                   service = socket.getservbyport(port, "tcp")

                except OSError:
                    service ="Unknown Service"
                except Exception as e:
                    service = f"Error: {e}"

                print(f"Port: {port} is open - Service: {service}")
    except Exception as e:
        print(f"Error scanning port: {e}")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan, range(start_port, end_port + 1))
