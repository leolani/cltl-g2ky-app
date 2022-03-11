from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read().strip()

setup(
    name='cltl.g2ky-app',
    version=version,
    package_dir={'': 'py-app'},
    packages=find_namespace_packages(include=['*'], where='py-app'),
    data_files=[('VERSION', ['VERSION'])],
    url="https://github.com/leolani/cltl-g2ky-app",
    license='MIT License',
    author='CLTL',
    author_email='t.baier@vu.nl',
    description='VAD for Leolani',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
    install_requires=[
        "cltl.backend[impl,host,service]",
        "cltl.asr[impl,service]",
        "cltl.vad[impl,service]",
        "cltl.cltl.face-recognition[impl,service]",
        "cltl.cltl.g2ky[impl,service]",
        "cltl.chat-ui[impl, service]",
        "flask",
        "werkzeug"
    ],
    entry_points={
        'g2ky': [ 'app:main']
    }
)
