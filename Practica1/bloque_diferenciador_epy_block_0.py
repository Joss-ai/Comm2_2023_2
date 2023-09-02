import numpy as np
from gnuradio import gr

class blk(gr.sync_block): 

    def __init__(self):
        
        gr.sync_block.__init__(
            self,
            name="Bloque_Diferenciador",
            in_sig=[np.float32],
            out_sig=[np.float32]
        
        )
        self.acum_anterior = 0
    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        
        N = len(x)
        diff = np.cumsum(x) - self.acum_anterior
        self.acum_anterior = diff[N-1]
        y[:] = diff
        return len(y)
