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


class DataPipeline:
    def __init__(self, read_function):
        self.read_function = read_function

    def template_method(self) -> None:

        self.df = self.read_function()
        self.summarize_data()
        self.output_summary()

    def summarize_data(self) -> None:
        self.summarized_data = self.df.describe()

    def output_summary(self) -> None:
        print(self.summarized_data)


def csv_data_pipeline():

    return pd.read_csv("./airline-safety.csv")


def json_data_pipeline():
    return pd.read_json("./airline-safety.json")


def client_code(pipeline) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """

    pipeline.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(DataPipeline(json_data_pipeline))

    print("Same client code can work with different subclasses:")
    client_code(DataPipeline(csv_data_pipeline))
