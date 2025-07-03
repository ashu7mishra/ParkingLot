class GateRepo:
    def __init__(self):
        self.gate_map = {}

    def find_gate_by_id(self, id):
        if id in self.gate_map:
            return self.gate_map[id]
        return None