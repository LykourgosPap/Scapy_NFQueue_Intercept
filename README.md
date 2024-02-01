# Scapy_NFQueue_Intercept

Useful script for intercepting output traffic with nfqueue filter, modify it with scapy and send it, while also drop the original packet.

## Requirements
We have three dependencies 
- scapy
- Netfilter queues
- NetFilter queues library

```bash
pip3 install scapy
pip3 install NetfilterQueue
sudo apt install libnetfilter-queue-dev
```

After installing the required dependencies, the following rule needs to be added to forward the traffic to netfilter queue:

```bash
iptables -D OUTPUT -p udp -d 172.31.105.98 -j NFQUEUE --queue-num 1 #queue-num needs to match the script, destination address etc can be modified as needed
```

