import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BespokeFurnitures.settings')
django.setup()
from django.conf import settings

from uuid import uuid4
import io
import os

import cadquery as cq
from cadquery.occ_impl.assembly import toCAF

from math import cos,sin,pi

if 0:

    def exportGLTF(
            assy,
            path: str,
            binary: Optional[bool] = None,
            tolerance: float = 1e-3,
            angularTolerance: float = 0.1,
    ):

        # If the caller specified the binary option, respect it
        if binary is None:
            # Handle the binary option for GLTF export based on file extension
            binary = True
            path_parts = path.split(".")

            # Binary will be the default if the user specified a non-standard file extension
            if len(path_parts) > 0 and path_parts[-1] == "gltf":
                binary = False

        # map from CadQuery's right-handed +Z up coordinate system to glTF's right-handed +Y up coordinate system
        # https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#coordinate-system-and-units
        orig_loc = assy.loc
        assy.loc *= cq.Location((0, 0, 0), (1, 0, 0), -90)

        _, doc = toCAF(assy, True, True, tolerance, angularTolerance)
        return doc

        """writer = RWGltf_CafWriter(TCollection_AsciiString(path), binary)
        result = writer.Perform(
            doc, TColStd_IndexedDataMapOfStringString(), Message_ProgressRange()
        )
    
        # restore coordinate system after exporting
        assy.loc = orig_loc
        return result"""

def CAD1(l1,l2,l3):
    def surface(t1, t2):
        R = 10
        t2_2 = (t2 - 1 / 2) * 2 * pi
        x = l1 * cos(t1 * 1 * pi) * cos(t2_2)
        y = l2 * sin(t1 * 1 * pi) * cos(t2_2)
        z = l3 * sin(t2_2)
        return (x, y, z)

    res = cq.Workplane().parametricSurface(surface, N=8)

    return res

def generateShape(length, width,height):
    print("start computation...",end="")
    """result = cq.Workplane("front").box(length,width,height)"""
    result = CAD1(length,width,height)
    assembly = (
        cq.Assembly()
        .add(result, name="result1"))

    # Save the GLTF model to a temporary file
    filename = f"tmp_{uuid4()}.gltf"
    gltf_path_MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, filename)
    gltf_path_MEDIA_URL = os.path.join(settings.MEDIA_URL, filename)

    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

    assembly.save(gltf_path_MEDIA_ROOT)

    print(gltf_path_MEDIA_ROOT)
    print(gltf_path_MEDIA_URL)
    print("saved(?).")
    return_and_delete_file = False
    if return_and_delete_file:
        # Read the temporary file into memory
        with open(gltf_path, 'rb') as temp_file:
            in_memory_file = io.BytesIO(temp_file.read())

        # Optionally, delete the temporary file
        #os.remove(gltf_path)

        # At this point, `in_memory_file` contains your GLTF model data in memory
        return in_memory_file
    else:
        return filename


if __name__ == "__main__":
    generateShape(1,1,1)