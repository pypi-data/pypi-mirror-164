# -*- coding: utf-8 -*-
"""
Test the properties in NestedSampler
"""
from collections import deque
import time
import datetime
import numpy as np
import pytest
from unittest.mock import MagicMock

from nessai.nestedsampler import NestedSampler


@pytest.fixture()
def sampler(sampler):
    sampler.state = MagicMock()
    return sampler


def test_log_evidence(sampler):
    """Check evidence is returned"""
    sampler.state.logZ = -2
    assert NestedSampler.log_evidence.__get__(sampler) == -2


def test_information(sampler):
    """Check most recent information estimate is returned"""
    sampler.state.info = [1, 2, 3]
    assert NestedSampler.information.__get__(sampler) == 3


def test_likelihood_calls(sampler):
    """Check likelihood calls from model are returned"""
    sampler.model = MagicMock()
    sampler.model.likelihood_evaluations = 10
    assert NestedSampler.likelihood_calls.__get__(sampler) == 10


def test_likelihood_evaluation_time(sampler):
    """Assert the time is the some of the time for individual proposals"""
    sampler.model = MagicMock()
    sampler.model.likelihood_evaluation_time = 1.0
    assert NestedSampler.likelihood_evaluation_time.__get__(sampler) == 1.0


def test_population_time(sampler):
    """Assert the time is the some of the time for individual proposals"""
    sampler._uninformed_proposal = MagicMock()
    sampler._flow_proposal = MagicMock()
    sampler._uninformed_proposal.population_time = 1
    sampler._flow_proposal.population_time = 2
    assert NestedSampler.proposal_population_time.__get__(sampler) == 3


def test_acceptance(sampler):
    """Test the acceptance calculation"""
    sampler.iteration = 10
    sampler.likelihood_calls = 100
    assert NestedSampler.acceptance.__get__(sampler) == 0.1


def test_current_sampling_time(sampler):
    """Test the current sampling time"""
    sampler.finalised = False
    sampler.sampling_time = datetime.timedelta(seconds=10)
    sampler.sampling_start_time = datetime.datetime.now()
    time.sleep(0.01)
    t = NestedSampler.current_sampling_time.__get__(sampler)
    assert t.total_seconds() > 10.0


def test_current_sampling_time_finalised(sampler):
    """Test the current sampling time if the sampling has been finalised"""
    sampler.finalised = True
    sampler.sampling_time = 10
    assert NestedSampler.current_sampling_time.__get__(sampler) == 10


def test_last_updated(sampler):
    """Assert last training iteration is returned"""
    sampler.training_iterations = [10, 20]
    assert NestedSampler.last_updated.__get__(sampler) == 20


def test_last_updated_no_training(sampler):
    """Assert None is return if the flow has not been trained"""
    sampler.training_iterations = []
    assert NestedSampler.last_updated.__get__(sampler) == 0


def test_mean_acceptance(sampler):
    """Assert the mean is returned"""
    sampler.acceptance_history = [1.0, 2.0, 3.0]
    assert NestedSampler.mean_acceptance.__get__(sampler) == 2.0


def test_mean_acceptance_empty(sampler):
    """Assert nan is returned if no points have been proposed"""
    sampler.acceptance_history = deque(maxlen=10)
    assert np.isnan(NestedSampler.mean_acceptance.__get__(sampler))
