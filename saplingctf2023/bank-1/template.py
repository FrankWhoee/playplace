from pwn import * # requires pwntools

# context.log_level = "debug"
r = remote("bank-1.ctf.maplebacon.org", 1337)
r.recvuntil(">")

def request_money(id):
    r.sendline(b"2")
    r.recvuntil(b":")
    r.sendline(str(id).encode())
    r.recvuntil(b"Your receipt: ")
    ctxt = r.recvline()
    r.recvuntil(b">")
    return ctxt

def send_money(sender_id, recipient_id, sender_pin, amount):
    r.sendline(b"1")
    r.recvuntil(b":")
    r.sendline(str(sender_id).encode())
    r.recvuntil(b":")
    r.sendline(str(recipient_id).encode())
    r.recvuntil(b":")
    r.sendline(str(sender_pin).encode())
    r.recvuntil(b":")
    r.sendline(str(amount).encode())
    r.recvuntil(b"Your receipt: ")
    ctxt = r.recvline()
    r.recvuntil(b">")
    return ctxt

def blockify(msg):
    blocks = []
    for i in range(0,len(msg),16):
        blocks.append(msg[i:i+16])
    return blocks

req_msg = "1234567812345678123456789123"
guess_msg = "78123456789123"
answer = ""
t0 = time.time()
tf = time.time()
for i in range(6):
    req_out = request_money(int(req_msg))
    req_blocks = blockify(req_out)
    reqpin = req_blocks[2] + req_blocks[3]
    for i in range(10):
        guess_out = send_money(0, 1234567812345, int(guess_msg), int(answer + str(i)))
        guess_blocks = blockify(guess_out)
        guesspin = guess_blocks[2] + guess_blocks[3]
        if reqpin == guesspin:
            print(i)
            answer += str(i)
            break
    req_msg = req_msg[:-1]
    guess_msg = guess_msg[:-1]

send_money(0,1,int(answer),100000)
r.sendline(b"3")
print(r.recvuntil(b">"))

