import hardware.rigol as ri
import numpy as np
import time


rigol=ri.DP1116A(device="TCPIP0::129.69.46.218::inst0::INSTR")

sweep_curr=np.linspace(0.001,0.1,num=100)
rigol.getOutput()
rigol.OutputEnable()

for curr in sweep_curr:
	rigol.setOutput(1,curr)
	time.sleep(0.1)
