class DFA:
    def __init__(self , Q, sigma, delta, q0, F):
        self.Q = Q # set of states
        self.sigma = sigma # set of symbols
        self.delta = delta # transition function as a dictionary
        self.q0 = q0 # initial state
        self.F = F # set of final states
    
    def __repr(self):
        return f"DFA({self.Q},\n\t{self.sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"