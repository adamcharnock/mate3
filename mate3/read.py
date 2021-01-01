import dataclasses as dc
from datetime import datetime
from typing import Any


@dc.dataclass
class FieldRead:
    raw_value: Any
    implemented: bool
    address: int
    time: datetime


class ModelRead(dict):
    """
    A class for storing all the reads for a given model for a given device.
    """

    def add(self, field_name, raw_value, implemented, address, time):
        self[field_name] = FieldRead(raw_value=raw_value, implemented=implemented, address=address, time=time)


class AllModelReads(dict):
    """
    A class for storing all the reads for all models. It's basically just a dict
        Dict[<model class>, List[ModelRead]]
    I.e. for each model class, a list of all the (full) reads of that model type (which can be multiple e.g. if there 
    are two of the same inverter.)
    """

    def add(self, model, model_read: ModelRead):
        self.setdefault(model, [])
        self[model].append(model_read)

    def get_reads_per_model_by_port(self, model):
        """
        Generally there are multiple devices for a given model (e.g. multiple FX inverters), and the way we delineate
        them is by the port (which they are plugged into the Hub with). So it's pretty common to want to get, for each
        model, the ModelReads in a dict <port>: <model_read>. 
        """
        if model not in self:
            return None

        # Read per port - using port=None if no port_number field
        reads_per_port = {}
        ports = []
        for model_reads in self[model]:
            port = None
            if "port_number" in model_reads:
                port = model_reads["port_number"].raw_value
            reads_per_port[port] = model_reads
            ports.append(port)

        # Check we don't have multiple devices with the same port:
        if len(ports) > len(reads_per_port):
            raise RuntimeError("Multiple devices have the same port!")

        return reads_per_port
