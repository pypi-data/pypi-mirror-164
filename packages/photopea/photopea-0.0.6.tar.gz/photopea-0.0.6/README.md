# Photopea

**Photo** and **Video** Convertor.

## Instructions

1. Install:

```
pip install photopea
```

2. Age and Gender determination:

```python
from photopea import getface
from getface import predict_age_and_gender

# Input photo file
photo = "/home/uzbpromax/Pictures/photo.png"
# Output photo file
output = "/home/uzbpromax/Pictures/output.png"
# Check Age and Gender
r = predict_age_and_gender(photo, output)
```

