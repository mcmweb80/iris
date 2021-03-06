# (C) British Crown Copyright 2013, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""Unit tests for :func:`iris.fileformats.pp_rules.convert`."""

# Import iris.tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests

import mock

from iris.fileformats.pp_rules import convert


class TestLBVC(tests.IrisTest):
    def test_soil_levels(self):
        field = mock.MagicMock(lbvc=6, blev=1234)
        (factories, references, standard_name, long_name, units,
         attributes, cell_methods, dim_coords_and_dims,
         aux_coords_and_dims) = convert(field)

        def is_model_level_coord(coord_and_dims):
            coord, dims = coord_and_dims
            return coord.standard_name == 'model_level_number'

        coords_and_dims = filter(is_model_level_coord, aux_coords_and_dims)
        self.assertEqual(len(coords_and_dims), 1)
        coord, dims = coords_and_dims[0]
        self.assertEqual(coord.points, 1234)
        self.assertIsNone(coord.bounds)


if __name__ == "__main__":
    tests.main()
