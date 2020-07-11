# this is for the windows only
import os

# updating the kiwi to the latest version
os.system('python -m pip uninstall -y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle')
os.system('python -m pip install --upgrade pip wheel setuptools')
os.system('python -m pip install --upgrade pip wheel setuptools virtualenv')
os.system('''
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy.deps.angle''')
os.system('python -m virtualenv kivy_venv')
os.system('python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*')
os.system('python -m pip install kivy_deps.gstreamer==0.1.*')
os.system('python -m pip install kivy_deps.angle==0.1.*')
os.system('python -m pip install kivy==1.11.1')
os.system('python -m pip install kivy_examples==1.11.1')
os.system('python -m pip install kivy')

# this is very important  this is for python 3.8.x versions
os.system('pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/')