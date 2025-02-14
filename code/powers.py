def deal(target, damage, times=1):
    target.hp -= damage * times

def gain(target, amount, stat):
    if stat == 'block':
        target.block += amount
    elif stat == 'strength':
        target.strength += amount

def apply(target, amount, stat):
    if stat == 'vulnerable':
        target.vulnerable = amount
    elif stat == 'weak':
        target.weak = amount