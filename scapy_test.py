from scapy.all import sniff

print("Waiting for Modbus packets (TCP Port 502)...")

def packet_callback(packet):
    print(packet.summary())

sniff(filter="tcp port 502", prn=packet_callback, store=False)