import isoext
import torch 

def sphere_sdf(x):
    return x.norm(dim=-1) - 0.5

res = 128
x = torch.linspace(-1, 1, res)
y = torch.linspace(-1, 1, res)
z = torch.linspace(-1, 1, res)
grid = torch.stack(torch.meshgrid([x, y, z], indexing='xy'), dim=-1)
sdf = sphere_sdf(grid).cuda() # Only accept a gpu tensor from pytorch for now

aabb = [-1, -1, -1, 1, 1, 1]
isolevel = -0.2

v, f = isoext.marching_cubes(sdf, aabb, isolevel)

print(v)