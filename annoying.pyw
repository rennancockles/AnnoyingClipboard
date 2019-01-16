# -*- coding: utf-8 -*-

import clipboard
import random
import string
import time


while True:
    size = random.randint(5, 20)
    txt = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(size))
    clipboard.copy(txt)
    time.sleep(.5)

