class DevRepr():
    def __str__(self):
        field_values = {}
        for field in self._meta.get_fields():
            field_values[field.name] = str(getattr(self, field.name, ''))
        return '\n'.join([f"{a}:\t{v}" for a, v in field_values.items()]) + '\n'
