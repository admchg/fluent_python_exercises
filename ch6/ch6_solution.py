import pandas as pd

def template_method(file_reader):
    """
    The template method defines the skeleton of an algorithm.
    """

    df = file_reader()
    summarized_data = summarize_data(df.copy())
    output_summary(summarized_data)


def summarize_data(df):
    summarized_data = df.describe()
    return summarized_data


def output_summary(summarized_data):
    print(summarized_data)


def read_json_file_to_df():
    df = pd.read_json('./airline-safety.json')
    return df


def read_csv_file_to_df():
    df = pd.read_csv('./airline-safety.csv')
    return df



if __name__ == "__main__":
    template_method(file_reader=read_json_file_to_df)

    template_method(file_reader=read_csv_file_to_df)