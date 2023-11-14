# Vehicle Data Python Package

This Python package provides functionality to retrieve vehicle-related information.

## Installation

You can install the package using pip:

```bash
pip install vehciledata
```

from vehciledata.main import getChallan, get_vehicle_details, getvehicle

# Example usage
```py
vehicle_number = "DL9CX5463"
challan_header, challans = getChallan(vehicle_number)
vehicle_details = get_vehicle_details(vehicle_number)

print(f"Challan Header: {challan_header}")
print(f"Challans: {challans}")
print(f"Vehicle Details: {vehicle_details}")
```

# Command Line Interface

getvehicle DL9CX5463


```py

from vehciledata.details import getChallan, get_vehicle_details, getvehicle

# Example usage
vehicle_number = "DL9CX5463"
challan_header, challans = getChallan(vehicle_number)
vehicle_details = get_vehicle_details(vehicle_number)

print(f"Challan Header: {challan_header}")
print(f"Challans: {challans}")
print(f"Vehicle Details: {vehicle_details}")

```
