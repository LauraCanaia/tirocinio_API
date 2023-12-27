from mitmproxy.http import HTTPFlow
from mitmproxy.io import FlowReader
import os


def extract_json_responses(flow_file):
    API_list = []
    with open(flow_file, "rb") as f:
        flow_reader = FlowReader(f)
        # Check if the output file exists, it removes it

        for f in flow_reader.stream():
            # the function isistance returns true whether the first parameter is an istance of a class or a subclass
            # specified in the second parameter (checks if f is an istance of HTTPFlow)
            if isinstance(f, HTTPFlow):
                # check if in the content type field the substring 'json' is present
                if "json" in f.response.headers.get("Content-Type", ""):
                    if f.request.method in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD', 'CONNECT',
                                            'TRACE']:
                        split_path = (f.request.path).split('/', 3)
                        resulting_string = f"{f.type}://{f.request.authority}/{split_path[1]}"
                        if resulting_string not in API_list:
                            API_list.append(resulting_string)

    return API_list


def write_in_output_file(outputfile, api_list):
    if os.path.exists(outputfile):
        os.remove(outputfile)
        # creates a new output file
    with open(outputfile, 'a'):
        pass  # Create an empty file

    with open(outputfile, 'a') as output:
        for elem in api_list:
            output.write(f"{elem}\n")


# first filter to strain the http flow in order to get only the responses with json in it
list_of_API = extract_json_responses('about.cilabs.com/flowDump')
write_in_output_file('about.cilabs.com/output.txt', list_of_API)
