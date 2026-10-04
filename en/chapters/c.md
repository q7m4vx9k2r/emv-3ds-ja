---
layout: default
title: "Generate ECC Key Pair"
lang: en
---

# Generate ECC Key Pair

[Home](../../index.md)

<a id="page-394"></a>

## PDF page 394

## Annex C

## Generate ECC Key Pair

A number of available cryptographic libraries include ECC key pair generation as a function. If not available, it is recommended to use a method of ECC key pair generation following [ISO/IEC 15946-1]. In this method, a random number is obtained and tested to determine that it will produce a value of d (the private key) in the correct range (1 < d < n). If d is out-of-range, another random number is obtained (for example, the process is iterated until an acceptable value of d is obtained). Note: The integers used in this function are large (32 or 66 bytes), which may mean they would be represented as strings of bytes (as in most cryptographic libraries) rather than built-in integers in an implementation. The following process or its equivalent may be used to generate an ECC key pair.

### C.1

### Input

Curve parameters (p, a, b, G, n, h):

### C.2

### Output

- status—Status returned from the key pair generation procedure. The status will indicate SUCCESS or an ERROR.

- (d, Q)—Generated private and public key

o d, the generated private key, is an integer in the range [1, n–1]

o Q, the generated public key, is the point on the specified curve

If an error is encountered during the generation process, no values for d and Q should be returned

C.2.1 Process

1. N:= len(n), the bit-length of n

2. d:= StringToInteger(Random(N))

3. If (d > n – 2), then go to step 2

4. d:= d + 1

5. Q:= PointMultiply(d, G, CurveID)

6. If successful, return SUCCESS, d, and Q

Else, return ERROR status.

---

<a id="page-395"></a>

## PDF page 395

Auxiliary functions used:

- StringToInteger(s) converts a string s of bits to a non-negative integer

- Random(c) generates a string of c bits, where c is a positive integer

- PointMultiply() performs scalar multiplication