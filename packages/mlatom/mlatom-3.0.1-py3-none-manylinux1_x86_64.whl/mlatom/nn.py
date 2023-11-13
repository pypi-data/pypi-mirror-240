import torch
from torch.nn import Sequential

class MLP(torch.nn.ModuleList):
    def __init__(self, neurons, activation_function=torch.nn.ReLU):
        layers = []
        for i in range(len(neurons)-2):
            layers.append(torch.nn.Linear(neurons[i],neurons[i+1]))
            layers.append(activation_function())
        layers.append(torch.nn.Linear(neurons[i+1],neurons[i+2]))
        super(MLP, self).__init__(layers)

    def forward(self, x):
        for module in self:
            x = module(x)
        return x

class Parallel(Sequential):
    def __init__(self, *args):
        super(Parallel, self).__init__(*args)
    
    def forward(self, x):
        return torch.cat([module(x) for module in self], dim=1)

def batch_jacobian(y, x):
    y=y.sum(dim=0)
    jac = [torch.autograd.grad(yi, x, retain_graph=True)[0] for yi in y]
    jac = torch.stack(jac, dim=1)
    return jac