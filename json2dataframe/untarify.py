# AUTOGENERATED! DO NOT EDIT! File to edit: 00_untarify.ipynb (unless otherwise specified).

__all__ = ['untar', 'powerup_untar']

# Cell
#export
from pathlib import Path
import concurrent.futures, gzip

# Cell
def untar(source: Path, verbose=False) -> Path:
    """
    Desc: creates a file with the same extension as the
    file contained within the zipped archive and
    then writes the contents from the zipped file
    into the new file created
    Args:
     source - Path object for the source from
              where the files needs to be fetched
     verbose - Let the method know if you want to
               see progress messages
    Returns: Path object for the uncompressed file
    """

    if verbose: print(f'source:{source}')
    dest_file = source.parent/source.stem
    if dest_file.exists(): dest_file.unlink()
    if not dest_file.exists():
        if verbose: print("extracting..")
        dest_file.touch()
        with gzip.open(source, "rb") as file:
            for line in file:
                dest_file.write_bytes(line)
                #dest_file.close()
        if verbose: print('File extracted successfully.')
    return dest_file

def powerup_untar(func):
    """
    Desc: Decorator which endows untar() with superpowers.
          Divides the untar process to multiple cores
    Args: Function to be decorated.
    Returns: Superpowers
    """
    def wrapper(*args):
        source = func(*args)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(untar, source)
    return wrapper