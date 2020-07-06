import re
from collections import OrderedDict
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from loguru import logger
from openpyxl import load_workbook

from mate3.sunspec.fields import Field, Mode

# from typing import Optional


PATH = Path(__file__).parent.parent / "doc" / "Outback.Power.SunSpec.Map.xlsx"
REGISTERS_SHEET = "SunSpecMap"
BITFIELDS_SHEET = "Bitfields"
MODELS_MODULE = Path(__file__).parent.parent / "models.py"
VALUES_MODULE = Path(__file__).parent.parent / "values.py"
MODELS_COLUMNS = OrderedDict(
    [
        ("did", {"column_names": ("DID",), "type": int}),
        ("start", {"column_names": ("Start",), "type": int}),
        ("end", {"column_names": ("End",), "type": int}),
        ("size", {"column_names": ("Size",), "type": int}),
        ("mode", {"column_names": ("R/W",), "type": str}),
        ("name", {"column_names": ("Name", "Field Name"), "type": str}),
        ("type", {"column_names": ("Type",), "type": str}),
        ("units", {"column_names": ("Units",), "type": str}),
        ("scale_factor", {"column_names": ("Scale Factor",), "type": str}),
        ("contents", {"column_names": ("Contents",), "type": str}),
        ("description", {"column_names": ("Description",), "type": str}),
    ]
)
BITFIELDS_COLUMNS = ("did", "bitfield_name", "name", "mask", "value", "description")

WARNING = f"This file is auto generated, do not edit. The generation code can be found in {Path(__file__).name}"


@dataclass
class ModelRow:

    did: int
    start: int
    end: int
    size: int
    mode: str
    name: str
    type: str
    units: str
    scale_factor: str
    contents: str
    description: str

    # set dynamically:
    python_name: str = None


@dataclass(frozen=False)
class BitfieldRow:

    did: int
    bitfield_name: str
    name: str
    mask: int
    value: int
    description: str

    # set dynamically:
    python_name: str = None


def python_name_from_field(name):
    name = name.strip()
    # first, replace kW/kWh (and variants of caps) with kw/kwh to avoid splitting:
    name = re.sub(r"(^|_)kwh(_|$)", r"\1kwh\2", name, flags=re.I)
    name = re.sub(r"(^|_)kw(_|$)", r"\1kw\2", name, flags=re.I)
    # now do naive snake case underscore insert - <lower><UPPER> -> <lower>_<upper>. Why naive? That's all we need.
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name).lower()
    # remove ick:
    name = re.sub(r"[^a-zA-Z0-9_]", r"", name)
    # manual renamings:
    name = re.sub(r"batt(_|$)", r"battery\1", name)
    name = re.sub(r"_sf$", r"_scale_factor", name)
    name = re.sub(r"_temp(_|$)", r"_temperature\1", name)
    return name


def find_common_prefixes(rows):
    """
    Find any common prefixes for the registry names given in the provided lines, after splitting on _. E.g. 

    PREFIX_a
    PREFIX_b_c
    ...

    Would return {'PREFIX'}. While

    PREFIX_PREFIX2_a
    PREFIX_PREFIX2_b_c
    ...

    Would return {'PREFIX_PREFIX2'}. We do this by finding the common ancestor that all have. If there is not at
    root level, then we just return the prefixes at root level, i.e.

    PREFIX1_a
    PREFIX2_b_c
    ...

    Would return {'PREFIX1', 'PREFIX2'}
    """

    if len(rows) <= 1:
        return set()

    splats = [row.name.split("_") for row in rows]
    previous_common_ancestor = None
    for i in range(1, max(len(s) for s in splats)):
        prefixes = set(["_".join(s[:i]) + "_" for s in splats])
        if len(prefixes) > 1:
            return prefixes if previous_common_ancestor is None else previous_common_ancestor
        previous_common_ancestor = prefixes
    else:
        raise RuntimeError("Couldn't find common prefixes!")


def strip_prefix(name, common_prefixes):
    """snake_case + remove common prefix at start"""
    for prefix in common_prefixes:
        if name.startswith(prefix):
            return name.replace(prefix, "", 1)
    return name


def clean_rows(rows):
    common_prefixes = find_common_prefixes(rows)
    for row in rows:
        row.python_name = python_name_from_field(strip_prefix(row.name, common_prefixes))


class ModelTable:
    def __init__(self, *, name, rows):
        self.name = name
        if len({row.did for row in rows}) > 1:
            raise ValueError("All rows must have the same DID!")
        self.did = rows[0].did
        self.rows = rows
        clean_rows(self.rows)

    @property
    def python_name(self):
        name = re.sub(r"[\s\-]", "", self.name)
        name = re.sub(r"(block|model)$", "", name, flags=re.I)
        return re.sub(r"(block|model)$", "", name, flags=re.I)

    def generate_definition(self, bitfields):
        class_name = self.python_name
        code = f"@unique\nclass {class_name}Model(Enum):\n"
        afters = []
        for row in self.rows:
            defn, after = self._generate_field(row=row, class_name=class_name, bitfields=bitfields)
            code += defn
            afters += after
        if afters:
            code += "\n\n"
            for after in afters:
                code += after
        code += "\n"
        return code

    def generate_values(self):
        class_name = self.python_name
        code = f"@dataclass\nclass {class_name}Values:\n"
        code += f"    address: int\n"
        # code += f"    __definition__ = models.{class_name}Model\n"
        for row in self.rows:
            name = row.python_name
            if name in ("sun_spec_did", "sun_spec_length"):
                name = name.replace("sun_spec_", "")
            code += f"    {name}: FieldValue\n"
        return code

    @lru_cache()
    def _get_scale_factor_python_name(self, scale_factor):
        rows = [r for r in self.rows if r.name == scale_factor]
        if len(rows) != 1:
            raise RuntimeError(f"Expected to find a single scale_factor '{scale_factor}' but found {len(rows)}")
        return rows[0].python_name

    def _generate_base_field(self, row):
        for field_name in Field.__dataclass_fields__:
            # ignore the name:
            if field_name == "name":
                continue
            value = getattr(row, field_name)
            # ignore none description as that's the default:
            if field_name == "description" and value is None:
                continue
            # Mode -> enum
            if field_name == "mode":
                value = Mode(row.mode.lower().replace("/", ""))
            # strings:
            if isinstance(value, str):
                value = '"' + value + '"'
            if field_name in ("start", "size", "mode"):
                yield f"{value}"
            else:
                yield f"{field_name}={value}"

    def _generate_integer_field(self, row, python_name, class_name):
        # Units:
        if row.units:
            yield False, f'units="{row.units}"'
        # Find the scale factor:
        scale_factor = row.scale_factor
        if scale_factor:
            scale_factor = self._get_scale_factor_python_name(scale_factor)
            yield True, f"{class_name}Model.{python_name}.value.scale_factor = {class_name}Model.{scale_factor}\n"
        # else:
        #    yield False, ""

    def _generate_bit_field(self, row, bitfields):
        yield f"flags={bitfields[row.name]}"

    def _generate_enumerated_field(self, row):
        # ok, generate always seems to following the form 1=..., 2=..., etc. or ...=1, ...=2, So let's look for that
        starts_number = list(re.finditer(r"(\-?[0-9]+)\s?=\s?(.*?)(?=\-?[0-9]+\s?=|$)", row.description))
        ends_number = list(re.finditer(r"(.*?)\s?=\s?(\-?[0-9]+)", row.description))
        options = []
        use_start = True
        if starts_number:
            if ends_number:
                n_start = len(starts_number)
                n_end = len(ends_number)
                if n_start == n_end:
                    # ok, confusing ... must be something like 0 = 1, 1 = 2, etc.
                    pass
                else:
                    # use the one with the most:
                    use_start = n_start > n_end
                    logger.warning(
                        f"field {row.name} is enumerated but the description matches both number-first and "
                        f"number-last enumeration. Going with number-{'first' if use_start else 'last'} as there are "
                        f"{n_start} number-first matches and {n_end} number-last matches.\n\tNB desc: {row.description}"
                    )
        elif ends_number:
            use_start = False
        else:
            raise ValueError("Couldn't match description to enumeration ...")

        if use_start:
            for m in starts_number:
                g = m.groups()
                k = int(g[0])
                v = g[1].strip().strip(",")
                options.append((v, k))
        else:
            for m in ends_number:
                g = m.groups()
                k = int(g[1])
                v = g[0].strip().strip(",")
                options.append((v, k))

        # check all values are unique:
        if len(set(i[1] for i in options)) < len(options):
            raise ValueError("Duplicate numeric values in enumerable!")

        # get rid of duplicates:
        unique_options = {}
        p = re.compile(r"[^a-z0-9]+", flags=re.I)
        for v, k in options:
            v_original = p.sub("_", v).upper().strip("_")
            if v in unique_options:
                v = f"{v_original}_{k}"
                logger.warning(f"{v_original}={k} renamed as {v}={k} as {v} already exists")
            unique_options[v] = k

        enum = f'Enum("{row.python_name}", {str(list(sorted(unique_options.items())))})'
        yield f"options={enum}"

    def _generate_field(self, row, class_name, bitfields):
        """Generate a single Field definition for a table Model class"""

        name = row.python_name
        if name in ("sun_spec_did", "sun_spec_length"):
            name = name.replace("sun_spec_", "")
        field_type = None
        field_args = list(self._generate_base_field(row))
        afters = []
        if row.type in ("uint16", "int16", "uint32", "int32"):
            int_field = True
            units = row.units.lower().strip() if row.units is not None else None
            if units == "bitfield":
                int_field = False
                # if we don't know about that bitfield, skip it - generally these are ones kept for future use
                if row.name not in bitfields:
                    logger.warning(f"skipping {row.name} as unknown bitfield. Row: {row}")
                    return "", []
                field_type = f"Bit{16 * row.size}"
                field_args += list(self._generate_bit_field(row, bitfields))
            elif units == "enumerated" or (
                row.description is not None
                and re.match(r"^\s*0\s*=\s*Disabled\s*[,;]\s*1\s*=\s*Enabled\s*$", row.description)
            ):
                try:
                    field_args += list(self._generate_enumerated_field(row))
                    field_type = f"Enum{row.type.title()}"
                    int_field = False
                except ValueError as e:
                    logger.warning(
                        (
                            f"field {row.name} is enumerated but the description isn't enumerable so "
                            f"treating as int: \n\tDesc: '{row.description}'\n\tError: {e}"
                        )
                    )
            elif units == "address":
                int_field = False
                field_type = "Address"

            if int_field:
                for after, args in self._generate_integer_field(row, name, class_name):
                    if after:
                        afters.append(args)
                    else:
                        field_args.append(args)
                field_type = row.type.title()
        elif row.type.startswith("string"):
            field_type = "String"
        else:
            raise ValueError(f"Don't know what to do with type {row.type}")
        return f"    {name} = {field_type}Field({', '.join(field_args)})\n", afters


class BitfieldTable:
    def __init__(self, rows):
        did = rows[0].did
        name = rows[0].bitfield_name
        for row in rows:
            if row.did != did or row.bitfield_name != name:
                raise RuntimeError("All rows should have the same name and did")
        self.name = name
        self.rows = self._sanitise_rows(rows)
        clean_rows(self.rows)

    def _sanitise_rows(self, rows):
        """
        Sometimes the 'off' value is specified in the table too e.g.
            Virtual Name            Mask    Value   Description
            OB_Inverter_AC_Input	0x0004	0x0004	Inverter AC Input Use 
            OB_Inverter_AC_Input	0x0004	0x0000	Inverter AC Input Drop 
        In this case, we only keep the 'on' one (where value is !0) and then update the description of value + mask.
        """
        on_by_name = {}
        off_by_name = {}
        for row in rows:
            if row.value is None or int(row.value, base=16) != 0:
                if row.name in on_by_name:
                    raise RuntimeError("multiple on rows!")
                on_by_name[row.name] = row
            else:
                if row.name in off_by_name:
                    raise RuntimeError("multiple off rows!")
                off_by_name[row.name] = row

        # update the ons with the offs:
        for row in off_by_name.values():
            logger.warning(
                (
                    f"{row.name} has an on value ({on_by_name[row.name].description}), and an off {row.description}. "
                    "Assuming these are opposites, so ignoring the off value so we have a proper bitfield."
                )
            )
            on_by_name[row.name].description += f" (Unset means '{row.description}')"

        return sorted(list(on_by_name.values()), key=lambda x: x.mask)

    @property
    def python_name(self):
        name = self.name.replace("_", "")
        name = re.sub(r"flags$", "", name, flags=re.I)
        return name + "Flags"

    def generate_definition(self):
        class_name = self.python_name
        code = f"@unique\nclass {class_name}(BitfieldDescriptionMixin, IntFlag):\n"
        for row in self.rows:
            mask = int(row.mask, base=16)
            code += f'    {row.python_name} = {mask}, "{row.description}"\n'
        return code


# function to ensure string values are ascii, and N/A -> null
def sanitise(value):
    if isinstance(value, str):
        value = value.encode("ascii", errors="backslashreplace").decode("ascii").strip()
        return None if value == "N/A" else value
    return value


def read_model_table(row_iter):

    # Start looking though rows until we find the start of a table - that is, where DID column == 'DID'. If we don't see
    # this for 100 rows (as there are some 'empty' error tables in between) then we assume there are no more tables.
    more_tables = True
    row = None
    try:
        for _ in range(100):
            row = next(row_iter)
            named_values = {k: row[idx].value for idx, k in enumerate(MODELS_COLUMNS)}
            if named_values["did"] == "DID":
                break
            previous_row = row
        else:
            # Ok, more than 100 blank lines - there aren't any tables after this:
            more_tables = False
    except StopIteration:
        # Or the iterator finished (as it was clever enough to know there was nothing else)
        more_tables = False

    if not more_tables:
        return None, None

    title_row = previous_row
    table_name = re.sub("^Table [0-9]+", "", title_row[1].value).strip()

    # Cool, next row is header - check column names:
    header_row = row
    for cidx, (name, (_, col)) in enumerate(zip(header_row, MODELS_COLUMNS.items())):
        name = name.value
        expected_names = col["column_names"]
        if name not in expected_names:
            raise ValueError(f"Expected table header for column {cidx} to be in {expected_names} but was '{name}'")

    # The rest of the rows, until we hit blank DID, are fields:
    model_rows = []
    for row in row_iter:
        named_values = {k: sanitise(row[idx].value) for idx, k in enumerate(MODELS_COLUMNS)}
        # if this is the first row, and it's blank, skip it - sometimes there's just a completely empty row after the
        # header:
        if not model_rows and all(v is None for v in named_values.values()):
            continue
        # if DID cell is blank, then we've finished parsing table:
        if named_values["did"] is None:
            return table_name, model_rows
        # type it:
        named_values = {k: v if v is None else MODELS_COLUMNS[k]["type"](v) for k, v in named_values.items()}
        model_rows.append(ModelRow(**named_values))
    # in case we finish iter:
    return table_name, model_rows


def read_bitfields(wb):
    did_names = {}
    ws = wb[BITFIELDS_SHEET]
    current_did = None
    current_name = None
    for row in ws.iter_rows(max_col=len(BITFIELDS_COLUMNS) + 1):
        values = {k: sanitise(v.value) for k, v in zip(BITFIELDS_COLUMNS, row)}
        did = values["did"]
        name = values["bitfield_name"]
        if isinstance(did, int):
            if did != current_did or name != current_name:
                if (did, name) in did_names:
                    raise RuntimeError("Uh-oh, repeat DID + Name table!")
                did_names[(did, name)] = []
            did_names[(did, name)].append(BitfieldRow(**values))
            current_did = did
            current_name = name
        else:
            current_did = None
            current_name = None
    tables = {}
    for rows in did_names.values():
        table = BitfieldTable(rows=rows)
        # last I_Event_1 ones seem to be repeats, just for different DID's - let's check they are the same
        if table.name in tables:
            a = [BitfieldRow(did=1, **{k: v for k, v in r.__dict__.items() if k != "did"}) for r in table.rows]
            b = [
                BitfieldRow(did=1, **{k: v for k, v in r.__dict__.items() if k != "did"})
                for r in tables[table.name].rows
            ]
            if a != b:
                raise RuntimeError(f"Duplicate table of name {table.name} but different rows.")
        else:
            tables[table.name] = table
    return list(tables.values())


def read_models(wb):
    tables = {}
    ws = wb[REGISTERS_SHEET]
    row_iter = ws.iter_rows(max_col=len(MODELS_COLUMNS) + 1)
    while True:
        name, rows = read_model_table(row_iter)
        if rows is None:
            break
        if name == "UPS Inverters":
            # This table is weird. Ignore it.
            break
        table = ModelTable(name=name, rows=rows)
        if table.name in tables:
            raise ValueError(f"Two tables named {table.name}")
        tables[table.name] = table
    return list(tables.values())


def main():

    wb = load_workbook(PATH)

    # bitfields first:
    bitfield_tables = read_bitfields(wb)
    bitfield_tables = sorted(bitfield_tables, key=lambda x: x.python_name)
    code = f'''"""{WARNING}"""


from enum import Enum, IntFlag, unique
from mate3.sunspec.fields import (
    Mode,
    StringField,
    Int16Field,
    Uint16Field,
    Int32Field,
    Uint32Field,
    EnumUint16Field,
    EnumUint32Field,
    EnumInt16Field,
    EnumInt32Field,
    Bit16Field,
    Bit32Field,
    BitfieldDescriptionMixin,
    AddressField
)


'''
    for table in bitfield_tables:
        code += table.generate_definition()
        code += "\n"

    code += f"""
@unique
class SunSpecHeaderModel(Enum):
    did = Uint32Field(1, 2, Mode.R)
    model_id = Uint16Field(3, 1, Mode.R)
    length = Uint16Field(4, 1, Mode.R)
    manufacturer = StringField(5, 16, Mode.R)
    model = StringField(21, 16, Mode.R)
    options = StringField(37, 8, Mode.R)
    version = StringField(45, 8, Mode.R)
    serial_number = StringField(53, 16, Mode.R)


@unique
class SunSpecEndModel(Enum):
    did = Uint16Field(1, 1, Mode.R, description="Should be {0xFFFF}")
    length = Uint16Field(2, 1, Mode.R, description="Should be 0")
\n
"""
    model_tables = read_models(wb)
    model_tables = sorted(model_tables, key=lambda x: x.did)
    bitfield_lookup = {t.name: t.python_name for t in bitfield_tables}
    for table in model_tables:
        code += table.generate_definition(bitfield_lookup)
        code += "\n"

    code += "MODEL_DEVICE_IDS = {\n"
    code += f"    {0x53756e53}: SunSpecHeaderModel,\n"
    code += "    65535: SunSpecEndModel,\n"
    for table in model_tables:
        code += f"    {table.did}: {table.python_name}Model,\n"
    code += "}\n"

    with open(str(MODELS_MODULE), "w") as f:
        f.write(code)

    # now values:
    code = f'''"""{WARNING}"""

from mate3.sunspec.fields import FieldValue
from dataclasses import dataclass
from mate3.sunspec import models


@dataclass
class SunSpecHeaderValues:
    address: int
    did: FieldValue
    model_id: FieldValue
    length: FieldValue
    manufacturer: FieldValue
    model: FieldValue
    options: FieldValue
    version: FieldValue
    serial_number: FieldValue


@dataclass
class SunSpecEndValues:
    address: int
    did: FieldValue
    length: FieldValue


'''
    for table in model_tables:
        code += table.generate_values()
        code += "\n\n"

    code += "MODELS_TO_VALUES = {\n"
    code += "    models.SunSpecHeaderModel: SunSpecHeaderValues,\n"
    code += "    models.SunSpecEndModel: SunSpecEndValues,\n"
    for table in model_tables:
        code += f"    models.{table.python_name}Model: {table.python_name}Values,\n"
    code += "}\n"

    with open(str(VALUES_MODULE), "w") as f:
        f.write(code)


if __name__ == "__main__":
    main()
