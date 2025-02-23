import argparse
import sys

# from parse_config_file import ParseConfigFile

"""
Handle all switches on the command line.  All info required by this script
loaded into global 'config_params' object.

Input and output dirs are checked for existence.  The output PATH is
built to ensure that the filename's extension is .csv.
"""
def parse_the_args():
    desc="""microelx.py [ Chap01 | Chap02 ]  PATH-to-config.ini

    Example runtime commands:
    (.venvPy3-12-0) C:\\SourceCode\\GitHub\\electronix\\microelec_neamen\\run> python microelx.py Chap01  ..\\config\\chap01\\config_chap01.ini
    """

    parser = argparse.ArgumentParser( prog=desc )
    # Below, dest='command' captures the sub-command supplied on cmd-line to
    # then determine which sub-command class to instantiate.
    # For example, if sub-command == SEARCH, then cl=task_seach.class_search.Search(...).
    subparsers = parser.add_subparsers( dest='command', required=False, help='Specify matcher runtime job' )
    parser_chap01 = subparsers.add_parser( 'Chap01', help='run Chapter 01 problems' )
    parser_chap01.add_argument( 'config_file', help='PATH to config.ini' )
    parser_chap02 = subparsers.add_parser( 'Chap02', help='run Chapter 02 problems' )
    parser_chap02.add_argument( 'config_file', help='PATH to config.ini' )
    parser_chap77 = subparsers.add_parser( 'Chap77', help='run Chapter XX problems' )
    parser_chap77.add_argument( 'config_file', help='PATH to config.ini' )

    # The REST
    parser.add_argument( "-p", "--pr", help="OPTION: print config.ini contents" )

    # let each "task" have its own version number
    parser.add_argument( "-v", "--version", help="print TASKS version and exit", action='store_true' )

    # No switches, not even -h
    if len( sys.argv ) == 1:
      parser.print_help( sys.stderr )
      sys.exit(1)

    global args
    args = parser.parse_args()
    # print( f"args cmd line: {args}" )
    # print( f"args sub-cmd: {args.command}" )
    # print( f"SEARCH cmd line: " )

    # Tend the optional switches
    if( args.pr ):
      # pcf = ParseConfigFile( args.pr )
      # pcf.print_all_config_parameters()
      sys.exit(1)

    if (args.version):
      print( f"Chap01 v0.1.0" )
      sys.exit(1)

    global chapter_subcmd
    chapter_subcmd = args.command
    global path_to_config_file
    path_to_config_file = args.config_file
