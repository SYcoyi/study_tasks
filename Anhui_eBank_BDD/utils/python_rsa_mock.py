# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
import math

import time

import rsa

ZERO_ARRAY = None
RSA_EXPONENT = '10001'
RSA_MODULUS = 'ac8e5f9bea40d0c06b76b04595e8457679251d590f5f3f442b0802b2055ea63b72c7c3b502c05856154bba1fdfaa3fa50478273187882ccc4f02c3b192a1455a6572d0d68b5ce132e765449b1b2edcd3a9cf8cc66ea838ff7dc74bc5e8b8ef37b37914227de536b4ace62e537c41ef0ce6ce4194e9c4ef472dd61ce2fb5cdaf5'
biRadixBase = 2
biRadixBits = 16
bitsPerDigit = biRadixBits
biRadix = 1 << 16
biHalfRadix = biRadix >> 1
biRadixSquared = biRadix * biRadix
maxDigitVal = biRadix - 1
maxInteger = 9999999999999998

highBitMasks = [
    0x0000,
    0x8000,
    0xc000,
    0xe000,
    0xf000,
    0xf800,
    0xfc00,
    0xfe00,
    0xff00,
    0xff80,
    0xffc0,
    0xffe0,
    0xfff0,
    0xfff8,
    0xfffc,
    0xfffe,
    0xffff
]


def setMaxDigits(value):
    maxDigits = value
    global ZERO_ARRAY
    ZERO_ARRAY = [0] * value
    iza = 0
    global bigZero
    bigZero = BigInt()
    global bigOne
    bigOne = BigInt()
    bigOne.digits[0] = 1


def cnumber(flag):
    if flag:
        return 1
    else:
        return 0


class BigInt():
    def __init__(self, flag=None):
        self.flag = flag
        if flag:
            self.digits = []
        else:
            self.digits = list(ZERO_ARRAY)
        self.isNeg = False


def charToHex(c):
    ZERO = 48
    NINE = ZERO + 9
    littleA = 97
    littleZ = littleA + 25
    bigA = 65
    bigZ = 65 + 25
    result = 0

    if (c >= ZERO and c <= NINE):
        result = c - ZERO
    elif (c >= bigA and c <= bigZ):
        result = 10 + c - bigA
    elif (c >= littleA and c <= littleZ):
        result = 10 + c - littleA
    else:
        result = 0

    return result


def hexToDigit(s):
    result = 0
    sl = min([len(s), 4])
    for i in range(0, sl):
        result <<= 4
        result |= charToHex(ord(s[i]))

    return result


def biFromHex(s):
    result = BigInt()
    sl = len(s)
    i = sl
    j = 0
    while (i > 0):
        result.digits[j] = hexToDigit(s[max([i - 4, 0]):max([i - 4, 0]) + min([i, 4])])
        j += 1
        i -= 4
    return result


def biHighIndex(x):
    result = len(x.digits) - 1
    while (result > 0 and x.digits[result] == 0):
        result -= 1
    return result


def biCopy(bi):
    result = BigInt(True)
    result.digits = list(bi.digits)
    if bi.isNeg:
        result.isNeg = True
    else:
        result.isNeg = False
    return result


def biNumBits(x):
    n = biHighIndex(x)
    d = x.digits[n]
    m = (n + 1) * bitsPerDigit
    result = m
    while (result > m - bitsPerDigit):
        if ((d & 0x8000) != 0):
            break
        d <<= 1
        result -= 1
    return result


def biAdd(x, y):
    result = None

    if (x.isNeg != y.isNeg):
        y.isNeg = (not y.isNeg)
        result = biSubtract(x, y)
        y.isNeg = (not y.isNeg)
    else:
        result = BigInt()
        c = 0
        n = 0
        i = 0
        while (i < len(x.digits)):
            i += 1
            n = x.digits[i] + y.digits[i] + c
            result.digits[i] = n & 0xffff
            if n >= biRadix:
                c = 1
        else:
            c = 0
        result.isNeg = x.isNeg
    return result


def biSubtract(x, y):
    result = None
    if (x.isNeg != y.isNeg):
        y.isNeg = (not y.isNeg)
        result = biAdd(x, y)
        y.isNeg = (not y.isNeg)
    else:
        result = BigInt()
        n = 0
        c = 0
        for index in range(len(x.digits)):
            n = x.digits[index] - y.digits[index] + c
            result.digits[index] = n & 0xffff
            if (result.digits[index] < 0):
                result.digits[index] += biRadix
            if n < 0:
                c = 0 - 1
            else:
                c = 0 - 0
        if (c == -1):
            c = 0
            for index in range((len(x.digits))):
                n = 0 - result.digits[index] + c
                result.digits[index] = n & 0xffff
                if (result.digits[index] < 0):
                    result.digits[index] += biRadix
                if n < 0:
                    c = 0 - 1
                else:
                    c = 0 - 0
            result.isNeg = (not x.isNeg)
        else:
            result.isNeg = x.isNeg
    return result


def arrayCopy(src, srcStart, dest, destStart, n):
    m = min([srcStart + n, len(src)])
    i = srcStart
    j = destStart
    while (i < m):
        dest[j] = src[i]
        i += 1
        j += 1


def biShiftLeft(x, n):
    digitCount = math.floor(n / bitsPerDigit)
    result = BigInt()
    arrayCopy(
        x.digits,
        0,
        result.digits,
        digitCount,
        len(result.digits) - digitCount
    )
    bits = n % bitsPerDigit
    rightBits = bitsPerDigit - bits
    i = len(result.digits) - 1
    i1 = i - 1
    while (i > 0):
        i -= 1
        i1 -= 1
        result.digits[i] = ((result.digits[i] << bits) & maxDigitVal) | (
            (result.digits[i1] & highBitMasks[bits]) >> rightBits)
    result.digits[0] = (result.digits[i] << bits) & maxDigitVal
    result.isNeg = x.isNeg
    return result


def biMultiplyByRadixPower(x, n):
    result = BigInt()
    arrayCopy(x.digits, 0, result.digits, n, len(result.digits) - n)
    return result


def biCompare(x, y):
    if (x.isNeg != y.isNeg):
        if x.isNeg:
            return 1 - 2 * 1
        else:
            return 1 - 2 * 0
    i = len(x.digits) - 1

    while (i >= 0):
        if (x.digits[i] != y.digits[i]):
            if (x.isNeg):
                if x.digits[i] > y.digits[i]:
                    return 1 - 2 * 1
                else:
                    return 1 - 2 * 0
            else:
                if x.digits[i] < y.digits[i]:
                    return 1 - 2 * 1
                else:
                    return 1 - 2 * 0
        i = i - 1
    return 0


lowBitMasks = [
    0x0000,
    0x0001,
    0x0003,
    0x0007,
    0x000f,
    0x001f,
    0x003f,
    0x007f,
    0x00ff,
    0x01ff,
    0x03ff,
    0x07ff,
    0x0fff,
    0x1fff,
    0x3fff,
    0x7fff,
    0xffff
]


def biMultiplyDigit(x, y):
    n = 0
    c = 0
    uv = 0

    result = BigInt()
    n = biHighIndex(x)
    c = 0
    j = 0
    while (j <= n):
        uv = result.digits[j] + x.digits[j] * y + c
        result.digits[j] = uv & maxDigitVal
        c = uv >> biRadixBits
        j += 1
    result.digits[1 + n] = c
    return result


def biShiftRight(x, n):
    digitCount = math.floor(n / bitsPerDigit)
    result = BigInt()
    arrayCopy(
        x.digits,
        digitCount,
        result.digits,
        0,
        len(x.digits) - digitCount
    )
    bits = n % bitsPerDigit
    leftBits = bitsPerDigit - bits
    i = 0
    i1 = i + 1
    while (i < (len(result.digits) - 1)):
        result.digits[i] = (result.digits[i] >> bits) | ((result.digits[i1] & lowBitMasks[bits]) << leftBits)
        i1 += 1
        i += 1
    result.digits[len(result.digits) - 1] >>= bits
    result.isNeg = x.isNeg
    return result


def biDivideModulo(x, y):
    nb = biNumBits(x)
    tb = biNumBits(y)
    origYIsNeg = y.isNeg
    q = None
    r = None
    if (nb < tb):
        if (x.isNeg):
            q = biCopy(bigOne)
            q.isNeg = (not y.isNeg)
            x.isNeg = False
            y.isNeg = False
            r = biSubtract(y, x)
            x.isNeg = True
            y.isNeg = origYIsNeg
        else:
            q = BigInt()
            r = biCopy(x)
        return [q, r]
    q = BigInt()
    r = x
    t = math.ceil(tb / bitsPerDigit) - 1
    lambdas = 0
    while (y.digits[t] < biHalfRadix):
        lambdas += 1
        y = biShiftLeft(y, 1)
        tb += 1
        t = math.ceil(tb / bitsPerDigit) - 1
    r = biShiftLeft(r, lambdas)
    nb += lambdas
    n = math.ceil(nb / bitsPerDigit) - 1
    b = biMultiplyByRadixPower(y, n - t)
    while (biCompare(r, b) != -1):
        q.digits[n - t] += 1
        r = biSubtract(r, b)
    i = n
    while (i > t):
        ri = 0 if i >= len(r.digits) else r.digits[i]
        ri1 = 0 if i - 1 >= len(r.digits) else r.digits[i - 1]
        ri2 = 0 if i - 2 >= len(r.digits) else r.digits[i - 2]
        yt = 0 if t >= len(y.digits) else y.digits[t]
        yt1 = 0 if t - 1 >= len(y.digits) else y.digits[t - 1]
        if (ri == yt):
            q.digits[i - t - 1] = maxDigitVal
        else:
            q.digits[i - t - 1] = math.floor((ri * biRadix + ri1) / yt)

        c1 = q.digits[i - t - 1] * (yt * biRadix + yt1)
        c2 = ri * biRadixSquared + (ri1 * biRadix + ri2)
        while (c1 > c2):
            q.digits[i - t - 1] -= 1
            c1 = q.digits[i - t - 1] * ((yt * biRadix) | yt1)
            c2 = ri * biRadix * biRadix + (ri1 * biRadix + ri2)
        b = biMultiplyByRadixPower(y, i - t - 1)
        r = biSubtract(r, biMultiplyDigit(b, q.digits[i - t - 1]))
        if (r.isNeg):
            r = biAdd(r, b)
            q.digits[i - t - 1] -= 1
        i -= 1
    r = biShiftRight(r, lambdas)
    q.isNeg = x.isNeg != origYIsNeg
    if (x.isNeg):
        if (origYIsNeg):
            q = biAdd(q, bigOne)
        else:
            q = biSubtract(q, bigOne)
        y = biShiftRight(y, lambdas)
        r = biSubtract(y, r)
    if (r.digits[0] == 0 and biHighIndex(r) == 0):
        r.isNeg = False

    return [q, r]


def biDivide(x, y):
    return biDivideModulo(x, y)[0]


def biDivideByRadixPower(x, n):
    result = BigInt()
    arrayCopy(x.digits, n, result.digits, 0, len(result.digits) - n)
    return result


def biMultiply(x, y):
    result = BigInt()
    c = 0
    n = biHighIndex(x)
    t = biHighIndex(y)
    u = 0
    uv = 0
    k = 0

    i = 0
    while (i <= t):
        c = 0
        k = i
        j = 0
        while (j <= n):
            uv = result.digits[k] + x.digits[j] * y.digits[i] + c
            result.digits[k] = uv & maxDigitVal
            c = uv >> biRadixBits
            j += 1
            k += 1
        result.digits[i + n + 1] = c
        i += 1
    result.isNeg = x.isNeg != y.isNeg
    return result


def biModuloByRadixPower(x, n):
    result = BigInt()
    arrayCopy(x.digits, 0, result.digits, 0, n)
    return result


class BarrettMu():
    def __init__(self, m):
        self.modulus = biCopy(m)
        self.k = biHighIndex(self.modulus) + 1
        b2k = BigInt()
        b2k.digits[2 * self.k] = 1
        self.mu = biDivide(b2k, self.modulus)
        self.bkplus1 = BigInt()
        self.bkplus1.digits[self.k + 1] = 1

    def BarrettMu_modulo(self, x):
        q1 = biDivideByRadixPower(x, self.k - 1)
        q2 = biMultiply(q1, self.mu)
        q3 = biDivideByRadixPower(q2, self.k + 1)
        r1 = biModuloByRadixPower(x, self.k + 1)
        r2term = biMultiply(q3, self.modulus)
        r2 = biModuloByRadixPower(r2term, self.k + 1)
        r = biSubtract(r1, r2)
        if (r.isNeg):
            r = biAdd(r, self.bkplus1)
        rgtem = biCompare(r, self.modulus) >= 0
        while (rgtem):
            r = biSubtract(r, self.modulus)
            rgtem = biCompare(r, self.modulus) >= 0
        return r

    def BarrettMu_multiplyMod(self, x, y):
        xy = biMultiply(x, y)
        return self.BarrettMu_modulo(xy)

    def BarrettMu_powMod(self, x, y):
        result = BigInt()
        result.digits[0] = 1
        a = x
        k = y
        while (True):
            if ((k.digits[0] & 1) != 0):
                result = self.BarrettMu_multiplyMod(result, a)
            k = biShiftRight(k, 1)
            if (k.digits[0] == 0 and biHighIndex(k) == 0):
                break
            a = self.BarrettMu_multiplyMod(a, a)
        return result


class RSAKeyPair():
    def __init__(self, encryptionExponent, decryptionExponent, modulus, keylen=None):
        self.e = biFromHex(encryptionExponent)
        self.d = biFromHex(decryptionExponent)
        self.m = biFromHex(modulus)
        global chunkSize
        if (type(keylen) != type(0)):
            self.chunkSize = 2 * biHighIndex(self.m)
        else:
            self.chunkSize = keylen / 8

        self.radix = 16

        self.barrett = BarrettMu(self.m)


class RSAAPP():
    def __init__(self):
        self.NoPadding = 'NoPadding'
        self.PKCS1Padding = 'PKCS1Padding'
        self.RawEncoding = 'RawEncoding'
        self.NumericEncoding = 'NumericEncoding'


rs = RSAAPP()

def digitToBytes(n):
    c1 = (n & 0xff).encode("utf-8")
    n >>= 8
    c2 = (n & 0xff).encode("utf-8")
    return c2 + c1


def biToBytes(x):
  result = ''
  i = biHighIndex(x)
  while(i > -1):
      result += digitToBytes(x.digits[i])
      i -= 1
  return result

hexToChar = [
  '0',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  'a',
  'b',
  'c',
  'd',
  'e',
  'f'
]

def reverseStr(s):
  result = ''
  i = len(s) - 1
  while(i > -1):
      result = result + s[i]
      i -= 1
  return result

def digitToHex(n):
  mask = 0xf
  result = ''
  i = 0
  while (i < 4):
      result += hexToChar[n & mask]
      n >>= 4
      i += 1
  return reverseStr(result)


def biToHex(x):
  result = ''
  n = biHighIndex(x)
  i = biHighIndex(x)
  while(i > -1):
      result += digitToHex(x.digits[i])
      i -= 1
  return result

hexatrigesimalToChar = [
  '0',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  'a',
  'b',
  'c',
  'd',
  'e',
  'f',
  'g',
  'h',
  'i',
  'j',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'w',
  'x',
  'y',
  'z'
]

def biToString(x, radix):
  b = BigInt()
  b.digits[0] = radix
  qr = biDivideModulo(x, b)
  result = hexatrigesimalToChar[qr[1].digits[0]]
  while (biCompare(qr[0], bigZero) == 1):
    qr = biDivideModulo(qr[0], b)
    digit = qr[1].digits[0]
    result += hexatrigesimalToChar[qr[1].digits[0]]
  pushString = ''
  if x.isNeg:
      pushString = '-'
  return pushString + reverseStr(result)


def encryptedString(key, s, pad = None, encoding=None):
    a = []
    sl = len(s)
    i = 0
    j = 0
    k = 0
    padtype = None
    encodingtype = None
    rpad = None
    al = None
    result = ''
    block = None
    crypt = None
    text = None

    if (type(pad) == type('string')):
        if (pad == rs.NoPadding):
            padtype = 1
        elif (pad == rs.PKCS1Padding):
            padtype = 2
        else:
            padtype = 0
    else:
        padtype = 0

    if (type(encoding) == type('string') and encoding == rs.RawEncoding):
        encodingtype = 1
    else:
        encodingtype = 0

    if (padtype == 1):
        if (sl > key.chunkSize):
            sl = key.chunkSize
    elif (padtype == 2):
        if (sl > key.chunkSize - 11):
            sl = key.chunkSize - 11

    i = 0

    if (padtype == 2):
        j = sl - 1
    else:
        j = key.chunkSize - 1

    while (i < sl):
        if (padtype):
            a.append(ord(s[i]))
        else:
            a.append(ord(s[i]))
        i += 1
        j -= 1
    if (padtype == 1):
        i = 0

    j = key.chunkSize - (sl % key.chunkSize)

    while (j > 0):
        if (padtype == 2):
            rpad = math.floor(math.random() * 256)
            while (not rpad):
                rpad = math.floor(math.random() * 256)
            a.append(rpad)
        else:
            a.append(0)
        i += 1
        j -= 1

    if (padtype == 2):
        a[sl] = 0
        a[key.chunkSize - 2] = 2
        a[key.chunkSize - 1] = 0

    al = len(a)

    i = 0
    while(i < al):
        block = BigInt()
        j = 0
        k = i
        while(k < i + key.chunkSize):
            block.digits[j] = a[k]
            k += 1
            block.digits[j] += a[k] << 8
            k += 1
            j += 1
        crypt = key.barrett.BarrettMu_powMod(block, key.e)
        if (encodingtype == 1):
            text = biToBytes(crypt)
        else:
            text = biToHex(crypt) if key.radix == 16 else biToString(crypt, key.radix)
        result += text
        i += key.chunkSize
    return result


if __name__ == '__main__':
    setMaxDigits(130)
    key = RSAKeyPair(RSA_EXPONENT, '', RSA_MODULUS)
    encryptRtn = encryptedString(key, '123123')
    print(encryptRtn)

