import cadquery as cq
from cadquery.occ_impl.assembly import AssemblyProtocol, toCAF, toVTK, toFusedCAF
from uuid import uuid4
import io
import os

from typing import Optional
if 0:

    from OCP.RWGltf import RWGltf_CafWriter
    from OCP.TCollection import TCollection_ExtendedString, TCollection_AsciiString
    from OCP.TColStd import TColStd_IndexedDataMapOfStringString
    from OCP.Message import Message_ProgressRange

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

def generateShape(length, width,height):
    print("start computation...")
    result = cq.Workplane("front").box(length,width,height)

    assembly = (
        cq.Assembly()
            .add(result, name="result1")
    )

    # Save the GLTF model to a temporary file
    gltf_path = f"/tmp/tmp_{uuid4()}.gltf"
    assembly.save(gltf_path)

    # Read the temporary file into memory
    with open(gltf_path, 'rb') as temp_file:
        in_memory_file = io.BytesIO(temp_file.read())

    # Optionally, delete the temporary file
    #os.remove(gltf_path)

    # At this point, `in_memory_file` contains your GLTF model data in memory
    return in_memory_file

generateShape(1,1,1)