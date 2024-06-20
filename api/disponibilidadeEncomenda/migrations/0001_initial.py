# Generated by Django 5.0.6 on 2024-06-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoPedido',
            fields=[
                ('cod_avaliacao_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('num_nota_avaliacao', models.IntegerField(blank=True, null=True)),
                ('txt_avaliacao', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'AVALIACAO_PEDIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('cod_bairro', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_bairro', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'BAIRRO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('cod_cardapio', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_cardapio', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_titulo_apres', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'CARDAPIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cod_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_categoria', models.CharField(blank=True, max_length=45, null=True)),
                ('img_categoria', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'CATEGORIA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('cod_cidade', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_cidade', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'CIDADE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cod_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_endereco', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_complemento', models.CharField(blank=True, max_length=45, null=True)),
                ('num_cep', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'CLIENTE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DisponExcecao',
            fields=[
                ('cod_dispon_excecao', models.AutoField(primary_key=True, serialize=False)),
                ('data_excecao', models.DateTimeField(blank=True, null=True)),
                ('tip_excecao', models.CharField(blank=True, max_length=1, null=True)),
                ('hora_inicio', models.DateTimeField(blank=True, null=True)),
                ('hora_fim', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DISPON_EXCECAO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('cod_disponibilidade', models.AutoField(primary_key=True, serialize=False)),
                ('num_dia_semana', models.IntegerField(blank=True, null=True)),
                ('hora_fim', models.DateTimeField(blank=True, null=True)),
                ('hora_inicio', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DISPONIBILIDADE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('cod_empreedimento', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_empreendimento', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_nome_fantasia', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_endereco', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_complemento', models.CharField(blank=True, max_length=45, null=True)),
                ('num_cep', models.CharField(blank=True, max_length=10, null=True)),
                ('img_empreendimento', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'EMPREENDIMENTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmprendFuncionario',
            fields=[
                ('cod_emprend_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('tip_funcionario', models.CharField(blank=True, max_length=1, null=True)),
                ('img_emprend_funcionario', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'EMPREEND_FUNCIONARIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('cod_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('data_saida', models.DateTimeField(blank=True, null=True)),
                ('data_entrega', models.DateTimeField(blank=True, null=True)),
                ('vlr_entrega', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('dcr_endereco', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_complem', models.CharField(blank=True, max_length=45, null=True)),
                ('num_cep', models.CharField(blank=True, max_length=10, null=True)),
                ('txt_referencia', models.CharField(blank=True, max_length=45, null=True)),
                ('flag_encomenda', models.CharField(blank=True, max_length=1, null=True)),
                ('flag_entregador', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'ENTREGA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('cod_evento', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_evento', models.CharField(blank=True, max_length=45, null=True)),
                ('num_ordem_evento', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'EVENTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormaPagto',
            fields=[
                ('cod_forma_pagto', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_forma_pagto', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'FORMA_PAGTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('cod_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome_funcionario', models.CharField(blank=True, max_length=45, null=True)),
                ('num_telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('dcr_email', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'FUNCIONARIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('cod_item_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('vlr_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('qtd_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('vlr_total', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'ITEM_PEDIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidade',
            fields=[
                ('cod_localidade', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_localidade', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'LOCALIDADE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('cod_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('tip_pedido', models.CharField(blank=True, max_length=1, null=True)),
                ('data_pedido', models.DateTimeField(blank=True, null=True)),
                ('vlr_pedido', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('dcr_dados_pagto', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'PEDIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('cod_produto', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_produto', models.CharField(blank=True, max_length=45, null=True)),
                ('img_produto', models.BinaryField(blank=True, null=True)),
                ('vlr_produto', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('flag_disponivel', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'PRODUTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RastreamentoPedido',
            fields=[
                ('cod_rastreamento_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('data_hora_evento', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'RASTREAMENTO_PEDIDO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SecaoCardapio',
            fields=[
                ('cod_secao_cardapio', models.AutoField(primary_key=True, serialize=False)),
                ('dcr_secao_cardapio', models.CharField(blank=True, max_length=45, null=True)),
                ('dcr_titulo_apres', models.CharField(blank=True, max_length=45, null=True)),
                ('num_ordem', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'SECAO_CARDAPIO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SecaoProduto',
            fields=[
                ('cod_secao_produto', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('num_ordem', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'SECAO_PRODUTOS',
                'managed': False,
            },
        ),
    ]
