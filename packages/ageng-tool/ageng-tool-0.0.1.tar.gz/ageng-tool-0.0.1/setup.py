import os
from setuptools import setup, find_packages


path = os.path.abspath(os.path.dirname(__file__))

try:
  with open(os.path.join(path, 'README.md')) as f:
    long_description = f.read()
except Exception as e:
  long_description = "find tar pic"

setup(
    name = "ageng-tool",
    version = "0.0.1",
    keywords = ("pip", "picdiff"),
    description = "ageng tool",
    long_description = long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.5.0",
    license = "MIT Licence",

    url = "https://gitlab.com/wangjin199410/ageng_tool/-/blob/main/my_tool.py",
    author = "wangjin",
    author_email = "631813797@qq.com",

    packages = find_packages(),
    include_package_data = True,
    install_requires = ["cv2", "numpy"],
    platforms = "any",

    scripts = []
)