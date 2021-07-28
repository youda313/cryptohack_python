from optparse import OptionParser

options = OptionParser(usage='%prog server [options]', description='test the passing of options as arguments')
options.add_option('-p', '--port', type='int', default=443, help='TCP port to test (default: 443)')
options.add_option('-f', '--filein', type='str', help='Specify input file')
opts, args = options.parse_args()

if opts.port:
   print ("\nPort set to ... %s" % opts.port)
if opts.filein:
   print ("\nThe file stdin is ... %s" % opts.filein)
