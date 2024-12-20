import genesis as gs

# Initialize Genesis with CPU backend
gs.init(backend=gs.cpu)

# Create a scene with viewer and better lighting
scene = gs.Scene(
    show_viewer=True,
    viewer_options=gs.options.ViewerOptions(
        res=(1280, 960),
        camera_pos=(0.5, 0.5, 0.5),
        camera_lookat=(0, 0, 0),
        camera_fov=40,
    ),
    vis_options=gs.options.VisOptions(
        show_world_frame=True,
        plane_reflection=True,
        ambient_light=(0.2, 0.2, 0.2),
    ),
    renderer=gs.renderers.Rasterizer(),
)

# Add a ground plane
plane = scene.add_entity(gs.morphs.Plane())

# Add the wine bottle (assuming you have a wine bottle mesh file)
# Note: You'll need to replace 'path/to/wine_bottle.obj' with your actual mesh file path
bottle = scene.add_entity(
    gs.morphs.Mesh(
        file='path/to/wine_bottle.obj',  # Replace with actual path
        pos=(0, 0, 0),
        euler=(0, 0, 0),
        scale=1.0,
        fixed=True
    )
)

# Add a camera for rendering
camera = scene.add_camera(
    res=(1280, 960),
    pos=(1.0, 1.0, 1.0),
    lookat=(0, 0, 0),
    fov=40,
    GUI=True
)

# Build the scene
scene.build()

# Start camera recording
camera.start_recording()

# Simulate and render for a few frames
import numpy as np
for i in range(120):
    scene.step()
    
    # Rotate camera around the bottle
    camera.set_pose(
        pos=(1.0 * np.sin(i / 30), 1.0 * np.cos(i / 30), 1.0),
        lookat=(0, 0, 0),
    )
    
    camera.render()

# Save the recording
camera.stop_recording(save_to_filename='wine_bottle.mp4', fps=30)
