from wakeonlan import send_magic_packet

def send_packet(macaddress):
    send_magic_packet(macaddress)
    print("WOL magic packet sent to device : {}".format(macaddress))
    return "Magic packet sent"