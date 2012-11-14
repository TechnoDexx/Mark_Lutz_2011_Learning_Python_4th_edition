#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

L = [2, 4, 9, 16, 25]

L1 = []
for x in L: L1.append(math.sqrt(x))
print(L1)

L2 = map(math.sqrt, L)
print(L2)

L3 = [math.sqrt(x) for x in L]
print(L3)
