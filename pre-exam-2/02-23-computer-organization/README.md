## Clarification alias vs copu

```python
# primitive datatypes are immutable
# a = b create a real copy of the value in a
# Changing one does not change the other.

amount = 5

amount2 = amount

print(amount, amount2) # prints [5, 5]

amount = 6

print(amount, amount2) # prints [6, 5]

# complex datatypes are (sometimes) mutable
# a = b creates an "alias". Both point to the same data.
# Changing on changes the other.

numbers = [1, 2, 3]
numbers2 = numbers

print(numbers, numbers2) # prints [1, 2, 3] [1, 2, 3]

numbers.append(4)

print(numbers, numbers2) # prints [1, 2, 3, 4] [1, 2, 3, 4]

# showing the ids proves the point
print(id(amount), id(amount2)) # different ids - independent locations in memory
print(id(numbers), id(numbers2)) # same id - both variables point to the same data in memory
```

## How does a computer understand code?

Original Python Code:

```python
for i in range(3):
  print(i)
```

This is source code and thus plain, human-readable text.
A computer doesn't understand it (yet).

### Compiler: Source Code > Assembly

Assembly code is specific to the CPU architecture of a computer. Depending on the hardware capabilities and brand of your CPU a specific `architecture` is used such as x86 or ARM64-AArch64 (Apple Silicon).

Here is the produced assembly code for modern MacOS systems

```assembly
        // i in x19 (callee-saved register)
        mov     x19, #0          // i = 0

.Lloop:
        cmp     x19, #3          // compare i with 3
        b.ge    .Ldone           // if i >= 3, exit loop

        // call print_int(i)
        mov     x0, x19          // AArch64 calling convention: 1st arg in x0
        bl      print_int        // branch-with-link (call)

        add     x19, x19, #1     // i = i + 1
        b       .Lloop           // repeat

.Ldone:
        ret
```

In most assembly:

- Every instruction takes 32 bits (4 Bytes).
- Data might have variable length.

### Assembler: Assembly > Machine code

The first line

```
mov x19, #0

or more formally:
MOVZ X19, #0, LSL #0
```

Translates to:

```
11010010100000000000000000010011
```

This is an instruction and clearly segmented:

```
|31|30|29 28 27|26 25|24 23|22 21|20........5|4....0|
|sf| 1  0  1  0| 1  0|  hw  |      imm16     |  Rd   |
```

- Bits `31–29`: sf + opcode prefix

  `1` - 64 bit registers

- Bits `30–23`: `10100100`

  This identifies:
  - Move Wide class
  - MOVZ variant

  Specifically:
  - opc = 10 → MOVZ
  - fixed pattern = 101001

- Bits `22–21`: `00`

  Meaning:
  - No left shift
  - LSL #0
  - Immediate placed in lowest 16 bits

- Bits `20–5`: `0000000000000000`

  16-bit immediate value with the value `0`

- Bits `4–0`: `10011`

  Rd = 19 (Destination Register)

### Interpreted Language

Unlike C or C++, Python source code (.py) is not compiled straight into native machine instructions. Instead:

1. source code (.py)
2. compiled to bytecode (.pyc)
3. executed by Python Virtual Machine (PVM)

### Interpreted vs compiled

- Interpreted Languages are plattform independend (+)
- Compiled Code (Binaries) are optimized for hardware and thus run faster (+), more energy efficient or can use more hardware components (GPU)
- Compiled Code only runs on the CPU architecture it was compiled in
