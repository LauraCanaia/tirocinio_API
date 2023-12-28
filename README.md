<img alt="alert" height="25" src="png-transparent-warning-sign-caution-frame-angle-image-file-formats-text.png" width="50"/>WORK IN PROGRESS<img alt="alert" height="25" src="png-transparent-warning-sign-caution-frame-angle-image-file-formats-text.png" width="50"/>

# Automatic swagger specification #
This project contains a .sh that joins different tools (like crawljax or mitmproxy) in order to help the automation of the 
generation process of an API's specification. \
This readme file tries to explain briefly the steps of the .sh code does in order to generate the different swaggers.   
This project was tested ONLY on linux based OS. In order to make it work you need to install mitmproxy distribution. All 
the details can be found at this link : [mitmproxy](https://mitmproxy.org/).

### Python code ###
The python code takes as input a flow from mitmdump tries to extract the different URLs of the different APIs
the website called during the autocrawling phase.
