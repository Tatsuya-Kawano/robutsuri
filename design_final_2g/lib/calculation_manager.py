from container import Container
from container_controller import ContainerController


class CalculationManager:

    def __init__(self, param):
        geom = param['geometry']
        delta = param['mesh_width']
        albedo = param['albedo']

        container = Container(geom, delta, albedo)
        self.controller = ContainerController(container)

    def run(self):
        return self.controller.calc()

    def get_keff(self):
        return self.controller.get_keff()

