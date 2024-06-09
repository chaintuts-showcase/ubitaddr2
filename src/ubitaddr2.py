# This file contains code for generating a Bitcoin address/private key on
# an Adafruit M4 microcontroller
#
# Author: Josh McIntyre
#

# Imports will be handled on a per-function basis due to memory concerns

# A class for handling the generation and display of
# cryptocurrency addresses and private keys

class uBitAddr2:

    # Class "constants"

    # Supported output types
    OUTPUT_DISPLAY = 0
    OUTPUT_DISPLAY_SERIAL = 1
    OUTPUT_SERIAL = 2

    DISPLAY_INTERVAL = 60

    # Supported currencies
    # BTC and BCH are the default
    BTCBCH = 0

    PRIVKEY_FORMAT_WIF = "(WIF)"

    # Initialize the object with a desired output and entropy source
    def __init__(self, output=OUTPUT_DISPLAY, currency=BTCBCH):

        self.output = output
        self.currency = currency
        self.privkey_format = self.PRIVKEY_FORMAT_WIF

    # Wrapper that calls the right function depending on the output
    def generate_and_output(self):

        address, privkey = self.get_address_privkey()

        try:
            if self.output == self.OUTPUT_DISPLAY:
                self.display_screen(address, privkey)
            if self.output == self.OUTPUT_DISPLAY_SERIAL:
                self.display_serial(address, privkey)
                self.display_screen(address, privkey)
            else:
                # If another option isn't available, print to serial
                self.display_serial(address, privkey)
        except Exception as e:
            print(e)
            print("Unable to output address and privkey")

    def get_address_privkey(self):

        import bitaddrlib

        bitaddr = bitaddrlib.BitAddr()
        addr_key = bitaddr.generate_address_privkey_btc()

        return addr_key

    # Prepare the data for display on the character screen
    def prep_data(self, data, colmax):

        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        prepped_data = ""
        for i in range(0, len(data)):
            if i != 0 and i % colmax == 0:
                prepped_data = prepped_data + "\n"

            if data[i] in alphabet:
                prepped_data = prepped_data + data[i]

        return prepped_data

    # Display via serial to PC
    def display_serial(self, address, privkey):
        print("Address: " + address)
        print("Private Key " + self.privkey_format + ": " + privkey)

    # Display the address or private key on a character LCD
    def display_screen(self, address, privkey):

        import busio
        import board
        import time
        import adafruit_character_lcd.character_lcd_i2c as character_lcd

        # Initialize the board
        i2c = busio.I2C(board.SCL, board.SDA)
        cols = 20
        rows = 4
        lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)
        lcd.backlight = True

        # Prep the address and display, wait N seconds,
        # then display the private key
        while True:
            lcd.clear()
            address = self.prep_data(address, cols)
            lcd.message = "Address:\n" + address

            time.sleep(self.DISPLAY_INTERVAL)

            lcd.clear()
            privkey = self.prep_data(privkey, cols)
            lcd.message = "Private Key " + self.privkey_format + ": \n" + privkey

            time.sleep(self.DISPLAY_INTERVAL)

if __name__ == "__main__":
    uba2 = uBitAddr2(output=uBitAddr2.OUTPUT_DISPLAY_SERIAL, currency=uBitAddr2.BTCBCH)
    uba2.generate_and_output()







