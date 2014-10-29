#
# Copyright 2014 Red Hat. All Rights Reserved.
#
# Author: Chris Dent <chdent@redhat.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os

from gabbi.driver import build_tests


TESTS_DIR = 'gabbits'


def load_tests(loader, tests, pattern):
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    return build_tests(test_dir, loader, tests, pattern)
