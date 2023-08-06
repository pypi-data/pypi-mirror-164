# NosoP-Py

Set of classes to read the data from Noso files.

Currently we have:

- NosoBlock: The block file
- NosoFileStream: A small class to mimic the Stream functionality of other languages
- NosoMemStream: A small class to mimic the Stream functionality of other languages

> **Attention**
> Pascal Short Strings my contain memory garbage, between the string length and their capacity.
> Due to that fact I've created the class name `PascalShortString` as an utility class to get around this know issue.

## Instruction for use

### Noso Block

```py
from datetime import datetime
from nosodata_py.block import NosoBlock

block = NosoBlock()
block.load_from_file('48028.blk')

print('Block #:', block.number)
print('Block Hash:', block.hash)
print('Time Start:', datetime.fromtimestamp(block.time_start))
print('Time End:', datetime.fromtimestamp(block.time_end))
print('Time Total:', block.time_total)
print('Time Last 20:', block.time_last_20)
print('Difficulty:', block.time_last_20)
print('Target Hash:', block.target_hash)
print('Solution:', block.solution)
print('Last Block Hash:', block.last_block_hash)
print('Next Block Diff:', block.next_block_diff)
print('Miner:', block.miner)
print('Fee:', block.fee)
print('Reward:', block.reward)

if len(block.orders) > 0:
    print()
    print('    Orders:')
    for order in block.orders:
        print('        ------------------------------------')
        print('        Block #:', order.block)
        print('        Order ID:', order.order_id)
        print('        Transder ID:', order.transfer_id)
        print('        Type:', order.order_type)
        print('        Timestamp:', datetime.fromtimestamp(order.timestamp))
        print('        Reference:', order.reference)
        print('        Sender:', order.sender)
        print('        Address:', order.address)
        print('        Receiver:', order.receiver)
        print('        Fee:', order.fee)
        print('        Amount:', order.amount)
        print('        Signature:', order.signature)

if len(block.pos_list) > 0:
    print()
    print('    PoS:', block.pos_reward)
    for address in block.pos_list:
        print('        Address:', address)

if len(block.mns_list) > 0:
    print()
    print('    MNs:', block.mns_reward)
    for address in block.mns_list:
        print('        Address:', address)
```

