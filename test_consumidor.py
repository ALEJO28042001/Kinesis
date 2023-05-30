from Consumidor_Limite_Superior import comprobacion_clasificacion as comprobacion_limite_Superior
from Consumidor_Limite_Inferior import comprobacion_clasificacion as comprobacion_limite_Inferior
import json

def test_conection():
    assert comprobacion_limite_Superior(1) > 0
    assert comprobacion_limite_Superior(2) > 0
    assert comprobacion_limite_Superior(10) < 0
    assert comprobacion_limite_Superior(70) < 0
    assert comprobacion_limite_Superior(60) < 0
    assert comprobacion_limite_Inferior(1) > 0
    assert comprobacion_limite_Inferior(2) > 0
    assert comprobacion_limite_Inferior(10) < 0
    assert comprobacion_limite_Inferior(70) < 0
    assert comprobacion_limite_Inferior(60) < 0