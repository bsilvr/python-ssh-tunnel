import time
from ssh_tunnel import SshTunnel

tunnel = SshTunnel("server.local", 9001, "localhost", 8123, "gateway", "/home/pi/.ssh/id_rsa")

tunnel.start()

time.sleep(60)

tunnel.stop()
