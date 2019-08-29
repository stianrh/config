
#!/bin/bash

# This script opens 4 terminal windows.

i="0"

while [ $i -lt 100 ]
do
nrfjprog --recover -f nrf52
i=$[$i+1]

done

