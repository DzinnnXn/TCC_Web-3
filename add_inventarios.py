import os
import django

# Defina as configurações do Django para que o script funcione fora do ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GerenciamentoDePatrimonios.settings")
django.setup()

# Agora fazemos uma importação absoluta
from AppGDP.models import Inventario  

# Lista de inventários para adicionar
inventarios = [
    {"num_inventario": "789076", "denominacao": "ARMARIO BAIXO POST FORM. L-166 -02PB- CADERODE-", "localizacao": "20210066"},
    {"num_inventario": "789078", "denominacao": "ARMARIO BAIXO POST FORM. L-166 -02PB- CADERODE-", "localizacao": "20210066"},
    {"num_inventario": "775954", "denominacao": "CADEIRA FIXA C/4 PES - TECIDO AZUL ROYAL", "localizacao": "20210066"},
    {"num_inventario": "775959", "denominacao": "CADEIRA FIXA C/4 PES - TECIDO AZUL ROYAL", "localizacao": "20210066"},
    {"num_inventario": "775964", "denominacao": "CADEIRA FIXA C/4 PES - TECIDO AZUL ROYAL", "localizacao": "20210066"},
    {"num_inventario": "527070", "denominacao": "CADEIRA P/ SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526155", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526156", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526160", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526161", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526163", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526165", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526172", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526175", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526179", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526180", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526184", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526192", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "526236", "denominacao": "CADEIRA P/SALA DE AULA - DC 1307", "localizacao": "20210066"},
    {"num_inventario": "515519", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525223", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525228", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525230", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525231", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525245", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525256", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525290", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525638", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525662", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525663", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525665", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525675", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525676", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525677", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525680", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525681", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525683", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525684", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525689", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525695", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525698", "denominacao": "CADEIRA P/SALA DE AULA DC 1307", "localizacao": "20210066"},
    {"num_inventario": "525030", "denominacao": "CADEIRA P/SALA DE AULA DC-1307", "localizacao": "20210066"},
    {"num_inventario": "528095", "denominacao": "CADEIRA P/SALA DE AULA DC-1307", "localizacao": "20210066"},
    {"num_inventario": "528099", "denominacao": "CADEIRA P/SALA DE AULA DC-1307", "localizacao": "20210066"},
    {"num_inventario": "1268561", "denominacao": "CARRINHO P/RECARGA 24 NOTEBOOKS/TABLETS", "localizacao": "20210066"},
    {"num_inventario": "1268562", "denominacao": "CARRINHO P/RECARGA 24 NOTEBOOKS/TABLETS", "localizacao": "20210066"},
    {"num_inventario": "777556", "denominacao": "CARTEIRA P/SALA DE AULA TAMPO E PORTA LIVROS", "localizacao": "20210066"},
    {"num_inventario": "777557", "denominacao": "CARTEIRA P/SALA DE AULA TAMPO E PORTA LIVROS", "localizacao": "20210066"},
    {"num_inventario": "777558", "denominacao": "CARTEIRA P/SALA DE AULA TAMPO E PORTA LIVROS", "localizacao": "20210066"}
]

# Inserção em massa
Inventario.objects.bulk_create(
    [Inventario(num_inventario=item['num_inventario'], denominacao=item['denominacao'], localizacao=item['localizacao']) for item in inventarios]
)
