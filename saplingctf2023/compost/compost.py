checkStr = "hglhhlbomrrw_nebedrcllpue"
# checkStr = "bbd"
def unrotate(c,n):
	c = ord(c)
	return chr((c - 32 - n) % (127 - 32) + 32)

def rotate(c,n):
	c = ord(c)
	return chr((c - 32 + n) % (127 - 32) + 32)

def decode(s, param2, level=0):
	if len(s) <= 0:
		return ""
	mid = len(s) // 2
	# print(s[0] + "|" + s[1:mid] + "|" + s[mid:])
	first = s[0] if param2 == 0 else unrotate(s[0], level)
	# first = s[0]
	if len(s) == 1:
		return first

	left = decode(s[1:mid + 1], param2 == 0, level = level + 1)
	right = decode(s[mid + 1:], param2 == 0, level = level + 1)
	return left + first + right


def encode(s, param2, level=0):
	if len(s) <= 0:
		return ""
	mid = len(s) // 2
	left = encode(s[:mid], param2 == 0, level=level + 1)
	right = encode(s[mid + 1:], param2 == 0, level=level + 1)
	insert = s[mid] if param2 == 0 else rotate(s[mid], level)
	# insert = s[mid]
	# print(insert + "|" + left + "|" + right)
	return  insert + left + right

# print(encode(checkStr,0))

deq = decode(checkStr, 0)
print(deq)
enq =  encode(deq,0)
print(checkStr == enq)
print(enq)

