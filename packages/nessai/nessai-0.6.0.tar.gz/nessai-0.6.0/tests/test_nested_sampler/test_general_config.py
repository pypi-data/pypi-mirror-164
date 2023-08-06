# -*- coding: utf-8 -*-
"""
Test general config functions called when the nested sampler is initialised.
"""
import os
import numpy as np
import pytest
from unittest.mock import patch, MagicMock

from nessai.nestedsampler import NestedSampler


def test_init(sampler):
    """Test the init method"""
    pool = "pool"
    n_pool = 2
    model = MagicMock()
    model.verify_model = MagicMock()
    model.configure_pool = MagicMock()

    sampler.setup_output = MagicMock()
    sampler.configure_flow_reset = MagicMock()
    sampler.configure_flow_proposal = MagicMock()
    sampler.configure_uninformed_proposal = MagicMock
    NestedSampler.__init__(
        sampler,
        model,
        nlive=100,
        poolsize=100,
        pool=pool,
        n_pool=n_pool,
    )
    assert sampler.initialised is False
    assert sampler.nlive == 100
    model.verify_model.assert_called_once()
    model.configure_pool.assert_called_once_with(pool=pool, n_pool=n_pool)


@patch("numpy.random.seed")
@patch("torch.manual_seed")
def test_set_random_seed(mock1, mock2, sampler):
    """Test the correct functions are called when setting the random seed"""
    NestedSampler.setup_random_seed(sampler, 150914)
    mock1.assert_called_once_with(150914)
    mock2.assert_called_once_with(seed=150914)


@patch("numpy.random.seed")
@patch("torch.manual_seed")
def test_no_random_seed(mock1, mock2, sampler):
    """Assert no seed is set if seed=None"""
    NestedSampler.setup_random_seed(sampler, None)
    mock1.assert_not_called()
    mock2.assert_not_called()


def test_setup_output(sampler, tmpdir):
    """Test setting up the output directories"""
    p = tmpdir.mkdir("outputs")
    sampler.plot = False
    path = os.path.join(p, "tests")
    resume_file = NestedSampler.setup_output(sampler, path)
    assert os.path.exists(path)
    assert resume_file == os.path.join(path, "nested_sampler_resume.pkl")


def test_setup_output_w_plotting(sampler, tmpdir):
    """Test setting up the output directories with plot=True"""
    p = tmpdir.mkdir("outputs")
    sampler.plot = True
    path = os.path.join(p, "tests")
    NestedSampler.setup_output(sampler, path)
    assert os.path.exists(os.path.join(path, "diagnostics"))


def test_setup_output_w_resume(sampler, tmpdir):
    """Test output configuration with a specified resume file"""
    p = tmpdir.mkdir("outputs")
    sampler.plot = False
    path = os.path.join(p, "tests")
    resume_file = NestedSampler.setup_output(sampler, path, "resume.pkl")
    assert resume_file == os.path.join(path, "resume.pkl")


def test_configure_max_iteration(sampler):
    """Test to make sure the maximum iteration is set correctly"""
    NestedSampler.configure_max_iteration(sampler, 10)
    assert sampler.max_iteration == 10


def test_configure_no_max_iteration(sampler):
    """Test to make sure if no max iteration is given it is set to inf"""
    NestedSampler.configure_max_iteration(sampler, None)
    assert sampler.max_iteration == np.inf


def test_training_frequency(sampler):
    """Make sure training frequency is set"""
    NestedSampler.configure_training_frequency(sampler, 100)
    assert sampler.training_frequency == 100


@pytest.mark.parametrize("f", [None, "inf", "None"])
def test_training_frequency_on_empty(sampler, f):
    """Test the values that should give 'train on empty'"""
    NestedSampler.configure_training_frequency(sampler, f)
    assert sampler.training_frequency == np.inf
