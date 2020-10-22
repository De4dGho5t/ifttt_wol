from wakeonlan import send_magic_packet

def send_packet(macaddress):
    send_magic_packet(macaddress)

    return "WOL magic packet sent to device : {}".format(macaddress)