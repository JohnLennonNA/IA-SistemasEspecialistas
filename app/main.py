from pyknow import *
from facts.Gatilho import Gatilho
from know_engine.Logistica import Logistica

motor = Logistica()
motor.reset()

motor.declare(Gatilho(perfil='Natureba'))
motor.declare(Gatilho(fome='Faminto'))
motor.declare(Gatilho(horario='Almoço'))

motor.run()