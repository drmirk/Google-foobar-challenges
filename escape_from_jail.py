def answer(digest):
    # your code here
    message = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,16):
        x, decoded = 0, .1
        while decoded != int(decoded):
            decoded = ((256 * x + digest[i]) ^ message[i-1])/129.0
            x += 1
        message[i] = int(decoded)
    return message

print answer([0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129])
print answer([0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165])


