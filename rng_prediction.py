f = open("rng_predictions.txt", "w")

rng1 = 0xD2
rng2 = 0x5B
rng3 = 0xFF
rng4 = 0x48
rng5 = 0xB6
rng6 = 0x27
rng7 = 0x4B
rng8 = 0x05

for rng_rolls in range(32768):
    f.write(str(rng_rolls) + " - ")
    if ((rng1 ^ rng2) & 2):
        cur_carry = 0x80
    else:
        cur_carry = 0
    next_carry = (rng1 & 1) << 7
    rng1 = ((rng1 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    next_carry = (rng2 & 1) << 7
    rng2 = ((rng2 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    next_carry = (rng3 & 1) << 7
    rng3 = ((rng3 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    next_carry = (rng4 & 1) << 7
    rng4 = ((rng4 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    next_carry = (rng5 & 1) << 7
    rng5 = ((rng5 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    next_carry = (rng6 & 1) << 7
    rng6 = ((rng6 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    next_carry = (rng7 & 1) << 7
    rng7 = ((rng7 >> 1) | cur_carry) & 0xFF
    cur_carry = next_carry
    rng8 = ((rng8 >> 1) | cur_carry) & 0xFF
    f.write(hex(rng1) + " ")
    f.write(hex(rng2) + " ")
    f.write(hex(rng3) + " ")
    f.write(hex(rng4) + " ")
    f.write(hex(rng5) + " ")
    f.write(hex(rng6) + " ")
    f.write(hex(rng7) + " ")
    f.write(hex(rng8) + " - ")
    f.write(str(((rng4 << 8) | rng3) & 0x1FF) + "\n") 

f.close()
