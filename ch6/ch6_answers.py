from abc import ABC, abstractmethod
import pandas as pd

"""
The following code implements a simple data pipeline using the Template Method pattern mentioned briefly in Chapter 6
Your task is to re-factor this code along functional principles taking advantage of functions as first-class objects.

You can read more about the Template Method pattern here:
https://refactoring.guru/design-patterns/template-method

The code below borrows heavily from the conceptual Python example here:
https://refactoring.guru/design-patterns/template-method/python/example#lang-features
"""


class AbstractDataPipeline(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive
    operations.

    Concrete subclasses should implement these operations, but leave the
    template method itself intact.
    """

    def template_method(self, types) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """
        
        self.read_file_to_df(types)
        self.summarize_data()
        self.output_summary()

    # These operations already have implementations.

    def summarize_data(self) -> None:
        self.summarized_data = self.df.describe()

    def output_summary(self) -> None:
        print(self.summarized_data)

    # These operations have to be implemented in subclasses.

    def read_file_to_df(self, types) -> None:
        if types == "json":
            self.df = pd.read_json("./airline-safety.json")
        elif types == "csv":
            self.df = pd.read_csv("./airline-safety.csv")
        else:
            raise NotImplementedError("NIE")


def client_code(abstract_class, types) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """

    abstract_class.template_method(types)


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    #client_code(JsonDataPipeline())
    client_code(AbstractDataPipeline(), types = "json")

    print("Same client code can work with different subclasses:")
    #client_code(CsvDataPipeline())
    client_code(AbstractDataPipeline(), types = "csv")
