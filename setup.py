import ssh_tunnel
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='sshtunnel',
    version=ssh_tunnel.__version__,
    packages=find_packages(),
    license='LICENSE',
    author='Bruno Silva',
    author_email='brunomiguelsilva@ua.pt',
    description='Library to create ssh remote tunnels',
    keywords=['ssh', 'remote', 'tunnel'],
    url='https://github.com/bsilvr/python-ssh-tunnel',
    # include_package_data=True,
    download_url='https://github.com/bsilvr/python-ssh-tunnel/tarball/' + ssh_tunnel.__version__,
)
