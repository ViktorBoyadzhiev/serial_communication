import binascii


class CommandParser2:
    """Parser class for second task."""
    DEFAULT_MAP = 0b0000000111111111
    response_OK = "OK"
    response_NOK = "NOK"

    def parse_request(self, request_type: str, register_value: str = DEFAULT_MAP, device_address: str = "22"):
        """Forms the request for write or read"""
        default_command = "ES+"
        if request_type == "W":
            command_string = default_command + device_address + "F2" + register_value + " "
            crc = binascii.crc32(command_string.encode('utf8'))
            command_string += crc
            return command_string
        if request_type == "R":
            command_string = default_command + device_address + "F2" + " "
            crc = binascii.crc32(command_string.encode('utf8'))
            command_string += crc
            return command_string

    def validate_response(self, command: str,  str_msg: str):
        """Validates the response to the request, prints a message about the mode and returns OK/NOK"""
        if "ERR" in str_msg:
            print("Invalid input data")
            return self.response_NOK
        if "ERR" not in str_msg:
            print("Input data is valid")
            return self.response_OK
