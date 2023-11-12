from setuptools import setup

setup(
   name='bepcar',
   version='0.1',
   author='Alex Zhou',
   author_email='ZYpS_leader@126.com',
   description='A short description of your library',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   url='https://github.com/yourusername/my_library',
   packages=['bepcar'],
   classifiers=[
       'Development Status :: 3 - Alpha',
       'Intended Audience :: Developers',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.6',
       'Programming Language :: Python :: 3.7',
       'Programming Language :: Python :: 3.8',
   ],
   install_requires=[
       'pyotp',
       'rich'
   ],
   python_requires='>=3.2',
);