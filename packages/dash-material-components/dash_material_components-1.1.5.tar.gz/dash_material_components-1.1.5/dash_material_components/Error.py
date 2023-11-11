# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Error(Component):
    """An Error component.


Keyword arguments:

- id (string; default 'error'):
    Used to identify dash components in callbacks.

- message (string; required):
    Error message.

- status (number; required):
    Error status code."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_material_components'
    _type = 'Error'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, status=Component.REQUIRED, message=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'message', 'status']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'message', 'status']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['message', 'status']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Error, self).__init__(**args)
