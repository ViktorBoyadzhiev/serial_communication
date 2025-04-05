class MyCustomError(Exception):
    """Exception raised for custom error in the application."""

    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"
    

def str2bin(word):
    hex_map = "0x" + word
    int_map = int(hex_map, 16)
    bin_map = bin(int_map)
    return bin_map


def main():   

    DEFAULT_MAP = 0b0000001100000011
    input_map_x16 = ""
    device_addr_x8 = ""
    CRC32 = ""
    COMMAND_ERROR = False
    command = ""
    SCW = str(hex(int(DEFAULT_MAP))[2:])

    msg = bytes("ES+W22003323 589B0F83", encoding="utf-8")
    
    #WRITE MSG: ES+W22003323 589B0F83
    #READ MSG: ES+R2200 BD888E1F
    #OK+0022093303

    #print(msg)

    #TODO: use [B], 00, split_msg[0] and memory map inconsistencies to check for incorrect msg

    str_msg = msg.decode(encoding="utf-8")
    #print(type(str_msg))
    if "ES+" not in str_msg:
        raise MyCustomError("Serious syntax error in input command!")

    split_msg = str_msg.split("+")
    command = split_msg[1][0]
    device_addr_x8 = split_msg[1][1:3]  #device addr always on these bits in W/R

    if command == "R":
        CRC32 = split_msg[1][6:]  #when in READ
    elif command == "W":
        CRC32 = split_msg[1][10:]   #when in WRITE
        input_map_x16 = split_msg[1][5:9]   #input map only in write command
        bin_map = str2bin(input_map_x16)
        SCW = DEFAULT_MAP
        SCW[-5:-14:-1] = bin_map[-5:-14:-1]
    print(bin_map)


    #print(SCW.zfill(4))

    # #print(bin_map[-1:-4:-1])


    # 

    # #print(CRC32)

    # #print(len("0b0011001100100011")) # can use bin map lenght to check for 14,15 bit values. if len< 14 they are 0. 15 should always be 0


if __name__ == "__main__":
    main()
