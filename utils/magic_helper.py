from IPython.core.magic import register_cell_magic
from IPython.core.interactiveshell import InteractiveShell

@register_cell_magic
def save_and_run(filename, cell):
    cell = cell.strip()
    with open(filename, 'w') as f:
        f.write(cell)
        
    shell = InteractiveShell()
    shell.run_cell(cell)

