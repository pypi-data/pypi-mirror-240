import numpy as np
import deepxde as dde
from .PINN import PINN
from ..cases.PDECases import Burgers
from ..decomposition.decomposition import time_marching_decomposition


class TimeMarching:
    def __init__(self, PDECase, solver, **kwargs):
        dde.optimizers.config.set_LBFGS_options(maxiter=1000)
        self.PDECase_list = time_marching_decomposition(PDECase, **kwargs)
        self.solver_list = [solver(PDECase) for PDECase in self.PDECase_list]

    def closure(self):
        self.train_step()

    def train(self):
        self.closure()

    def train_step(self):
        for solver in self.solver_list:
            solver.train()

    def save(self, add_time=False):
        for solver in self.solver_list:
            solver.save(add_time=add_time)

    def plot_loss_history(self, axes=None, train=False, use_time=False):
        for solver in self.solver_list:
            solver.plot_loss_history(axes, train, use_time)


if __name__ == "__main__":
    PDECase = Burgers(NumDomain=2000 // 2)
    solver = TimeMarching(PDECase=PDECase, solver=PINN, num_split=2)
    solver.train()
    solver.save(add_time=True)
