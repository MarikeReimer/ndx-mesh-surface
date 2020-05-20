# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec
# TODO: import the following spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""Add group to PlaneSegmentation for faces and vertices of mesh""",
        name="""ndx-mesh-surface""",
        version="""0.1.0""",
        author=list(map(str.strip, """Marike Reimer""".split(','))),
        contact=list(map(str.strip, """marike.reimer@yale.edu""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types
    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('PlaneSegmentation', namespace='core')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information

    #Mesh surface(Directly repurposed from CorticalSurfaces)
    mesh_surface = NWBGroupSpec(doc='Vertices and faces which define a 3D mesh surface',
                        datasets=[
                            NWBDatasetSpec(doc='faces for surface, indexes vertices', shape=(None, 3),
                                            name='faces', dtype='uint', dims=('face_number', 'vertex_index')),
                            NWBDatasetSpec(doc='vertices for surface, points in 3D space', shape=(None, 3),
                                            name='vertices', dtype='float', dims=('vertex_number', 'xyz'))],
                        neurodata_type_def='MeshSurface',
                        neurodata_type_inc='NWBDataInterface')


    #Extend PlaneSegmentation to add a group for mesh_surface
    mesh_plane_segmentation = NWBGroupSpec('A PlaneSegmentation that stores mesh surface data',
                                neurodata_type_inc='PlaneSegmentation',
                                neurodata_type_def='MeshPlaneSegmentation',
                                groups = [mesh_surface])
                            
    # TODO: add all of your new data types to this list
    new_data_types = [mesh_plane_segmentation]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
