import torch

class ID(torch.nn.Module):
    def __init__(self, n_atom, weights=None, optimizable=False):
        super().__init__()
        self.register_buffer('n_atom', torch.tensor(n_atom))
        self.register_buffer('triu_idx', torch.triu_indices(n_atom, n_atom, 1))
        
        if weights is None:
            weights = torch.ones(self.triu_idx.shape[-1])
        else:
            assert weights.shape == self.triu_idx[0].shape, "the length of the weights does not match the length of the descriptor"
            weights = weights.float()
        
        if optimizable:
            self.register_parameter('weights', torch.nn.parameter.Parameter(weights))
        else:
            self.register_buffer('weights', weights)
    
    def forward(self, xyz):
        return self.weights/distance_matrix(xyz, xyz)[:, self.triu_idx[0], self.triu_idx[1]]

    def back_convert(self, descr):
        n = descr.shape[-2]
        d_mat = torch.zeros(n, self.n_atom, self.n_atom)
        distances = self.weights/descr
        d_mat[:, self.triu_idx[0], self.triu_idx[1]] = distances
        d_mat = torch.transpose(d_mat, -2, -1)
        d_mat[:, self.triu_idx[0], self.triu_idx[1]] = distances
        d2 = d_mat**2
        c = torch.eye(self.n_atom).repeat(n, 1, 1) - torch.ones_like(d2)/self.n_atom
        b = -0.5 * c.matmul(d2.matmul(c))
        U, S, _ = torch.linalg.svd(b)
        xyz = S[:, None, :3].sqrt()*U[:, :, :3]
        return xyz

class RE(ID):
    def __init__(self, eqxyz, optimizable=False):
        n_atom = eqxyz.shape[-2]
        weights = distance_matrix(eqxyz, eqxyz)[torch.triu_indices(n_atom, n_atom, 1).unbind()]
        super().__init__(n_atom, weights, optimizable)

class CM(ID):
    def __init__(self, z, optimizable=False):
        n_atom = z.shape[-1]
        weights = z.outer(z)[torch.triu_indices(n_atom, n_atom, 1).unbind()]
        super().__init__(n_atom, weights, optimizable)

def distance_matrix(x, y):
    x2 = (x**2).sum(dim=-1)
    y2 = (y**2).sum(dim=-1)
    xy = torch.matmul(x, torch.transpose(y, -2, -1))
    return (x2.unsqueeze(-1) - 2*xy + y2.unsqueeze(-2)).sqrt()