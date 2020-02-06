from csv import reader as CSVReader

def ReadHexDump(fileName='hex-dump.txt'):
	with open(fileName, 'r') as file:
		contents = file.read()
		frames = contents.split('\n')

		while '' in frames:
			frames.remove('')

		return frames

def HexToDec(a):	
    return [int(i,16) for i in a]

def ParseFrame(frame):
	destMac, sourceMac = frame[:6], frame[6:12] #HexToDec(frame[:6]), HexToDec(frame[6:12])
	etherVer, ipVer = HexToDec(frame[12:14]), int(frame[14][0])
	fragmentID, fragmentField = HexToDec(frame[18:20]), HexToDec(frame[20:22])
	
	ttl = frame[22]
	protocol = int(frame[23],16)
	checksum = HexToDec(frame[24:26])

	differentiatedServices = frame[15]
	NoBytes = frame[14][1]
	lengthIPHeader = HexToDec(frame[16:18])

	sourceIP, destIP = HexToDec(frame[26:30]),HexToDec(frame[30:34])
	sourcePort, destPort = int(''.join(frame[34:36]),16), int(''.join(frame[36:38]),16)


	FrameFields = {
		'destMac': destMac,
		'sourceMac': sourceMac,
		'etherVer': etherVer,
		'ipVer': ipVer,
		'fragmentID': fragmentField,
		'ttl': ttl,
		'protocol': protocol,
		'checksum': checksum,
		'differentiatedServices': differentiatedServices,
		'NoBytes': NoBytes,
		'lengthIPHeader': lengthIPHeader,
		'sourceIP': sourceIP, 'sourcePort': sourcePort,
		'destIP': destIP, 'destPort': destPort
	}

	return [sourceIP, sourcePort, destIP, destPort, ipVer, etherVer], FrameFields

def CompareIP(a,b):
	a = a.split('.')

	if(a[0]=='Any'): 		return True

	for i in range(len(a)):
		if(a[i] == '*'):			continue

		if(int(a[i]) == b[i]):	continue

		else:					return False

	return True		

def ComparePort(a,b):
	if(a=='Any'):		return True
	if(int(a)==b):		return True
	
	return False

def ACLSetup():
	ACL_List = []

	with open('ACL.csv',newline = '') as file:
		contents = CSVReader(file, delimiter=' ')
		for row in contents:
			ACL_List.append(row)

		ACL_List = ACL_List[1:]

		for i in range(len(ACL_List)):
			ACL_List[i] = ACL_List[i][0].split(',')

		return ACL_List

def ACLCheck(x, acls):
	for acl in acls:
		srcIP, srcPort = CompareIP(acl[0], x[0]), ComparePort(acl[1], x[1])
		destIP, destPort = CompareIP(acl[2], x[2]), ComparePort(acl[3], x[3])

		if (srcIP and srcPort) and (destIP and destPort):
			return acl[4]

def printFields(FrameFields):
	proto = {1: 'ICMP', 6: 'TCP', 17: 'UDP', }
	print("Dest Mac Addr : ", ":".join([str(i) for i in FrameFields['destMac']]))
	print("Source Mac Addr: ", ":".join([str(i) for i in FrameFields['sourceMac']]))
	# print("etherVer : ", FrameFields['etherVer'])
	print("ip version : ",FrameFields['ipVer'])
	# print("Num bytes in Header : \t",FrameFields['NoBytes'])
	
	print("Protocol : ", proto[int(FrameFields['protocol'])])
	print("Source IP : ", ".".join([str(i) for i in FrameFields['sourceIP']]))
	print("Destination IP :", ".".join([str(i) for i in FrameFields['destIP']]))
	print("Source Port :", FrameFields['sourcePort'])
	print("Destination Port :", FrameFields['destPort'])

def main():
	acls = ACLSetup()

	frames  =  ReadHexDump()

	i = 0
	for frame in frames:
		frame  =  frame.split(' ')
		x, FrameFields  =  ParseFrame(frame)

		print('------------------------------------------------------------------------------------------------------')
		if x[5][1] != 0:
			print('Firewall: Not an ip packet')
		else:
			printFields(FrameFields)
			print('\nFirewall: ', ACLCheck(x, acls))
		i += 1 									#[sourceIP, sourcePort, destIP, destPort, ipVer, etherVer]
		print('------------------------------------------------------------------------------------------------------\n\n\n')
if __name__  ==  '__main__':
	main()