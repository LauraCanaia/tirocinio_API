from mitmproxy.http import HTTPFlow
from mitmproxy.io import FlowReader
import os
"""
if f.request.scheme in ['http', 'https', 'get', 'post', 'put', 'delete', 'patch',
                        'options', 'head', 'connect', 'trace', 'json']:
    print(f"Request URL: {f.request.url}\n")
    print(f"Request Method: {f.request.method}\n")
    print(f"Request Headers: {f.request.headers}\n")
    print(f"Request Body: {f.request.content}\n")
    print("\n")
    output_file.write(f"Request URL: {f.request.url}\n")
    output_file.write(f"Request Method: {f.request.method}\n")
    output_file.write(f"Request Headers: {f.request.headers}\n")
    output_file.write(f"Request Body: {f.request.content}\n")
    output_file.write("\n")
    """

def extract_json_responses(flow_file, outputfile):
    with open(flow_file, "rb") as f:
        flow_reader = FlowReader(f)
        # Check if the output file exists, it removes it
        if os.path.exists(outputfile):
            os.remove(outputfile)
        # creates a new output file
        with open(outputfile, 'a'):
            pass  # Create an empty file

        with open(outputfile, 'a') as output_file:
            for f in flow_reader.stream():
                # the function isistance returns true whether the first parameter is an istance of a class or a subclass
                # specified in the second parameter (checks if f is an istance of HTTPFlow)
                if isinstance(f, HTTPFlow):
                    # check if in the content type field the substring 'json' is present
                    if "json" in f.response.headers.get("Content-Type", ""):
                        output_file.write(f"{f.type}://{f.request.authority}{f.request.path}\n")
                        output_file.write(f"{f}\n")
                        output_file.write("\n")

# first filter to strain the http flow in order to get only the responses with json in it
extract_json_responses('about.cilabs.com/flowDump', 'about.cilabs.com/output.txt')

