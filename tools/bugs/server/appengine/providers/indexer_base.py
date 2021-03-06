# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Base class for Indexer objects.

The choice to add the bug to the function rather than to the object was that
the indexer may be run on many bugs/items/etc so I didn't want the object to
become dependent on the bug it was manipulating.
"""

__author__ = 'jason.stredwick@gmail.com (Jason Stredwick)'


class Error(Exception):
  pass


class IndexerBase(object):
  """Indexer base class

  Indexer are responsible creating search indices for bug from a specific
  provider.
  """

  def __init__(self):
    pass

  def Index(self, bug):
    raise NotImplementedError
