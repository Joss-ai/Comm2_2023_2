import numpy as np
from gnuradio import gr

class QPSKModulator(gr.sync_block):

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='QPSK Modulator',
            in_sig=[np.int8],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        input_data = input_items[0]
        output_data = output_items[0]

        # Mapear los valores de input_data a símbolos QPSK
        constelation = {
            0: 1 + 0j,
            1: 0 + 1j,
            2: -1 + 0j,
            3: 0 - 1j
        }

        for i in range(len(input_data)):
            symbol = constelation.get(input_data[i], 0)
            output_data[i] = symbol

        return len(input_data)

