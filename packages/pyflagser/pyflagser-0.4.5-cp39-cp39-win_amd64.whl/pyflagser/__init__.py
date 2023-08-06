

""""""# start delvewheel patch
def _delvewheel_init_patch_0_0_23():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pyflagser.libs'))
    if sys.version_info[:2] >= (3, 8):
        conda_workaround = os.path.exists(os.path.join(sys.base_prefix, 'conda-meta')) and (sys.version_info[:3] < (3, 8, 13) or (3, 9, 0) <= sys.version_info[:3] < (3, 9, 9))
        if conda_workaround:
            # backup the state of the environment variable CONDA_DLL_SEARCH_MODIFICATION_ENABLE
            conda_dll_search_modification_enable = os.environ.get('CONDA_DLL_SEARCH_MODIFICATION_ENABLE')
            os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = '1'
        os.add_dll_directory(libs_dir)
        if conda_workaround:
            # restore the state of the environment variable CONDA_DLL_SEARCH_MODIFICATION_ENABLE
            if conda_dll_search_modification_enable is None:
                os.environ.pop('CONDA_DLL_SEARCH_MODIFICATION_ENABLE', None)
            else:
                os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = conda_dll_search_modification_enable
    else:
        from ctypes import WinDLL
        with open(os.path.join(libs_dir, '.load-order-pyflagser-0.4.5')) as file:
            load_order = file.read().split()
        for lib in load_order:
            WinDLL(os.path.join(libs_dir, lib))


_delvewheel_init_patch_0_0_23()
del _delvewheel_init_patch_0_0_23
# end delvewheel patch

from ._version import __version__

from .flagio import load_unweighted_flag, load_weighted_flag, \
    save_unweighted_flag, save_weighted_flag
from .flagser import flagser_unweighted, flagser_weighted
from .flagser_count import flagser_count_unweighted, \
    flagser_count_weighted

__all__ = ['load_unweighted_flag',
           'load_weighted_flag',
           'save_unweighted_flag',
           'save_weighted_flag',
           'flagser_unweighted',
           'flagser_weighted',
           'flagser_count_unweighted',
           'flagser_count_weighted',
           '__version__']
