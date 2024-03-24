from setuptools import find_packages, setup

package_name = 'z4_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='janhajsok',
    maintainer_email='makprdi123@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'brojcanik = z4_pubsub.brojcanik:main',
                'kvadriranje_broja = z4_pubsub.kvadriranje_broja:main'
        ],
    },
)
