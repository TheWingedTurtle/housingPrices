import Load_Datasets as ld


housing = ld.loading_house("housing.csv")
print housing.info()