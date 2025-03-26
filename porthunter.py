import socket
import concurrent.futures

target = input("Enter the target to scan: ")
ip = socket.gethostbyname(target)
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print(r"""
 ____   ____   ____   _____    _  _   _  _   _  _   _____  ___   ____  
)  _)\ / __ \ /  _ \ )__ __(  ) () ( ) () ( ) \/ ( )__ __() __( /  _ \ 
| '__/ ))__(( )  ' /   | |    | -- | | \/ | |  \ |   | |  | _)  )  ' / 
)_(    \____/ |_()_\   )_(    )_()_( )____( )_()_(   )_(  )___( |_()_\ 
                                                                       
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
