
from enum import Enum
RETURN_COMMAND_TEST = "OK+0022093303"
MANDATORY_FIELD = "ES+"
READ_FIELD = "R"
WRITE_FIELD = "W"
DEVICE_ADDRESS = hex('0x22')
#REGISTER_VALUE = hex('0022093303')  reg value is coded only in [WWWW] part which is only in write words


class BCN(Enum):
    ENABLED = 0
    DISABLED = 1

class CHO(Enum):
    ENABLED = 0
    DISABLED = 1

class UartBaud(Enum):
    _9600 = 0
    RESERVED = 1
    _19200 = 2
    _115200 = 3

config = {
    "color": 1,
       "width": 1,
       "height": 3,
       "font":1,
   }

for items in config
    asd = ""
    asd.append(confg[items])
parse_write_comand = MANDATORY_FIELD + WRITE_FIELD + DEVICE_ADDRESS + REGISTER_VALUE