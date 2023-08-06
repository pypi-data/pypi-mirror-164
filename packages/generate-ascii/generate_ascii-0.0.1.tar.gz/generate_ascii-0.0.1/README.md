# Generate ASCII Image

Generate **A S C I I** iamge.

## Instructions

1. Install:

```
pip install generate_ascii
```

2. Generate an ASCII image:

```python
from generate_ascii import synthesize

# initialize drive object (to generate ASCII image)
drive = synthesize.Drive()
# generate a ASCII visual (dark_mode optional)
drive.generate(dark_mode=True)
# save to png
drive.to_png('img_name.png')
```