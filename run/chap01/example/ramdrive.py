"""
To reduce fixed-disk read/write for development, create RAMDRIVE environment
in which to run.
"""
from inspect import currentframe
from os import path
from pathlib import Path
import shutil


print( f"START" )
fcn_name:str = currentframe().f_code.co_name
print( f"ENTRYPOINT: Module: '{__name__}'; function: '{fcn_name}'" )

ramdrive_root:str = 'r:/micro'

# ---- config.ini ------------------------------------------------------------
config_dir:str = 'config/chap01/example'
dest_dir:str = path.join( ramdrive_root, config_dir )
Path( dest_dir ).mkdir( parents=True, exist_ok=True)

fname_to_copy:str = 'config_example__01-10.ini'
path_src_file:str = f"../../../config/chap01/example/{fname_to_copy}"
path_dest_file:str = path.join( ramdrive_root, config_dir, fname_to_copy )
shutil.copy( path_src_file, path_dest_file )

# ---- src.py ------------------------------------------------------------
src_file_dir:str = 'run/chap01/example'
dest_dir:str = path.join( ramdrive_root, src_file_dir )
Path( dest_dir ).mkdir( parents=True, exist_ok=True)

fname_to_copy:str = 'exam1_XX.py'
path_src_file:str = f"{fname_to_copy}"
path_dest_file:str = path.join( ramdrive_root, src_file_dir, fname_to_copy )
shutil.copy( path_src_file, path_dest_file )

# ---- class_chapXX.py -------------------------------------------------------
src_file_dir:str = 'run/chap01'
dest_dir:str = path.join( ramdrive_root, src_file_dir )

fname_to_copy:str = 'class_chap01.py'
path_src_file:str = f"../{fname_to_copy}"
path_dest_file:str = path.join( ramdrive_root, src_file_dir, fname_to_copy )
shutil.copy( path_src_file, path_dest_file )

# ---- ./run/ files -------------------------------------------------------
src_file_dir:str = 'run'
dest_dir:str = path.join( ramdrive_root, src_file_dir )

list_fname_to_copy = [ 'microelx.py', 'parse_cmd_line.py', 'parse_config_file.py' ]
for fname_to_cpy in list_fname_to_copy:
	path_src_file:str = f"../../{fname_to_cpy}"
	path_dest_file:str = path.join( ramdrive_root, src_file_dir, fname_to_cpy )
	shutil.copy( path_src_file, path_dest_file )

# ---- assertions -------------------------------------------------------
src_file_dir:str = 'run/assertions'
dest_dir:str = path.join( ramdrive_root, src_file_dir )
Path( dest_dir ).mkdir( parents=True, exist_ok=True)

fname_to_copy:str = 'assertions.py'
path_src_file:str = f"../../assertions/{fname_to_copy}"
path_dest_file:str = path.join( ramdrive_root, src_file_dir, fname_to_copy )
shutil.copy( path_src_file, path_dest_file )

# ---- logger -------------------------------------------------------
src_file_dir:str = 'run/logger'
dest_dir:str = path.join( ramdrive_root, src_file_dir )
Path( dest_dir ).mkdir( parents=True, exist_ok=True)

fname_to_copy:str = 'logger.py'
path_src_file:str = f"../../logger/{fname_to_copy}"
path_dest_file:str = path.join( ramdrive_root, src_file_dir, fname_to_copy )
shutil.copy( path_src_file, path_dest_file )
