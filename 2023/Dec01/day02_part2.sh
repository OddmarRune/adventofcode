#!/bin/bash
cat input.txt | sed -e 's/one/o1e/g' -e 's/two/t2o/g' -e 's/three/t3e/g' -e 's/four/4/g' \
	-e 's/five/5e/g' -e 's/six/6/g' -e 's/seven/7n/g' -e 's/eight/e8t/g' \
	-e 's/nine/9e/g' -e 's/[a-z]//g' | rev | sed 's/.*/&&/' | \
	awk '{sum += substr($0, length($0)/2, 2)} END {print "part 2 : " sum}'
