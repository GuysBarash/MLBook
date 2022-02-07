import numpy as np
import pandas as pd
from scipy.optimize import minimize


class F_class:
    def __init__(self, a, A, B):
        self.a = a
        self.A = A
        self.B = B

    def calc(self, x):
        res = np.zeros(x.shape)

        bigger_idx = x > self.a
        smaller_idx = x <= self.a

        res[bigger_idx] = np.power(x[bigger_idx], 2) * self.A
        res[smaller_idx] = np.power(x[smaller_idx], 2) * self.B

        return res


a = 0
A = 1
B = -1

f = F_class(a, A, B)
X = np.arange(-5, 5)
Y = f.calc(X)
D = pd.DataFrame(columns=['X', 'Y'], data=np.array([X, Y]).T)


def sum_of_squares(params, X, Y):
    a, A, B = params
    model = F_class(a, A, B)
    y_pred = model.calc(X)
    obj = np.sqrt(((y_pred - Y) ** 2).sum())
    return obj


# perform fit to find optimal parameters
# initial value is a guess
initial_guess = [0., 0., 0.]  # a, A, B
res = minimize(sum_of_squares, x0=initial_guess, args=(X, Y), tol=1e-5, method="Powell")
a_pred, A_pred, B_pred = res.x

print("Estimated values:")
print(f"a = {a_pred:>.3f}")
print(f"A = {A_pred:>.3f}")
print(f"B = {B_pred:>.3f}")

model = F_class(a_pred, A_pred, B_pred)
Y_pred = model.calc(X)
MSE = np.sqrt(((Y_pred - Y) ** 2).sum())
print(f"MSE: {MSE}")
