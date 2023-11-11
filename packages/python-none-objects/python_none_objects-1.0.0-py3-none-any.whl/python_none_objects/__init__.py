"""
This file is part of python-none-objects library.

python-none-objects is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python-none-objects is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with python-none-objects.
If not, see <http://www.gnu.org/licenses/>.

©Copyright 2023 Laurent Lyaudet
"""
# from typing import Iterable, Container, Collection, Mapping
from types import MappingProxyType

NoneIterable = ()
NoneContainer = NoneIterable
NoneCollection = NoneIterable
NoneMapping = MappingProxyType({})
