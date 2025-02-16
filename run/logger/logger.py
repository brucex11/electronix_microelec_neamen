import logging
import os
import pathlib

def build_logger( pcf, opera:str ) -> logging.Logger:
	# build log-file subdir
	subdir_to_log_file = os.path.join(
		pcf.get_config_params['common']['logger_root_dir'],
		pcf.get_config_params['common']['project_title'],
		opera
	)
	# print( f"SUBDIR TO LOGGER: {subdir_to_log_file}" )
	pathlib.Path( subdir_to_log_file ).mkdir( parents=True, exist_ok=True )
	# path_to_log_file:str = os.path.join(
	# 	subdir_to_log_file,
	# 	pcf.get_config_params['common']['logger_fname'] )
	# print( f"PATH TO LOGGER: {path_to_log_file}" )

	# Configure the logging, build the path
	ftmp1:str = pcf.get_config_params['common']['logger_fname']
	ftmp2:str = ftmp1.replace( 'PROJ', pcf.get_config_params['common']['project_title'] )
	ftmp3:str = ftmp2.replace( 'OPERA', opera )
	fname:str = ftmp3.replace( 'TASK', pcf.get_config_params['common']['problem_num'] )
	path_to_log_file:str = os.path.join( subdir_to_log_file, fname )
	logging.basicConfig(
		filename=path_to_log_file,  # Log file name
		filemode='a',  # Write mode ('w' for overwrite, 'a' for append)
		level=logging.DEBUG,  # Set the minimum level of messages to capture
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
	)
	lg = logging.getLogger( opera )
	# print( f"type(lg): {type(lg)}" )
	lg.info( f"---- START {pcf.get_config_params['common']['problem_num']} ----" )
	lg.info( f"PATH to this log file: '{path_to_log_file}'" )
	# lg.info( f"PATH to config file: '{path_to_config_file}'" )
	# lg.info( f"src_nfract_xml_files: '{pcf.get_config_params['copyfiles']['src_nfract_xml_files']}'" )
	# lg.info( f"xml_copy_subdir: '{pcf.get_config_params['copyfiles']['xml_copy_subdir']}'" )

	return lg
