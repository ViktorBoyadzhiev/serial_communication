from serial import Serial, SerialException, serialutil
debug = False


class SerialCommunication:
    """Class for serial communication with commands"""

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
        """Data to be written to device prepared in correct format"""
        byte_converted_message = bytes(input_message, encoding="utf-8")
        self.serial.write(byte_converted_message)
        if debug:
            print(f"Input string {input_message}")
            print(f"Converted byte message : {byte_converted_message}")

    def serial_read(self) -> bytes:
        """Read response from the device decoded"""
        read_value = self.serial.read_until(expected=serialutil.CR)
        return bin(read_value, encoding="utf-8")

    def DUT_Read_Write(self, request: str) -> str:
        """Sends the request to the device and reads its response"""
        self.serial_write(request)
        data = self.serial_read()
        return data
