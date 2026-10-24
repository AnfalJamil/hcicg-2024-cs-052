import glfw
from OpenGL.GL import *

if not glfw.init():
    raise SystemExit("GLFW failed to start")

window = glfw.create_window(800, 600, "HCI-CG Lab 01", None, None)
if not window:
    glfw.terminate()
    raise SystemExit("Could not open a window")
glfw.make_context_current(window)

print("GL %s on %s" % (glGetString(GL_VERSION).decode(), glGetString(GL_RENDERER).decode()))

while not glfw.window_should_close(window):
    glClearColor(0.55, 0.10, 0.30, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
