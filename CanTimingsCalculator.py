#THIS IS A DRAFT TODO: add stuff BEFORE the prescaler
# can speed calculator
FrequencyAfterCanBusScaller = 8000000
Tseg1=13
Tseg2=2
BandwithCanbus = FrequencyAfterCanBusScaller/(Tseg1+Tseg2+1)
print("Frequency of CAN bus is: ", BandwithCanbus," bits per sec, with a small 'b'")
print("or ", BandwithCanbus/1000, " kbps")
print("or ", BandwithCanbus/1000000, " Mbps")