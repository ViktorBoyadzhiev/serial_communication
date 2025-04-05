from communication import SerialCommunication


def main():
    print("Hello world!")
    asd = SerialCommunication()
    # asd.serial_open()
    print(asd)
    asd.serial_write("ES+R2200 BD888E1F")
    out = asd.serial_read()
    print(out)
    asd.serial_close()


if __name__ == "__main__":
    main()
