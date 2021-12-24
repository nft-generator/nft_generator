#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_nft_generator
----------------------------------

Tests for `nft_generator` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from nft_generator import cli


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    #assert 'nft_generator.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    #assert '--help  Show this message and exit.' in help_result.output
