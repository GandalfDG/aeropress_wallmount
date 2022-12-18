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
     chamber_od: float = 10

ap = AeropressMeasurements()

hanger_thickness = 3
inner_hanger_profile = cq.Sketch().circle(ap.chamber_od/2).push([(0,ap.chamber_od/2,0)]).rect(ap.chamber_od,ap.chamber_od)
outer_hanger_profile = cq.Sketch().circle(ap.chamber_od/2+hanger_thickness)

hanger = cq.Workplane("XY").placeSketch(outer_hanger_profile).extrude(1).faces(">Z").placeSketch(inner_hanger_profile).cutThruAll()



# hanger_profile = (cq.Sketch()
#                   .circle()
# )

# hanger = cq.Workplane("XY").placeSketch(inner_hanger_profile).extrude(20)