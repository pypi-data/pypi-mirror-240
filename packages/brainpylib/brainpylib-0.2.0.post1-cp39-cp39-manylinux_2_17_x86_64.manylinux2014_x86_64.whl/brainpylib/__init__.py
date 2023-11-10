# -*- coding: utf-8 -*-


__version__ = "0.2.0.post1"

__brainpy_minimal_version__ = '2.4.4.post3'
__minimal_taichi_version__ = (1, 7, 0)

import os
import taichi as ti  # noqa

taichi_path = ti.__path__[0]
taichi_c_api_install_dir = os.path.join(taichi_path, '_lib', 'c_api')
os.environ.update({'TAICHI_C_API_INSTALL_DIR': taichi_c_api_install_dir,
                   'TI_LIB_DIR': os.path.join(taichi_c_api_install_dir, 'runtime')})

if ti.__version__ < __minimal_taichi_version__:
    raise RuntimeError(
        f'We need taichi>={__minimal_taichi_version__}. '
        f'Currently you can install taichi>={__minimal_taichi_version__} through taichi-nightly:\n\n'
        '> pip install -i https://pypi.taichi.graphics/simple/ taichi-nightly'
    )

# find brainpylib in the installed package
import pkg_resources
__pkg_lists__ = [i.key for i in pkg_resources.working_set]
__is_brainpylib__ = int('brainpylib' in __pkg_lists__)
__is_brainpylib_cu11x__ = int('brainpylib-cu11x' in __pkg_lists__)
__is_brainpylib_cu12x__ = int('brainpylib-cu12x' in __pkg_lists__)
if __is_brainpylib__ + __is_brainpylib_cu11x__ + __is_brainpylib_cu12x__ > 1:
    raise RuntimeError('You have multiple brainpylib installed, please uninstall them. brainpylib is for CPU verion, '
                       'brainpylib-cu11x is for CUDA 11.x version, brainpylib-cu12x is for CUDA 12.x version.')


def check_brainpy_version():
    import brainpy as bp
    if bp.__version__ < __brainpy_minimal_version__:
        raise RuntimeError(f'brainpylib needs brainpy >= {__brainpy_minimal_version__}, please upgrade it. ')
