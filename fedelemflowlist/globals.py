#Set global variables for flow list creation

inputpath = 'fedelemflowlist/input/'
outputpath = 'fedelemflowlist/output/'
flowmappingpath = 'fedelemflowlist/flowmapping'
context_fields = ['Directionality','Compartment']

#list_version_no = '0.1' #Must be numeric
#flow_types = {'Energy':'resource', 'Fuel':'resource', 'Land':'resource', 'Chemicals':'emission', 'Groups':'emission'}

list_version_no = '0.3e' #Must be numeric
#flow_types = ['Biological','Chemicals','Energy', 'Fuel', 'Geological','Groups','Land','Water','Other']
flow_types = ['Energy']

def convert_to_lower(x):
    x = str(x)
    x = str.lower(x)
    return x

def as_path(*args: str) -> str:
    strings = []
    for arg in args:
        if arg is None:
            continue
        strings.append(str(arg).strip().lower())
    return "/".join(strings)

