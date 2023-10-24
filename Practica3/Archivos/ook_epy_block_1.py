

import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='VCO_RF',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
       

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        y[:]=A*np.cos(2*math.pi*Q)
        return len(output_items[0])
