import os
import pandas as pd
import matplotlib.pyplot as plt
project_path = "/Users/abhinavsrivastav/Desktop/projects/one/"
dataset_path = "datasets/"

csv_path = os.path.join(project_path, dataset_path)


# housing = pd.read_csv(os.path.join(csv_path , "housing.csv"))
# print housing.info()

# print pd.read_csv(os.path.join(csv_path, "housing.csv")).head()


def loading_house(name_of_dataset):
    return pd.read_csv(os.path.join(csv_path, name_of_dataset))


housing = loading_house("housing.csv")

housing.hist(bins=50, figsize=(20, 15))
