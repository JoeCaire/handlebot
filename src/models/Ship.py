class Ship:
    def __init__(self, name, manufacturer, size, focus, cargo_capacity, crew, type, price, in_game_price, production_status, length, width, height, pitch_max, yaw_max, roll_max, x_axis_acceleration, y_axis_acceleration, z_axis_acceleration, component_json):
        self.name = name
        self.manufacturer = manufacturer
        self.size = size
        self.focus = focus
        self.cargo_capacity = cargo_capacity
        self.crew = crew
        self.type = type
        self.price = price
        self.in_game_price = in_game_price
        self.production_status = production_status
        self.length = length
        self.width = width
        self.height = height
        self.pitch_max = pitch_max
        self.yaw_max = yaw_max
        self.roll_max = roll_max
        self.x_axis_acceleration = x_axis_acceleration
        self.y_axis_acceleration = y_axis_acceleration
        self.z_axis_acceleration = z_axis_acceleration
        self.component_json = component_json

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name'),
            manufacturer=data.get('manufacturer'),
            size=data.get('size'),
            focus=data.get('focus'),
            cargo_capacity=data.get('cargo_capacity'),
            crew=data.get('crew'),
            type=data.get('type'),
            price=data.get('price'),
            in_game_price=data.get('in_game_price'),
            production_status=data.get('production_status'),
            length=data.get('length'),
            width=data.get('width'),
            height=data.get('height'),
            pitch_max=data.get('pitch_max'),
            yaw_max=data.get('yaw_max'),
            roll_max=data.get('roll_max'),
            x_axis_acceleration=data.get('x_axis_acceleration'),
            y_axis_acceleration=data.get('y_axis_acceleration'),
            z_axis_acceleration=data.get('z_axis_acceleration'),
            component_json=data.get('component_json')
        )

    def to_dict(self):
        return {
            'name': self.name,
            'manufacturer': self.manufacturer,
            'size': self.size,
            'focus': self.focus,
            'cargo_capacity': self.cargo_capacity,
            'crew': self.crew,
            'type': self.type,
            'price': self.price,
            'in_game_price': self.in_game_price,
            'production_status': self.production_status,
            'length': self.length,
            'width': self.width,
            'height': self.height,
            'pitch_max': self.pitch_max,
            'yaw_max': self.yaw_max,
            'roll_max': self.roll_max,
            'x_axis_acceleration': self.x_axis_acceleration,
            'y_axis_acceleration': self.y_axis_acceleration,
            'z_axis_acceleration': self.z_axis_acceleration,
            'component_json': self.component_json
        }
