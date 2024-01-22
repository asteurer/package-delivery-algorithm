from HashMap import HashMap
from Package import Package

def main():
    map = HashMap()
    package = Package(2, "IN_TRANSIT", "EOD", "233 canyon Rd", "Salt Lake City", 84103)
    map.set_value(3, package.map_array())
    print(map.get_value(3, "city"))



main()