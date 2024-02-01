from netfilterqueue import NetfilterQueue as nfq
from scapy.all import *
def packet_listener(packet):
 scapy_packet = IP(packet.get_payload())
 if scapy_packet.haslayer("UDP") and scapy_packet[UDP].dport == 53:
   scapy_packet[IP].src = "10.10.11.100"  # change src address
   
   #delete checksum and length fields since they will be re-calculated by scapy on send()
   del scapy_packet[IP].chksum
   del scapy_packet[IP].len
   del scapy_packet[UDP].chksum
   del scapy_packet[UDP].len
   
   packet.drop()  # drop the original packet
   
   send(scapy_packet) #send 
 else:  # accept packets that we are not interested in
   packet.accept()

queue = nfq()
queue.bind(1, packet_listener)
queue.run()
