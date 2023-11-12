# Copyright Louis Paternault 2014-2023

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Convert PDF files to 'n-up' PDF files, guessing the output layout."""

import logging

VERSION = "1.8.1"
__AUTHOR__ = "Louis Paternault (spalax@gresille.org)"
__COPYRIGHT__ = "(C) 2014-2023 Louis Paternault. GNU AGPL 3 or later."

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
