from task1_command_parser import CommandParser
from communication import SerialCommunication
filename = "data.txt"


def main():
    com = SerialCommunication()
    parser = CommandParser()
    com.serial_open()
    request = parser.parse_request("R")
    response = com.DUT_Read_Write(request)

    # Validate response
    result = parser.validate_response(command="R", str_msg=response)
    if result == "OK":
        with open(filename, 'a') as file:
            file.write(response + "\n")

    com.serial_close()


if __name__ == "__main__":
    main()
