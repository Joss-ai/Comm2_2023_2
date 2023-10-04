import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following: it only has 2 inputs, the first one is used to define the amplitude of the exponential function and the second specifies the value which multiplies the exponent by j (the imaginary number).
    The output is a complex signal with the form: input_1*e^(j*input_2).
    To design a modulation which uses the real and imaginary domain is recommended to keep the amplitud as a constant and send the message in the exponent of the function."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])
