#!/bin/bash
cat input.txt | sed 's/[a-z]//g' | rev | sed 's/.*/&&/' | awk '{sum += substr($0, length($0)/2, 2)} END {print "part 1 : " sum}'
