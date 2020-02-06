from csv import reader as CSVReader
from scapy.all import *
import time

def CompareIP(a,b):
    if(a[0]=='Any'): 		return True

    for i in range(len(a)):
        if(a[i] == '*'):			continue

        if(int(a[i]) == int(b[i])):	continue

        else:					return False

    return True		

def ComparePort(a,b):
	if(a=='Any'):		return True
	if(int(a)==int(b)):		return True
	
	return False

def PacketSend(source, dest, sport, dport, packetCount=100):
    print("Packets from ", "(Src:", source, "port:",sport, ") to (dest:", dest,"port:",dport,")")
    sr(IP(src=source, dst=dest)/TCP(sport=sport,dport=dport), inter=0.5, timeout=5, iface=conf.iface)


def AsyncSnifferStart(source):
    filter = "dst host" + " " + source
    asyncSniff = AsyncSniffer(filter=filter)
    asyncSniff.start()
    
    return asyncSniff

def AsyncSnifferStop(asyncSniff):
    return asyncSniff.stop()

def ACLSetup():
	ACL_List = []

	with open('acl-lab3.csv',newline = '') as file:
		contents = CSVReader(file, delimiter=' ')
		for row in contents:
			ACL_List.append(row)

		ACL_List = ACL_List[1:]

		for i in range(len(ACL_List)):
			ACL_List[i] = ACL_List[i][0].split(',')

		return ACL_List

def ACLCheck(x, acls):
    for acl in acls:
        # print("MYACL : ", acl)
        srcIP, srcPort = CompareIP(acl[0].split('.'), x[0]), ComparePort(acl[1], x[1])        
        destIP, destPort = CompareIP(acl[2].split('.'), x[2]), ComparePort(acl[3], x[3])

        
        if (srcIP and srcPort and destIP and destPort):
            return acl[4]

def Printer(packet):
    print("**********************************************************************")
    print("Src ip: ", packet[0][IP].src)
    print("Dest ip: ", packet[0][IP].dst)

    print("\nSrc Mac: ", packet[0].src)
    print("Dest Mac: ", packet[0].dst)

    print("\nSrc port: ", packet[0].sport)
    print("Dest port: ", packet[0].dport)
    
def main():
    ACLs = ACLSetup()
    # for a in ACLs:
    #     print(a)
    src = "20.20.20.20"
    dest = "100.100.100.100"
    sport = 11
    dport = 80

    sniffer = AsyncSnifferStart(dest)
    PacketSend(src, dest, sport, dport, packetCount=100)

    time.sleep(5)

    CapturedPackets = AsyncSnifferStop(sniffer)
    print("Raw packet: ", raw(CapturedPackets[0]))
    print(CapturedPackets[0].show())
    split = [CapturedPackets[0][IP].src.split('.'), CapturedPackets[0].sport, CapturedPackets[0][IP].dst.split('.'), CapturedPackets[0].dport]
    
    Printer(CapturedPackets)

    print("\n------Firewall: ", ACLCheck(split, ACLs), "------")

    print("**********************************************************************")

if __name__ == '__main__':
    main()