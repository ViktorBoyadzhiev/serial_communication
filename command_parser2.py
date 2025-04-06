
def str2int(word):
    int_val = int(word, 16)
    return int_val


def main():   
    DEFAULT_MAP = "01FF"
    cur_SCW = ""
    prev_SCW = DEFAULT_MAP
    device_addr_x8 = ""
    CRC32 = ""
    command_error = False
    command = ""
    output = ""
    input_msg = ""

    while (input_msg != "Close"):
        input_msg = input("Enter command:")
        msg = bytes(input_msg, encoding="utf-8")
        
        #WRITE MSG: ES+R22F2 2AE33143
        #READ MSG: ES+W22F201FF 852DF0FE

        str_msg = msg.decode(encoding="utf-8")

        while (True):
            if "ES+" not in str_msg or str_msg[2] != "+" or str_msg[6:8] != "F2" or ' ' not in str_msg:
                CRC32 = str_msg[len(str_msg)-8:]
                command_error = True
                output = "ERR"
                break 
            split_msg = str_msg.split("+")
            command = split_msg[1][0]
            device_addr_x8 = split_msg[1][1:3]  #device addr always on these bits in W/R

            if command == "R":
                CRC32 = split_msg[1][6:]  #when in READ
                output = "OK+" + str(prev_SCW) + ' ' + CRC32
                break
            elif command == "W":
                CRC32 = split_msg[1][10:]   #when in WRITE
                cur_SCW = split_msg[1][5:9]   #input map only in write command 
                if str2int(cur_SCW[3:]) < 0x0A or str2int(cur_SCW[3]) > 0x1 or str2int(cur_SCW[4]) > 0x1:
                    cur_SCW = prev_SCW

                # print("prev_SCW" + str(prev_SCW))
                # print("cur_SCW" + cur_SCW)

                output = "OK+" + cur_SCW + ' ' + CRC32
            break    

        if not command_error and command == "W":
            prev_SCW = cur_SCW

        command_error = False

        print(command)       
        print(output)


        #return output
    

if __name__ == "__main__":
    main()
