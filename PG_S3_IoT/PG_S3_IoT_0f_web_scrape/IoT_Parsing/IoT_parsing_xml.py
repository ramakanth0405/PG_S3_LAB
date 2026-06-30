import xml.etree.ElementTree as ET

# Raw XML text data string

raw_xml_payload = """
<telemetry>
    <device>Node_B</device>
    <reading unit= "celcius">24.1</reading>
</telemetry>
"""

# Parse the XML string into a queryable tree layout
root = ET.fromstring(raw_xml_payload)

for child in root:
    print(child.tag, child.attrib)


# Extract text values by finding the matching tags 
device_name = root.find('device').text
temperature_value = root.find('reading').text
unit_attribute = root.find('reading').get('unit')

print(f"Device: {device_name}")
print(f"Reading: {temperature_value}{unit_attribute}")