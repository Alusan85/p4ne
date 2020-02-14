import random
import ipaddress


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (int(random.randint(0x0B000000, 0xDF000000)),
                                              random.randint(8, 24)), strict=False)

    def regular(self):
        if not self.is_multicast and not self.is_private:
            return True
        else:
            return False

    def key_value(self):
        return int(self.network_address) + int(self.netmask)


networks = []

for x in range(0, 6):
    ip1 = IPv4RandomNetwork()
    if ip1.regular():
        networks.append(ip1)

print(networks)

for x in sorted(networks, key=IPv4RandomNetwork.key_value()):
    print(x)