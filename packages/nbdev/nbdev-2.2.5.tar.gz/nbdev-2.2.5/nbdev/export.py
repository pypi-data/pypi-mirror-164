# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04a_export.ipynb.

# %% auto 0
__all__ = ['ExportModuleProc', 'black_format', 'create_modules', 'nb_export']

# %% ../nbs/04a_export.ipynb 2
from .config import *
from .maker import *
from .imports import *
from .process import *

from fastcore.script import *
from fastcore.basics import *
from fastcore.imports import *

from collections import defaultdict

# %% ../nbs/04a_export.ipynb 4
class ExportModuleProc:
    "A processor which exports code to a module"
    def begin(self): self.modules,self.in_all = defaultdict(L),defaultdict(L)
    def _default_exp_(self, cell, exp_to): self.default_exp = exp_to
    def _exporti_(self, cell, exp_to=None): self.modules[ifnone(exp_to, '#')].append(cell)
    def _export_(self, cell, exp_to=None):
        self._exporti_(cell, exp_to)
        self.in_all[ifnone(exp_to, '#')].append(cell)
    _exports_=_export_

# %% ../nbs/04a_export.ipynb 7
def black_format(cell, # Cell to format
                 force=False): # Turn black formatting on regardless of settings.ini
    "Processor to format code with `black`"
    try: cfg = get_config()
    except FileNotFoundError: return
    if (str(cfg.get('black_formatting')).lower() != 'true' and not force) or cell.cell_type != 'code': return
    try: import black
    except: raise ImportError("You must install black: `pip install black` if you wish to use black formatting with nbdev")
    else:
        _format_str = partial(black.format_str, mode = black.Mode())
        try: cell.source = _format_str(cell.source).strip()
        except: pass

# %% ../nbs/04a_export.ipynb 9
def create_modules(path, dest, procs=None, debug=False, mod_maker=ModuleMaker):
    "Create module(s) from notebook"
    exp = ExportModuleProc()
    nb = NBProcessor(path, [exp]+L(procs), debug=debug)
    nb.process()
    for mod,cells in exp.modules.items():
        all_cells = exp.in_all[mod]
        name = getattr(exp, 'default_exp', None) if mod=='#' else mod
        if not name:
            warn(f"Notebook '{path}' uses `#|export` without `#|default_exp` cell.\n"
                 "Note nbdev2 no longer supports nbdev1 syntax. Run `nbdev_migrate` to upgrade.\n"
                 "See https://nbdev.fast.ai/getting_started.html for more information.")
            return
        mm = mod_maker(dest=dest, name=name, nb_path=path, is_new=mod=='#')
        mm.make(cells, all_cells, lib_path=dest)

# %% ../nbs/04a_export.ipynb 16
def nb_export(nbname, lib_path=None):
    if lib_path is None: lib_path = get_config().path('lib_path')
    create_modules(nbname, lib_path, procs=[black_format])
