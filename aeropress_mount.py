from dataclasses import dataclass
import cadquery as cq


mounting_strip_width = 15.8
mounting_strip_height = 46.8

base_thickness = 3

# command_mount = (cq.Workplane("XZ")
#                  .box(mounting_strip_width,
#                       mounting_strip_height,
#                       base_thickness)
#                  .edges("|Y").fillet(2).faces(">Y").fillet(.5))

@dataclass
class AeropressMeasurements():
     chamber_od: float = 63.45
     octagon_width = 97.05
     chamber_to_octagon = 16.45

     @property
     def chamber_radius(self):
          return self.chamber_od/2


ap = AeropressMeasurements()

hanger_thickness = 10
hanger_depth = ap.octagon_width

outer_hanger_profile = cq.Sketch().circle(ap.chamber_od/2+hanger_thickness).push(
    [(0, -hanger_depth/2, 0)]).rect(ap.chamber_od + hanger_thickness * 2, hanger_depth)
hanger_sketch = outer_hanger_profile.reset().circle(ap.chamber_radius, mode='s').push(
    [(0, -hanger_depth/2, 0)]).rect(ap.chamber_od, hanger_depth, mode='s')

# round the ends
endpoints = [(ap.chamber_radius+hanger_thickness/2, -hanger_depth, 0),(-(ap.chamber_radius+hanger_thickness/2), -hanger_depth, 0)]
hanger_sketch = hanger_sketch.push(endpoints).circle(hanger_thickness/2)
hanger = cq.Workplane("XY").placeSketch(hanger_sketch).extrude(10).faces(">Z").workplane().pushPoints(endpoints).sphere(hanger_thickness/2)






# hanger_profile = (cq.Sketch()
#                   .circle()
# )

