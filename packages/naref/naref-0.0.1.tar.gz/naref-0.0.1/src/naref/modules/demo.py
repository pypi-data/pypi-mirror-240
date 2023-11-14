#!/usr/bin/env python
"""
Defines reasonable demo-testing functions
"""
from naref.modules.classical.hyper import HyperC
from naref.modules.quantum.hyper import HyperQ
from naref.modules.quantum import QRC
from naref.modules.classical import CRC
from naref.modules import data

def fastest_hs() -> (HyperC, HyperQ):
	"""
	Fastest hyperparameter search
	Returns:
		the completed HyperC and HyperQ object
		all relevant info in csv files
	"""
	hc = HyperC(
		sample_len_list=[8],
		nb_neurons_list=[9, 12, 16, 25, 70],
		input_type_list=['sine'],
		train_len_list=[250, 400],
		verbose=False)
	hc.search()
	hq = HyperQ(
		sample_len_list=[8],
		nb_atoms_list=[4],
		N_samples_list=[1024],
		inp_duration_list=[1000],
		reset_rate_list=[0],
		geometry_list=None,
		atom_distance_list=[15, 20],
		input_type_list=['sine'],
		train_len_list=[250, 400])
	hq.search()
	return hc, hq


def fast_hs() -> (HyperC, HyperQ):
	"""
	Fast hyperparameter search
	Returns:
		the completed HyperC and HyperQ object
		all relevant info in csv files
	"""
	hc = HyperC(
		sample_len_list=[6, 8, 10],
		nb_neurons_list=[9, 12, 16, 25, 70],
		input_type_list=['sine'],
		train_len_list=[250, 400],
		verbose=False)
	hc.search()
	hq = HyperQ(
		sample_len_list=[8],
		nb_atoms_list=[9],
		N_samples_list=[1024],
		inp_duration_list=[1000],
		reset_rate_list=[0],
		geometry_list=None,
		atom_distance_list=[15, 20],
		input_type_list=['sine'],
		train_len_list=[250, 400])
	hq.search()
	return hc, hq


def long_hs() -> (HyperC, HyperQ):
	"""
	Long hyperparameter search
	Returns:
		the completed HyperC and HyperQ object
		all relevant info in csv files
	"""
	hc = HyperC(
		sample_len_list=[8],
		nb_neurons_list=[9, 12, 16, 25, 70],
		input_type_list=['sine', 'mackey'],
		train_len_list=[250, 300, 350, 400, 450, 500, 550])
	hc.search()
	hq = HyperQ()
	hq.search()
	return hc, hq


def demo_notebook():
	"""
	Function used for a live demonstration
	"""
	qrc = QRC(
		sample_len=data.sample_len,
		nb_atoms=data.nb_atoms,
		N_samples=data.N_samples,
		inp_duration=data.inp_duration,
		reset_rate=data.reset_rate,
		geometry=data.geometry,
		atom_distance=data.atom_distance,
		input_type=data.input_type,
		test_len=data.real_test_len,
		train_len=data.real_train_len,
		verbose=True)
	qrc.build_model(data.inp_test, data.inp_train)
	qrc.show_test_prediction()
	qrc.show_train_prediction()
	qrc.get_error_train()
	qrc.get_error_test()
	crc = CRC(
		sample_len=data.sample_len,
		nb_neurons=data.nb_neurons)
	crc.build_model(data.inp_test, data.inp_train)
	crc.show_test_prediction()
	crc.show_train_prediction()
	crc.get_error_train()
	crc.get_error_test()
