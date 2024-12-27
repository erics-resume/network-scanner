# Network Port Scanner Project
# Use modules like Socket
from socket import *
import time
startTime = time.time()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Prompt hostname (e.g. website)
    # port scanning CAN BE SEEN AS, OR CONSTRUED AS, A CRIME
    # ONLY on localhost or your own website
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    # Check which ports are open using socket
    for i in range(49, 499):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()

    # Check how much time taken to scan port
    print('Time taken:', time.time() - startTime)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
