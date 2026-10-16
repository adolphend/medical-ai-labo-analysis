#!/usr/bin/env python3
"""Check installed runtime and hardware; never load weights or send data."""
import json,platform
import torch
data={"os":platform.system(),"torch":torch.__version__,
      "cuda_available":torch.cuda.is_available(),
      "mps_available":bool(getattr(torch.backends,"mps",None) and torch.backends.mps.is_available())}
if data["cuda_available"]:
    p=torch.cuda.get_device_properties(0)
    data["gpu"]=p.name;data["vram_gib"]=round(p.total_memory/1024**3,2)
print(json.dumps(data,indent=2))
