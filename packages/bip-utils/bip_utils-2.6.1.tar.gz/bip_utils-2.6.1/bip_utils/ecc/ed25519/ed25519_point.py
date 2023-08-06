# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Module for ed25519 point."""

# Imports
from typing import Any

from bip_utils.ecc.common.ipoint import IPoint
from bip_utils.ecc.curve.elliptic_curve_types import EllipticCurveTypes
from bip_utils.ecc.ed25519.lib import ed25519_lib, ed25519_nacl_wrapper
from bip_utils.utils.misc import DataBytes


class Ed25519PointConst:
    """Class container for ed25519 point constants."""

    # Point coordinte length in bytes
    POINT_COORD_BYTE_LEN: int = 32


class Ed25519Point(IPoint):
    """Ed25519 point class."""

    m_point: bytes

    @classmethod
    def FromBytes(cls,
                  point_bytes: bytes) -> IPoint:
        """
        Construct class from point bytes.

        Args:
            point_bytes (bytes): Point bytes

        Returns:
            IPoint: IPoint object
        """
        if len(point_bytes) == Ed25519PointConst.POINT_COORD_BYTE_LEN:
            try:
                ed25519_lib.point_decode(point_bytes)
            except ValueError as ex:
                raise ValueError("Invalid point bytes") from ex
            return cls(point_bytes)
        if len(point_bytes) == Ed25519PointConst.POINT_COORD_BYTE_LEN * 2:
            if not ed25519_lib.point_is_on_curve(ed25519_lib.point_bytes_to_coord(point_bytes)):
                raise ValueError("Invalid point bytes")
            return cls(
                ed25519_lib.point_encode(point_bytes)
            )
        raise ValueError("Invalid point bytes")

    @classmethod
    def FromCoordinates(cls,
                        x: int,
                        y: int) -> IPoint:
        """
        Construct class from point coordinates.

        Args:
            x (int): X coordinate of the point
            y (int): Y coordinate of the point

        Returns:
            IPoint: IPoint object
        """
        return cls.FromBytes(
            ed25519_lib.point_coord_to_bytes((x, y))
        )

    def __init__(self,
                 point_bytes: bytes) -> None:
        """
        Construct class from point object.

        Args:
            point_bytes (bytes): Point bytes
        """
        self.m_point = point_bytes

    @staticmethod
    def CurveType() -> EllipticCurveTypes:
        """
        Get the elliptic curve type.

        Returns:
           EllipticCurveTypes: Elliptic curve type
        """
        return EllipticCurveTypes.ED25519

    def UnderlyingObject(self) -> Any:
        """
        Get the underlying object.

        Returns:
           Any: Underlying object
        """
        return self.m_point

    def X(self) -> int:
        """
        Get point X coordinate.

        Returns:
           int: Point X coordinate
        """
        return ed25519_lib.point_decode_no_check(self.m_point)[0]

    def Y(self) -> int:
        """
        Get point Y coordinate.

        Returns:
           int: Point Y coordinate
        """
        return ed25519_lib.point_decode_no_check(self.m_point)[1]

    def Raw(self) -> DataBytes:
        """
        Return the point encoded to raw bytes.

        Returns:
            DataBytes object: DataBytes object
        """
        return self.RawDecoded()

    def RawEncoded(self) -> DataBytes:
        """
        Return the encoded point raw bytes.

        Returns:
            DataBytes object: DataBytes object
        """
        return DataBytes(self.m_point)

    def RawDecoded(self) -> DataBytes:
        """
        Return the decoded point raw bytes.

        Returns:
            DataBytes object: DataBytes object
        """
        dec = ed25519_lib.point_decode_no_check(self.m_point)
        return DataBytes(ed25519_lib.encode_int(dec[0]) + ed25519_lib.encode_int(dec[1]))

    def __add__(self,
                point: IPoint) -> IPoint:
        """
        Add point to another point.

        Args:
            point (IPoint object): IPoint object

        Returns:
            IPoint object: IPoint object
        """
        return self.__class__(
            ed25519_nacl_wrapper.point_add(self.m_point, point.UnderlyingObject())
        )

    def __radd__(self,
                 point: IPoint) -> IPoint:
        """
        Add point to another point.

        Args:
            point (IPoint object): IPoint object

        Returns:
            IPoint object: IPoint object
        """
        return self + point

    def __mul__(self,
                scalar: int) -> IPoint:
        """
        Multiply point by a scalar.

        Args:
            scalar (int): scalar

        Returns:
            IPoint object: IPoint object
        """
        return self.__class__(
            ed25519_nacl_wrapper.point_mul(scalar, self.m_point)
        )

    def __rmul__(self,
                 scalar: int) -> IPoint:
        """
        Multiply point by a scalar.

        Args:
            scalar (int): scalar

        Returns:
            IPoint object: IPoint object
        """
        return self * scalar
