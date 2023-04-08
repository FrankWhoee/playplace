checkStr = "hglhhlbomrrw_nebedrcllpue"

def unrotate(c,n):
	c = ord(c)
	return chr((c - 32 - n) % (127 - 32) + 32)

def rotate(c,n):
	c = ord(c)
	return chr((c - 32 + n) % (127 - 32) + 32)

def decode(s, level=0):
	if len(s) <= 0:
		return ""
	mid = len(s) // 2
	return decode(s[:mid], level=level + 1) + unrotate(s[mid],level) + decode(s[mid + 1:], level=level + 1)

print(decode(checkStr))
