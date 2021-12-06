#!/usr/bin/env python

import numpy as np
from datetime import datetime
import time


if __name__ == '__main__':
    try:
        # get current time as a timestamp for the initial script execution
        now = datetime.utcnow()
        print(f'{now} - Starting times.py ✅')
    except Exception as e:
        print(f'{e} ❌')
