import sys
def check_endianness():
	if sys.byteorder == "little":
		print("little-endian")
	else:
		print("big-endian")
if __name__ == "__main__":
	check_endianness()
