import csv
import inspect
import re
from enum import Enum
from pathlib import Path
from typing import NamedTuple, Optional, NewType, Dict, List, Tuple, Set
import black
from click.testing import CliRunner

from mate3.base_definitions import Field, Mode
from mate3.base_structures import Device

CSV_PATH = Path(__file__).parent.parent / 'registry_data'
DEFINITIONS_MODULE = Path(__file__).parent / 'definitions.py'
STRUCTURES_MODULE = Path(__file__).parent / 'structures.py'

WARNING = f'This file is auto generated, do not edit. The generation code can be found in {Path(__file__).name}'


class Line(NamedTuple):
    """Represents a line in a CSV file"""
    did: int
    start: int
    end: int
    size: int
    mode: str
    name: str
    type: str
    units: Optional[str]
    scale_factor: Optional[str]
    contents: str
    description: str

    @property
    def python_name(self) -> str:
        name = self.name.replace('\n', '').lower()
        name = re.sub(r'[^a-zA-Z0-9_]', r'', name)
        name = re.sub(r'batt(_|$)', r'battery\1', name)
        name = re.sub(r'_sf$', r'_scale_factor', name)
        name = re.sub(r'_temp(_|$)', r'_temperature\1', name)
        return name

    @property
    def python_type(self):
        if self.type in ('uint16', 'int16', 'uint32', 'int32'):
            return self.type
        elif 'string' in self.type:
            return 'str'
        else:
            assert False, f"Don't know what to do with type {self.type}"

    @property
    def normalised_mode(self) -> Mode:
        return Mode(self.mode.lower().replace('/', ''))


def find_common_name_prefixes(lines: List[Line]) -> Set[str]:
    """Find any common prefixes for the registry names given in the provided lines

    This is a little bit complex. We split all the registry names on the underscore
    character, then turn them into a tree. We then descend that tree until it starts
    to branch out. When it branches out we assume we've reached the end of the common
    prefix.
    """
    tree: Dict[str, List[int, dict]] = {}
    names = [l.name.split('_') for l in lines]
    for name in names:
        current_tree = tree
        for bit in name:
            current_tree.setdefault(bit, [0, {}])
            current_tree[bit][0] += 1
            current_tree = current_tree[bit][1]

    def _find_prefixes(node: dict, bits: tuple):
        found_prefixes = []
        for bit, (total_children, child_node) in node.items():
            total_forks = len(child_node)
            if total_children == 1:
                # We've come to a leaf node. Don't include this bit
                # in the common prefix
                found_prefixes.append(bits)
            elif total_forks > 2:
                # Things start forking quite a lot here, so lets stop
                # chasing this path and say that this is a common prefix
                found_prefixes.append(bits + (bit,))
            else:
                # There are one or two forks (i.e. one child or two children),
                # so let's treat them as common and descend into them
                found_prefixes.extend(_find_prefixes(child_node, bits + (bit,)))

        return found_prefixes

    prefixes = _find_prefixes(tree, tuple())
    prefixes = {'_'.join(prefix_bits).lower() + '_' for prefix_bits in prefixes if prefix_bits}
    return prefixes


def strip_prefixes(register_name: str, prefixes: Set[str]):
    """Utility to strip a set of strings from the start of another string"""
    for prefix in prefixes:
        if register_name.startswith(prefix):
            register_name = register_name.replace(prefix, '', 1)
            break

    return register_name


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


def read_file(csv_path: Path) -> List[Line]:
    """Read the given csv file and return a list of Line tuples"""
    lines = []

    def _remove_whitespace(v):
        return re.sub(r'\s', '', v)

    with open(str(csv_path), newline='') as csv_file:
        reader = csv.reader(csv_file)

        # Ensure the first column as the header 'DID'
        headers = next(reader)
        if headers[0].lower().strip() != 'did':
            return []

        # Now get all the rows which have a DID as the first value
        for row in reader:
            if row[0].isnumeric() and len(row) == len(Line._fields):
                row = [v.strip() for v in row]

                lines.append(Line(
                    did=int(_remove_whitespace(row[0])),
                    start=int(_remove_whitespace(row[1])),
                    end=int(_remove_whitespace(row[2])),
                    size=int(_remove_whitespace(row[3])),
                    mode=str(_remove_whitespace(row[4])),
                    name=str(_remove_whitespace(row[5])),
                    type=str(_remove_whitespace(row[6])),
                    units=str(_remove_whitespace(row[7])),
                    scale_factor=str(_remove_whitespace(row[8])),
                    contents=str(_remove_whitespace(row[9])),
                    description=str(row[10].replace('\n', ' ')),
                ))

    return lines


def read_all_files() -> Dict[Device, List[Line]]:
    """Read all CSV files and return a Line tuples grouped by device"""
    lines = {}
    csv_paths = CSV_PATH.glob('*.csv')
    for csv_path in csv_paths:
        for line in read_file(csv_path):
            device = Device(line.did)
            lines.setdefault(device, [])
            lines[device].append(line)

    return dict(sorted(lines.items(), key=lambda l: l[0].value))


def generate_field(line: Line, prefixes_to_strip: Set[str], other_lines: List[Line]):
    """Generate a single Field definition for a block Definition class"""
    # Get the default Field attribute values so we can exclude fields we don't need to specify
    arg_spec = inspect.getfullargspec(Field)
    default_names = arg_spec[3]
    attribute_names = arg_spec[0][-len(default_names):]
    defaults = dict(zip(attribute_names, default_names))

    field_args = []
    for field_name in Field._fields:
        if field_name in ('name', 'device'):
            # These are set programmatically, their data is not available in the CSV
            continue

        value = getattr(line, field_name)
        if field_name in defaults and value == defaults[field_name]:
            # Has the default value. nothing to do
            break

        if isinstance(value, str) and value.lower().strip() == 'n/a':
            value = None

        if isinstance(value, Enum):
            value = value.value

        if field_name == "scale_factor" and value:
            destination_field = [ol for ol in other_lines if ol.name == value]
            assert destination_field, f"Count not find field {value} which the scaling factor points to. Line: {line}"
            value = strip_prefixes(register_name=destination_field[0].python_name, prefixes=prefixes_to_strip)

        if field_name == "mode" and value:
            value = line.normalised_mode

        if field_name == "type" and value:
            value = line.python_type

        if isinstance(value, str) and field_name not in ('type',):
            value = repr(value)

        field_args.append(f'{field_name}={value}')

    name = strip_prefixes(register_name=line.python_name, prefixes=prefixes_to_strip)
    return f"    {name} = Field({', '.join(field_args)})\n"


def generate_definition_header():
    return (
        f"'''{WARNING}'''\n\n"
        "from mate3.base_definitions import *\n"
        "from mate3.base_structures import *\n"
        "from mate3.structures import *\n"
        "\n\n"
    )


def generate_definition(device: Device, lines: List[Line]):
    """Generate an entire block Definition class"""
    common_prefixes = find_common_name_prefixes(lines)

    class_name = f"{to_camel_case(device.name)}Definition"

    code = (
        f"# {WARNING}\n"
        f"class {class_name}(BaseDefinition):\n"
    )

    for line in lines:
        code += generate_field(line, prefixes_to_strip=common_prefixes, other_lines=lines)

    code += "\n"
    code += f"    structure = {to_camel_case(device.name)}Block\n"
    code += f"    device = Device.{device.name}\n\n"

    return code


def generate_structure_header():
    return (
        f"# {WARNING}\n\n"
        "from mate3.base_structures import *\n"
        "from typing import NamedTuple\n"
        "\n\n"
    )


def generate_structure(device: Device, lines: List[Line]):
    common_prefixes = find_common_name_prefixes(lines)

    class_name = f"{to_camel_case(device.name)}Block"
    code = f"# {WARNING}\n"
    code += f"class {class_name}(NamedTuple):\n"
    code += f"    device: Device\n\n"

    for line in lines:
        name = strip_prefixes(register_name=line.python_name, prefixes=common_prefixes)
        if 'string' in line.type:
            type = 'str'
        else:
            type = line.type

        code += f'    {name}: {type}\n'

    return code


def format_python_file(path: Path):
    runner = CliRunner()
    result = runner.invoke(
        black.main,
        [str(path)],
    )
    assert result.exit_code == 0, result.output


def main():
    definition_code = generate_definition_header()
    for device, lines in read_all_files().items():
        definition_code += generate_definition(device, lines)

    structure_code = generate_structure_header()
    for device, lines in read_all_files().items():
        structure_code += generate_structure(device, lines)

    with open(str(DEFINITIONS_MODULE), 'w') as f:
        f.write(definition_code)

    format_python_file(DEFINITIONS_MODULE)

    with open(str(STRUCTURES_MODULE), 'w') as f:
        f.write(structure_code)

    format_python_file(STRUCTURES_MODULE)


if __name__ == '__main__':
    main()
