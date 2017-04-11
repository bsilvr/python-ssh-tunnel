import subprocess


class SshTunnel:

    def __init__(self, remote_host, remote_port, local_host, local_port, username, private_key_path):
        self.__remote_host = remote_host
        self.__remote_port = remote_port
        self.__local_host = local_host
        self.__local_port = local_port
        self.__username = username
        self.__private_key = private_key_path

        self.__connection = ["ssh", "-oStrictHostKeyChecking=no", "-i", self.__private_key, "-N", "-R",
                             str(self.__remote_port) + ":" + self.__local_host + ":" + str(self.__local_port),
                             self.__username + "@" + self.__remote_host]
        self.__process = None

    def start(self):
        self.__process = subprocess.Popen(self.__connection)

    def stop(self):
        self.__process.terminate()
