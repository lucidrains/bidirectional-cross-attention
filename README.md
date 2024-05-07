## Bidirectional Cross Attention

A simple cross attention that updates both the source and target in one step. The key insight is that one can do <a href="https://arxiv.org/abs/2001.04451">shared query / key attention</a> and use the attention matrix twice to update both ways. Used for a contracting project for predicting DNA / protein binding <a href="https://github.com/lucidrains/tf-bind-transformer">here</a>.

## Install

```bash
$ pip install bidirectional-cross-attention
```

## Usage

```python
import torch
from bidirectional_cross_attention import BidirectionalCrossAttention

video = torch.randn(1, 4096, 512)
audio = torch.randn(1, 8192, 386)

video_mask = torch.ones((1, 4096)).bool()
audio_mask = torch.ones((1, 8192)).bool()

joint_cross_attn = BidirectionalCrossAttention(
    dim = 512,
    heads = 8,
    dim_head = 64,
    context_dim = 386
)

video_out, audio_out = joint_cross_attn(
    video,
    audio,
    mask = video_mask,
    context_mask = audio_mask
)

# attended output should have the same shape as input

assert video_out.shape == video.shape
assert audio_out.shape == audio.shape
```

## Todo

- [ ] allow for cosine sim attention

## Citations

```bibtex
@article{Hiller2024PerceivingLS,
    title   = {Perceiving Longer Sequences With Bi-Directional Cross-Attention Transformers},
    author  = {Markus Hiller and Krista A. Ehinger and Tom Drummond},
    journal = {ArXiv},
    year    = {2024},
    volume  = {abs/2402.12138},
    url     = {https://api.semanticscholar.org/CorpusID:267751060}
}
```
