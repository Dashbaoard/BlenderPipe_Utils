#blender remove utils

#apply all modifiers
import bpy

def apply_modifiers(obj):
    ctx = bpy.context.copy()
    ctx['object'] = obj
    for _, m in enumerate(obj.modifiers):
        try:
            ctx['modifier'] = m
            bpy.ops.object.modifier_apply(ctx, modifier=m.name)
        except RuntimeError:
            print(f"Error applying {m.name} to {obj.name}, removing it instead.")
            obj.modifiers.remove(m)

    for m in obj.modifiers:
        obj.modifiers.remove(m)
        

# apply modifiers on every object in your scene
for o in bpy.data.objects:
    apply_modifiers(o)

#delete all vertex groups


# Get a list of all objects in the scene
all_objects = bpy.data.objects

# Loop through each object
for obj in all_objects:
    if obj.type == 'MESH':
        # Check if the object has vertex groups
        if obj.vertex_groups:
            # Delete all vertex groups for the object
            for group in obj.vertex_groups:
                obj.vertex_groups.remove(group)

#delete the armature
# Select the armature you want to delete
armature = bpy.data.objects["Armature"]

# Set the context to the armature
bpy.context.view_layer.objects.active = armature

# Apply location, rotation, and scale transforms
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Delete the armature
bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
armature.select_set(True)  # Select the armature
bpy.ops.object.delete()