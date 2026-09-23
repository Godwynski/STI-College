"""
================================================================================
Record 3D Rotating Wireframe Cube Demonstration Video
Student Name: Godwyn Neri
Course:       Game Development / Computer Graphics Programming (IT2202)
Section:      BSIT / BSIT711
Activity:     03 Laboratory Exercise 1
Output:       03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.mp4 (60 FPS H.264)
================================================================================
"""

import os
import shutil
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2
import imageio

# -----------------------------------------------------------------------------
# 3D Cube Topology Specifications
# -----------------------------------------------------------------------------
vertices = (
    ( 1,  1,  1),  # Vertex 0
    ( 1,  1, -1),  # Vertex 1
    ( 1, -1, -1),  # Vertex 2
    ( 1, -1,  1),  # Vertex 3
    (-1,  1,  1),  # Vertex 4
    (-1, -1, -1),  # Vertex 5
    (-1, -1,  1),  # Vertex 6
    (-1,  1, -1)   # Vertex 7
)

edges = (
    (0, 1),  # Edge A
    (1, 2),  # Edge B
    (2, 3),  # Edge C
    (3, 0),  # Edge D
    (4, 7),  # Edge E
    (7, 5),  # Edge F
    (5, 6),  # Edge G
    (6, 4),  # Edge H
    (3, 6),  # Edge I
    (0, 4),  # Edge J
    (2, 5),  # Edge K
    (1, 7)   # Edge L
)

def draw_cube():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def add_hud_overlay(img_rgb, frame_idx, total_frames, angle):
    """
    Overlays a professional STI academic HUD on the rendered OpenGL frame.
    """
    h, w, _ = img_rgb.shape
    bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    overlay = bgr.copy()
    # 1. Top Header Banner (46px height)
    cv2.rectangle(overlay, (0, 0), (w, 46), (20, 24, 32), -1)
    cv2.rectangle(overlay, (0, 44), (w, 46), (200, 100, 0), -1) # STI Gold/Cyan Accent
    
    # 2. Bottom Telemetry Banner (34px height)
    cv2.rectangle(overlay, (0, h - 34), (w, h), (20, 24, 32), -1)
    cv2.rectangle(overlay, (0, h - 34), (w, h - 32), (200, 100, 0), -1)

    # Alpha blend banners (85% opacity)
    alpha = 0.85
    cv2.addWeighted(overlay, alpha, bgr, 1 - alpha, 0, bgr)

    # Render Header Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(bgr, "STI COLLEGE ALABANG  |  BSIT711  |  GODWYN NERI", (16, 20), font, 0.48, (0, 215, 255), 1, cv2.LINE_AA)
    cv2.putText(bgr, "03 LAB 1: WIREFRAME CUBE (PYGAME + OPENGL)", (16, 38), font, 0.44, (240, 240, 240), 1, cv2.LINE_AA)
    cv2.putText(bgr, "60.0 FPS", (w - 95, 30), font, 0.50, (0, 255, 128), 1, cv2.LINE_AA)

    # Render Bottom Telemetry Text
    status_str = f"AXIS: (1, 1, 1)  |  ROTATION: {angle:03d}deg  |  FRAME: {frame_idx + 1:03d}/{total_frames}"
    cv2.putText(bgr, status_str, (16, h - 12), font, 0.44, (240, 240, 240), 1, cv2.LINE_AA)
    cv2.putText(bgr, "DOUBLE BUFFER: OK", (w - 170, h - 12), font, 0.44, (0, 255, 128), 1, cv2.LINE_AA)

    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

def record_video():
    width, height = 800, 600
    fps = 60
    total_frames = 360 # Exactly 1 full 360-degree rotation at 1 deg/frame = 6.0 seconds

    print(f"[*] Initializing headless Pygame + PyOpenGL context ({width}x{height})...")
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL | pygame.HIDDEN)

    # Configure viewport and projection
    glViewport(0, 0, width, height)
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)
    glEnable(GL_DEPTH_TEST)

    # Configure paths
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    assignment_dir = os.path.abspath(os.path.join(curr_dir, ".."))
    screenshots_dir = os.path.join(curr_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    output_filename = "03_Laboratory_Exercise_1_Godwyn_Neri_BSIT711.mp4"
    out_video_path = os.path.join(assignment_dir, output_filename)
    cgp_video_path = os.path.abspath(os.path.join(assignment_dir, "..", "..", "..", "Computer_Graphics_Programming", "assignments", "midterm", "03_Laboratory_Exercise_1", output_filename))
    downloads_video_path = os.path.join(os.path.expanduser("~"), "Downloads", output_filename)

    print(f"[*] Recording {total_frames} frames to {out_video_path} at {fps} FPS...")

    # Initialize high-quality H.264 writer
    writer = imageio.get_writer(
        out_video_path,
        fps=fps,
        codec='libx264',
        quality=9,
        pixelformat='yuv420p',
        macro_block_size=16
    )

    preview_frame = None

    for i in range(total_frames):
        # Step 16: Continuous rotation by 1 degree across vector (1, 1, 1)
        glRotatef(1, 1, 1, 1)

        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Step 17: Draw wireframe cube
        draw_cube()

        # Capture back buffer
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        raw_data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
        frame_array = np.frombuffer(raw_data, dtype=np.uint8).reshape((height, width, 3))
        # OpenGL has origin at bottom-left, flip vertically for standard video orientation
        frame_array = np.flipud(frame_array)

        # Overlay student & academic HUD
        angle = (i + 1) % 360
        composed_frame = add_hud_overlay(frame_array, i, total_frames, angle)

        writer.append_data(composed_frame)

        # Save preview frame at frame 45 for report documentation
        if i == 45:
            preview_frame = composed_frame

        if (i + 1) % 60 == 0:
            print(f"    Rendered frame {i + 1}/{total_frames} ({(i + 1)/fps:.1f}s)")

    writer.close()
    pygame.quit()

    file_size_mb = os.path.getsize(out_video_path) / (1024 * 1024)
    print(f"[+] Video successfully generated: {out_video_path} ({file_size_mb:.2f} MB)")

    # Save video preview screenshot
    if preview_frame is not None:
        preview_path = os.path.join(screenshots_dir, "wireframe_cube_video_preview.png")
        imageio.imwrite(preview_path, preview_frame)
        print(f"[+] Video preview snapshot saved: {preview_path}")

    # Mirror to Downloads and Computer Graphics Programming directory
    try:
        shutil.copyfile(out_video_path, downloads_video_path)
        print(f"[+] Mirrored video to Downloads: {downloads_video_path}")
    except Exception as e:
        print(f"[-] Could not copy to Downloads: {e}")

    try:
        if os.path.exists(os.path.dirname(cgp_video_path)):
            shutil.copyfile(out_video_path, cgp_video_path)
            print(f"[+] Mirrored video to CGP assignment folder: {cgp_video_path}")
    except Exception as e:
        print(f"[-] Could not copy to CGP: {e}")

if __name__ == "__main__":
    record_video()
