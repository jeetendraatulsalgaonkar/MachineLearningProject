from dataclasses import dataclass

@dataclass
class BasicData:
    vehicle_type: str
    make: str
    model: str
    body_type: str
    model_year: int
    vin: str

@dataclass
class EngineAndDriveType:
    kw: float
    hp: float
    transmission_type: str
    capacity_ccm: float
    number_of_gears: int
    driven_wheels: int
    steering: str
    speedometer_unit: str
    number_of_cylinders: int
    emission_class: str

@dataclass
class BodyAndChassis:
    number_of_doors: int
    seating_capacity: int

@dataclass
class TankAndConsumption:
    fuel_category_1: str
    fuel_type_1: str
    fuel_unit_1: str
    fuel_volume_1: float
    fuel_category_2: str
    fuel_type_2: str
    fuel_unit_2: str
    fuel_volume_2: float
    plugin: bool
    battery_range: float
    consumption_city: float
    consumption_highway: float
    consumption_combined: float

@dataclass
class Equipment:
    equipment_type: str
    equipment_price: float

@dataclass
class Price:
    base_price: float
    equipment_price: float
    total_price: float

@dataclass
class VehicleData:
    basic_data: BasicData
    engine_and_drive_type: EngineAndDriveType
    body_and_chassis: BodyAndChassis
    tank_and_consumption: TankAndConsumption
    equipment: list[Equipment]
    price: Price