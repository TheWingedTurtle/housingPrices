import numpy as np
from zlib import crc32


def split_datasets(data, ratio):
	len_test = int(len(data) * ratio)
	shuffeled_indices = np.random.permutation(len(data))
	test_indices = shuffeled_indices[:len_test]
	train_indices = shuffeled_indices[len_test:]
	return data.iloc[test_indices], data.iloc[train_indices]


def test_set_check(identifier, test_ratio):
	return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2 ** 32


def split_train_Ids(data, test_ratio, id_column):
	ids = data[id_column]
	in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
	return data.loc[in_test_set], data.loc[~in_test_set]
