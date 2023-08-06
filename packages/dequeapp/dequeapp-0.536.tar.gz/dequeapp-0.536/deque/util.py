from importlib import import_module
_not_importable = set()

DEQUE_IMAGE = "deque_image"
DEQUE_HISTOGRAM = "deque_histogram"
DEQUE_AUDIO="deque_audio"
DEQUE_VIDEO="deque_video"
DEQUE_TABLE="deque_table"
DEQUE_TEXT="deque_text"
DEQUE_BOUNDING_BOX="deque_bounding_box"
MODEL="model"
DATA="data"
PYTORCH="pytorch"
TENSORFLOW="tensorflow"
ENVIRONMENT="environment"
CODE="code"
RESOURCES = "resources"

def get_full_typename(o):

    instance_name = o.__class__.__module__ + "." + o.__class__.__name__
    if instance_name in ["builtins.module", "__builtin__.module"]:
        return o.__name__
    else:
        return instance_name


def is_type_torch_tensor(typename):
    return typename.startswith("torch.") and (
            "Tensor" in typename or "Variable" in typename
    )


def get_module(name, required=None):
    """
    Return module or None. Absolute import is required.
    :param (str) name: Dot-separated module path. E.g., 'scipy.stats'.
    :param (str) required: A string to raise a ValueError if missing
    :return: (module|None) If import succeeds, the module will be returned.
    """
    if name not in _not_importable:
        try:
            return import_module(name)
        except Exception as e:
            _not_importable.add(name)
            msg = "Error importing optional module {}".format(name)

    if required and name in _not_importable:
        raise Exception("required")