"""Various validators"""


def validate_integer(
		arg_name, arg_value, min_value = None, max_value=None,
		custom_min_message=None, custom_max_message=None
):
	"""
	Validates that 'arg_value' is an integer and optionally falls within specific bounds.
	A custom override error message can be provided when min/max bounds are exceeded.

	:param arg_name:(str)
	:param arg_value:(obj)
	:param min_value:(int)
	:param max_value:(max)
	:param custom_min_message:(str)
	:param custom_max_message:(str)
	:return:
		None: no exceptions raised if the validation passes

	Raises:
		TypeError: if the arg_value is not an int
		ValueError: if arg_value does not satisfy the bounds
	"""

	if not isinstance(arg_value, int):
		raise TypeError(f'{arg_name} must be an integer')
	if min_value is not None and arg_value < min_value:
		if custom_min_message is not None:
			raise ValueError(custom_min_message)
		raise ValueError(f"{arg_name} that cannot be less than {min_value}")
	if max_value is not None and arg_value > max_value:
		if custom_max_message is not None:
			raise ValueError(custom_max_message)
		raise ValueError(f"{arg_name} that cannot be greater than {max_value}")
