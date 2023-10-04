import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following: the general property 'fc' defines the central frequency of the sinusoidal carrier signal and the configuration 'samp_rate' is used to choose the number of samples per second to calculate.
      It has 2 inputs the first one configures the VCO's amplitud and the second the frequency deviation. The output is an amplitude or frequency modulated signal in the form of: input1*cos(2*pi*fc+input2).
      Example: To design an amplitude modulation use a constant (example 1) for the second input 'frequency deviation' to avoid frequency variation and in the first input the message to modulate, it can be a streaming signal as [1 0 0 1 ...]."""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


