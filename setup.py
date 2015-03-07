import os
import sys
import json

from setuptools import setup


package_name = 'odm'
package_fullname = 'pulsar-odm'
os.environ['pulsar_odm_setup'] = 'running'
root_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = os.path.join(root_dir, package_name)
odm = __import__(package_name)


def read(fname):
    with open(os.path.join(root_dir, fname)) as f:
        return f.read()


def requirements():
    req = read('requirements.txt').replace('\r', '').split('\n')
    result = []
    for r in req:
        r = r.replace(' ', '')
        if r:
            result.append(r)
    return result


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
def get_rel_dir(d, base, res=''):
    if d == base:
        return res
    br, r = os.path.split(d)
    if res:
        r = os.path.join(r, res)
    return get_rel_dir(br, base, r)

packages, data_files = [], []
pieces = fullsplit(root_dir)
if pieces[-1] == '':
    len_root_dir = len(pieces) - 1
else:
    len_root_dir = len(pieces)

for dirpath, _, filenames in os.walk(package_dir):
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)[len_root_dir:]))
    elif filenames and not dirpath.endswith('__pycache__'):
        rel_dir = get_rel_dir(dirpath, package_dir)
        data_files.extend((os.path.join(rel_dir, f) for f in filenames))


if __name__ == '__main__':

    setup(name=package_fullname,
          version=odm.__version__,
          author=odm.__author__,
          author_email=odm.__contact__,
          url=odm.__homepage__,
          license='BSD',
          description=odm.__doc__,
          long_description=read('README.rst'),
          packages=packages,
          package_dir={package_name: package_name},
          package_data={package_name: data_files},
          install_requires=requirements(),
          classifiers=['Development Status :: 2 - Pre-Alpha',
                       'Environment :: Web Environment',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: BSD License',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3.4',
                       'Topic :: Utilities'])
