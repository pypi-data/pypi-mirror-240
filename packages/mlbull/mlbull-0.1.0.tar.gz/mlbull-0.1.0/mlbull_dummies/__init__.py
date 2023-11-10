class FunctionGatherer:
    def __init__(self) -> None:
        self.gathered_functions = []

    def __call__(self, function):
        self.gathered_functions.append(function)
        return function


predict_function = FunctionGatherer()
