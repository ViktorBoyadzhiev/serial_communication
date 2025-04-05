
def str2bin(word):
    hex_map = "0x" + word
    int_map = int(hex_map, 16)
    bin_map = bin(int_map)
    return bin_map

def bin2hex(word):
    int_map = int(word, 2)
    hex_num = hex(int_map)
    return hex_num[2:].upper()

def main():   

    DEFAULT_MAP = 0b0000001100000011
    cur_SCW = ""
    prev_SCW = DEFAULT_MAP
    device_addr_x8 = ""
    CRC32 = ""
    command_error = False
    command = ""
    case = ""
    RR = "03"   #from default of RF mode if this is the way it is generated
    BB = 0  #Reset counter - by reset, power down or bootloader
    output = ""

    msg = bytes("ES+R2200 BD888E1F", encoding="utf-8")
    
    #WRITE MSG: ES+W22003323 589B0F83
    #READ MSG: ES+R2200 BD888E1F
    #OK+0022093303

    str_msg = msg.decode(encoding="utf-8")

    while (True):
        if "ES+" not in str_msg or str_msg[2] != "+" or str_msg[6:8] != "00" or ' ' not in str_msg:
            CRC32 = str_msg[len(str_msg)-8:]
            command_error = True
            output = "ERR+VAL " + CRC32
            break 
        split_msg = str_msg.split("+")
        command = split_msg[1][0]
        device_addr_x8 = split_msg[1][1:3]  #device addr always on these bits in W/R

        if command == "R":
            CRC32 = split_msg[1][6:]  #when in READ
            output = "OK+" + RR + device_addr_x8 + str(BB) + str(prev_SCW) + ' ' + CRC32
        elif command == "W":
            CRC32 = split_msg[1][10:]   #when in WRITE
            cur_SCW = split_msg[1][5:9]   #input map only in write command
            cur_SCW_bin = str2bin(cur_SCW)
            prev_SCW_bin = str2bin(str(prev_SCW))   
            if cur_SCW_bin[-12] == "1":
                BB += 1
            if cur_SCW_bin[-12] == "1" and prev_SCW_bin[-12] == "0" and cur_SCW_bin[-5] == "1" and prev_SCW_bin[-5] == "0":
                case = "2"
            elif cur_SCW_bin[-12] == "1" and prev_SCW_bin[-12] == "0" and cur_SCW_bin[-5] == "0" and prev_SCW_bin[-5] == "1":
                case = "3"
            else:
                case = "1"
            if cur_SCW_bin[-12] == "0" and cur_SCW_bin[-6] == "0" and prev_SCW_bin[-6] == "1":
                case = "4"

        match case:
            case "1":
                output = "OK+" + cur_SCW + ' ' + CRC32
            case "2":
                output = "OK+C3C " + CRC32
            case "3":
                output = "OK+8787 " + CRC32
            case "4":
                output = "+ESTTC " + CRC32
        break    

    if not command_error:
        prev_SCW = cur_SCW
            
    return output
    

if __name__ == "__main__":
    main()
