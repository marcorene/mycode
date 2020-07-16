work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], 
            "10.2.0.1":["interface eth1/1", "shutdown"], 
            "10.3.0.1":["interface eth1/5", "no shutdown"]} 
work2do.update({"10.22.22.22":["interface eth1/9", "reboot"]})
#print(work2do["10.22.22.22"][1])
#x = work2do["10.22.22.22"][1]
#print(x)
#x = "NO REEBOOT"
work2do["10.22.22.22"][1] = "NO REBOOT"
for coffeetime in work2do.keys():
    print('Handshaking. .. ... connecting with ' + coffeetime )
    for mycmds in work2do[coffeetime]:
        print('Attempting to sending command --> ' + mycmds )