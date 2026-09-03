import torch

a = 5 # scalar

b = torch.tensor([1,2,3,4]) #vector / 1D tensor
"""
print(b)
print(b.shape)
"""

c = torch.tensor([[1,2,3,4,5],[1,2,3,4,5]]) #matrix / 2D tensor

#print(c)
#print(c.shape)


d = torch.rand(3,3)
#print(d)
f = torch.ones(3,3)
#print(f)

add = d + f
#print(add)
mul = d*f
#print(mul)

A = d @ f
#print(A)

x = torch.zeros(3,3)
#print(x)
y = torch.arange(0,12,2)
#print(y)

p = torch.rand(4,4)
print(p)
print()
print(p.T)


z = torch.ones(4,4)
#print(z)

sub = p - z
#print(sub)

div =  p / z
#print(div)

#print(b.reshape(2,2))
#print(b.dtype)