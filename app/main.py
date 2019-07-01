from app.facts.Gatilho import Gatilho
from app.know_engine.Logistica import Logistica

mt_log = Logistica()
mt_log.reset()

mt_log.declare(Gatilho(perfil='Natureba'))
mt_log.declare(Gatilho(fome='Faminto'))
mt_log.declare(Gatilho(horario='Almoço'))

mt_log.run()
