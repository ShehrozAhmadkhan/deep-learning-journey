import torch

m1 = torch.rand(3,3)
#print(m1)
#print(m1[0])
#print(m1[2])
#print(m1[1,2])
#print(m1[0:,:1])

x = torch.tensor([[1,2,3,4,5],[6,7,8,9,10],[9,8,7,6,5],[4,3,2,1,0]])
y = torch.tensor([5,5,5,5,5])
z = x + y
#print(x)
#print(y)
#print(z)


# Check karein GPU available hai ya nahi
print(torch.cuda.is_available())

# Tensor CPU pe by default banta hai
x = torch.rand(3, 3)
print(x.device)   # cpu

# Agar GPU available ho, tensor ko GPU pe move kar sakte hain
if torch.cuda.is_available():
    x = x.to("cuda")
    print(x.device)   # cuda:0