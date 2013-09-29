__author__ = 'Fabianus'

import sys
import re

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
print ' '.join(str(x+1) for x in (m.start() for m in re.finditer('(?=%s)' % t, s)))