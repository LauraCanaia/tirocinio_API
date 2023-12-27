![picture alt](https://images.app.goo.gl/6UzEhRed8PFydrji6)  __WORK IN PROGRESS__ 

# Automatic swagger specification #
This project contains a .sh that joins different tools (like crawljax or mitmproxy) in order to help the automation of the 
generation process of an API's specification. \
This readme file tries to explain briefly the steps the .sh code does in order to generate the different swaggers.

### Python code ###
The python code takes as input a flow from mitmdump tries to extract the different URLs of the different APIs
the website called during the autocrawling phase.