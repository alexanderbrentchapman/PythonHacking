"""
	TODO:
	@alexander:finish tx_speed
"""
#########################################
# this program is only for linux so far #
#########################################
def get_txcurrent(iface):
    # creating object with path of tx speed using the given interface
    speed_file = "/sys/class/net/" + iface + "/statistics/tx_bytes"
    file = open(speed_file)  # opening the file
    speed = file.read()  # reading file
    file.close()  # closing file
    return int(speed)  # returning speed as an integer


# getting interface name from the user
iface_name = input("Interface Name: ")

while True:
    tx_past = 0
    tx_current = get_txcurrent(iface_name)
    print(tx_current)
    print(tx_past)
    if tx_past > tx_current:
        tx_speed = tx_past - tx_current
        print(tx_speed)
        tx_past = tx_current
        tx_current = get_txcurrent(iface_name)

    if tx_current > tx_past:
        tx_speed = tx_current - tx_past
        print(tx_speed)
        tx_past = tx_current
        tx_current = get_txcurrent(iface_name)
