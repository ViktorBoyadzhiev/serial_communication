from serial import Serial, SerialException, serialutil
#import command_parser
debug = True


class SerialCommunication:
    BAUDRATE: int = 19200
    PORT: str = 'COM5'
    timeout = 2.0

    def __init__(self):
        self.serial = Serial(port=self.PORT, baudrate=self.BAUDRATE, timeout=self.timeout)

    def serial_open(self) -> None:
        try:
            self.serial.open()
        except SerialException:
            self.serial_close()
            self.serial_open()

    def serial_close(self) -> None:
        self.serial.close()

    def serial_write(self, input_message: str) -> None:
        byte_converted_message = bytes(input_message, encoding="utf-8")
        self.serial.write(byte_converted_message)
        self.serial.write
        if debug:
            print(f"Input string {input_message}")
            print(f"Converted byte message : {byte_converted_message}")

    def serial_read(self) -> bytes:
        self.serial.read_until(expected=serialutil.CR)  
        #return bin(command_parser.RETURN_COMMAND_TEST, encoding="utf-8")
