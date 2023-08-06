# mne-icalabel

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Codecov](https://codecov.io/gh/mne-tools/mne-icalabel/branch/main/graph/badge.svg)](https://codecov.io/gh/mne-tools/mne-icalabel)
[![unit-tests](https://github.com/mne-tools/mne-icalabel/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/mne-tools/mne-icalabel/actions/workflows/unit_tests.yml)
[![CircleCI](https://circleci.com/gh/mne-tools/mne-icalabel/tree/main.svg?style=svg)](https://circleci.com/gh/mne-tools/mne-icalabel/tree/main)
[![PyPI Download count](https://pepy.tech/badge/mne-icalabel)](https://pepy.tech/project/mne-icalabel)
[![Latest PyPI release](https://img.shields.io/pypi/v/mne-icalabel.svg)](https://pypi.org/project/mne-icalabel/)
[![Latest conda-forge release](https://img.shields.io/conda/vn/conda-forge/mne-icalabel.svg)](https://anaconda.org/conda-forge/mne-icalabel/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![status](https://joss.theoj.org/papers/d91770e35a985ecda4f2e1f124977207/status.svg)](https://joss.theoj.org/papers/d91770e35a985ecda4f2e1f124977207)

This repository is a conversion of the popular Matlab-based
[ICLabel](https://github.com/sccn/ICLabel) classifier for Python.
In addition, `mne-icalabel` provides extensions and improvements in the form of other models.

# Why?

EEG and MEG recordings include artifacts, such as heartbeat, eyeblink, muscle, and movement activity.
Independent component analysis (ICA) is a common method to remove artifacts, but typically relies on manual
annotations labelling which independent components (IC) reflect noise and which reflect brain activity.

This package aims at automating this process, using the popular MNE-Python API for EEG, MEG and iEEG data.

# Basic Usage

MNE-ICALabel estimates the labels of ICA components given
a MNE-Python [Raw](https://mne.tools/stable/generated/mne.io.Raw.html) or
[Epochs](https://mne.tools/stable/generated/mne.Epochs.html) object and an ICA instance using the
[ICA decomposition](https://mne.tools/stable/generated/mne.preprocessing.ICA.html)
available in MNE-Python.

```
from mne_icalabel import label_components

# assuming you have a Raw and ICA instance previously fitted
label_components(raw, ica, method='iclabel')
```

The only current available method is `'iclabel'`.

# Documentation

[Stable version](https://mne.tools/mne-icalabel/stable/index.html) documentation.
[Dev version](https://mne.tools/mne-icalabel/dev/index.html) documentation.

# Installation

The current stable release of `mne-icalabel` can be installed with pip, for example, by running:

    pip install mne-icalabel

For further details about installation, see the
[install](https://mne.tools/mne-icalabel/stable/install.html) page.

To get the latest (development) version, using [git](https://git-scm.com/), open a terminal and type:

    git clone git://github.com/mne-tools/mne-icalabel.git
    cd mne-icalabel
    pip install -e .

The development version can also be installed directly using pip:

    pip install https://api.github.com/repos/mne-tools/mne-icalabel/zipball/main

Alternatively, you can also download a
[zip file of the latest development version](https://github.com/mne-tools/mne-icalabel/archive/main.zip).

# Contributing

If you are interested in contributing, please read the
[contributing guidelines](https://github.com/mne-tools/mne-icalabel/blob/main/CONTRIBUTING.md).

# Getting Help

[<img alt="MNE Forum" src="https://user-images.githubusercontent.com/1681963/52239617-e2683480-289c-11e9-922b-5da55472e5b4.png" height=60/>](https://mne.discourse.group)

For any usage questions, please post to the
[MNE Forum](https://mne.discourse.group). Be sure to add the `mne-icalabel` tag to
your question.
