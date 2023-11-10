"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

from geometry import GPS, Coord, Point, Transformation, PX, PY, PZ, P0, Euler
import numpy as np
from json import load, dump
from flightdata import Flight
from typing import Self

class Box(object):
    '''This class defines an aerobatic box in the world, it uses the pilot position and the direction 
    in which the pilot is facing (normal to the main aerobatic manoeuvering plane)'''

    def __init__(self, name, pilot_position: GPS, heading: float):
        self.name = name
        self.pilot_position = pilot_position # position of pilot
        self.heading = heading  # direction pilot faces in radians from North (clockwise)
        self.rotation = Euler(0, 0, -self.heading)

    def to_dict(self) -> dict:
        temp = self.__dict__.copy()
        temp["pilot_position"] = self.pilot_position.to_dict()
        return temp

    @staticmethod
    def from_dict(data: dict) -> Self:
        return Box(
            data['name'], 
            GPS(**data['pilot_position']), 
            data['heading']
        )

    @staticmethod
    def from_json(file):
        if hasattr(file, 'read'):
            data = load(file)
        else:
            with open(file, 'r') as f:
                data = load(f)
        return Box.from_dict(data)

    def to_json(self, file):
        with open(file, 'w') as f:
            dump(self.to_dict(), f)
        return file

    def __str__(self):
        return "Box:{}".format(self.to_dict())

    def __repr__(self):
        return f'Box(heading={np.degrees(self.heading)},pos={self.pilot_position})'

    @staticmethod
    def from_initial(flight: Flight):
        '''Generate a box based on the initial position and heading of the model at the start of the log. 
        This is a convenient, but not very accurate way to setup the box. 
        '''
        
        position = GPS(flight.gps_latitude[0], flight.gps_longitude[0], flight.gps_altitude[0])
        heading = Euler(flight.attitude)[0].transform_point(PX())

        return Box('origin', position, np.arctan2(heading.y, heading.x)[0])

    @staticmethod
    def from_points(name, pilot: GPS, centre: GPS):
        direction = centre - pilot
        return Box(
            name,
            pilot,
            np.arctan2(direction.y[0], direction.x[0])
        )

    def to_f3a_zone(self):
        
        centre = self.pilot_position.offset(
            100 * Point(np.cos(self.heading), np.sin(self.heading), 0.0)
        )

        oformat = lambda val: "{}".format(val)

        return "\n".join([
            "Emailed box data for F3A Zone Pro - please DON'T modify!",
            self.name,
            oformat(self.pilot_position.lat[0]),
            oformat(self.pilot_position.long[0]),
            oformat(centre.lat[0]),
            oformat(centre.long[0]),
            "120"
        ])


    @staticmethod
    def from_f3a_zone(file_path: str):
        if hasattr(file_path, "read"):
            lines = file_path.read().splitlines()
        else:
            with open(file_path, "r") as f:
                lines = f.read().splitlines()
        return Box.from_points(
            lines[1],
            GPS(float(lines[2]), float(lines[3]), 0),
            GPS(float(lines[4]), float(lines[5]), 0)
        )

    @staticmethod
    def from_fcjson_parmameters(data: dict):
        return Box.from_points(
            "FCJ_box",
            GPS(float(data['pilotLat']), float(data['pilotLng']), 0),
            GPS(float(data['centerLat']), float(data['centerLng']), 0)
        )


    def gps_to_point(self, gps: GPS) -> Point:
        pned = gps - self.pilot_position
        return self.rotation.transform_point(Point(pned.y, pned.x, -pned.z ))

    
