import os
import zipfile
import re
import argparse
import shutil
import zlib

#replaces all the usernames in the list of strings
def replace_user(user, data):
	outdata = []
	for line in data:
		outdata.append(re.sub(r"(user='\S*')", f"user='{user}'", line))
	return outdata

#replaces all the host in the list of strings
def replace_host(host,data):
	outdata = []
	for line in data:
		outdata.append(re.sub(r"(host=\S*)", f"host={host}", line))
	return outdata

#replaces all the usernames in the list of strings
def replace_port(port,data):
	outdata = []
	for line in data:
		outdata.append(re.sub(r"(port=\S*)", f"port={port}", line))
	return outdata

#replaces all the usernames in the list of strings
def replace_password(password,data):
	outdata = []
	for line in data:
		outdata.append(re.sub(r"(password='\S*')", f"password='{password}'", line))
	return outdata

def replace_dbname(dbname,data):
	outdata = []
	for line in data:
		outdata.append(re.sub(r"(dbname='\S*')", f"dbname='{dbname}'", line))
	return outdata

def zipdir(path, ziph):
	# ziph is zipfile handle
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Generate PDF report')
	parser.add_argument('-U', "--username", help="The replacement username")
	parser.add_argument('-H', "--hostname", help="The replacement hostname")
	parser.add_argument('-P', "--port", help="The replacement port")
	parser.add_argument('-W', "--password", help="The replacement password")
	parser.add_argument('-d', "--dbname", help="The replacement dbname")
	parser.add_argument('infile', help="infile")
	parser.add_argument('outfile', help="outfile")
	args = parser.parse_args()
	infile = args.infile
	outfile = args.outfile
	print(f"Infile: {infile} outfile: {outfile}")
	with zipfile.ZipFile(f'{infile}', 'r') as zip_ref:
		zip_ref.extractall('./temp')
	data = []
	infile_qgs = re.sub(r'\.qgz$','.qgs',infile)
	infile_qgd = re.sub(r'\.qgz$','.qgd',infile)
	outfile_qgs = re.sub(r'\.qgz$','.qgs',outfile)
	outfile_qgd = re.sub(r'\.qgz$','.qgd',outfile)
	with open(f"./temp/{infile_qgs}", 'r') as myfile:
		data = myfile.readlines()
	outdata = data
	if args.username:
		outdata = replace_user(args.username, outdata)
	if args.port:
		outdata = replace_port(args.port, outdata)
	if args.hostname:
		outdata = replace_host(args.hostname, outdata)
	if args.password:
		outdata = replace_password(args.password, outdata)
	if args.dbname:
		outdata = replace_dbname(args.dbname, outdata)
	with open(f"./temp/{outfile_qgs}", 'w') as writefile:
		writefile.writelines(outdata)
	
	os.rename(f"./temp/{infile_qgd}",f"./temp/{outfile_qgd}")

	os.remove(f"./temp/{infile_qgs}")

	with zipfile.ZipFile(outfile, mode='w') as zip_out:
		zip_out.write(f"./temp/{outfile_qgd}")
		zip_out.write(f"./temp/{outfile_qgs}", compress_type=zipfile.ZIP_DEFLATED)
	try:
		shutil.rmtree('./temp')
	except OSError as e:
		print ("Error: %s - %s." % (e.filename, e.strerror))