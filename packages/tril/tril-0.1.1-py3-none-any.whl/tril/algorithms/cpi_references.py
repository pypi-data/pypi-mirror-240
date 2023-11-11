from typing import Optional

from accelerate import Accelerator

from tril.algorithms.cpi import CPI
from tril.logging import Tracker


class CPIReference(CPI):
    def __init__(
        self, cfg, accelerator: Accelerator, tracker: Optional[Tracker] = None
    ):
        super().__init__(cfg, accelerator, tracker)

    def generate_rollin(self, obs_tensor):
        gen_tokens = obs_tensor["reference_encoded_pt"][:, -self.max_gen_len :]
        seq_lens = gen_tokens.not_equal(self.tokenizer.pad_token_id).sum(axis=1).numpy()
        return gen_tokens, seq_lens
