# !/usr/bin/python
# coding=utf-8
try:
    import pymel.core as pm
except ImportError as error:
    print(__file__, error)
# from this package:
from mayatk import core_utils


class EditUtils:
    @staticmethod
    @core_utils.CoreUtils.undo
    def show_scene_elements(
        elements="geometry", include_ancestors=True, affect_layers=True
    ):
        """
        Shows specific elements in the Maya scene by setting their visibility to True.
        It can also optionally affect the visibility of layers and ancestor nodes.

        Parameters:
        elements (str): The type of elements to show. Default is 'geometry'.
                        Other possible types include 'nurbsCurves', 'nurbsSurfaces', 'lights', etc.
        include_ancestors (bool): If True, will also show all ancestor transform nodes of the elements.
        affect_layers (bool): If True, will ensure that all layers except the default layer are visible.

        Usage:
        show_scene_elements('geometry')  # Shows all geometry and their ancestors, affects layers.
        show_scene_elements('lights', include_ancestors=False)  # Shows all lights without affecting their ancestors.
        show_scene_elements('nurbsCurves', affect_layers=False)  # Shows all nurbsCurves, doesn't affect layers.
        """
        if affect_layers:
            # Show all layers except the default layer
            for layer in pm.ls(type="displayLayer"):
                if layer.name() != "defaultLayer" and not layer.isReferenced():
                    try:
                        layer.visibility.set(True)
                    except pm.MayaAttributeError:
                        pass  # Skip the layer if visibility cannot be set

        # Show all elements of the specified type
        scene_elements = pm.ls(type=elements)
        for element in scene_elements:
            if include_ancestors:
                # Make ancestor transform nodes visible
                ancestors = [
                    ancestor
                    for ancestor in element.getAllParents()
                    if isinstance(ancestor, pm.nt.Transform)
                ]
                for ancestor in ancestors:
                    try:
                        ancestor.visibility.set(True)
                    except pm.MayaAttributeError:
                        pass  # Skip the ancestor if visibility cannot be set

            # Set the visibility of the element
            try:
                element.visibility.set(True)
            except pm.MayaAttributeError:
                pass  # Skip the element if visibility cannot be set


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    pass

# -----------------------------------------------------------------------------
# Notes
# -----------------------------------------------------------------------------
