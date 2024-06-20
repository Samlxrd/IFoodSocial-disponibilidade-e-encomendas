<template>
  <div class="entrega-view">
    <h1>Agendar Entregas</h1>
    <div class="pedido-lista">
      <div
        v-for="pedido in pedidos"
        :key="pedido.cod_pedido"
        class="pedido-item"
        @click="selecionarPedido(pedido)"
      >
        <span :class="pedido.icon_class"></span>
        <span>{{ pedido.cod_pedido }} - {{ pedido.tip_status }}</span>
      </div>
    </div>

    <div v-if="pedidoSelecionado" class="pedido-detalhes">
      <h2>Pedido {{ pedidoSelecionado.cod_pedido }}</h2>
      <form @submit.prevent="registrarEntrega">
        <div>
          <label for="dataEntrega">Data de Entrega:</label>
          <input type="date" v-model="dataEntrega" required />
        </div>
        <div>
          <label for="endereco">Endereço:</label>
          <input type="text" v-model="endereco" required />
        </div>
        <div>
          <label for="valor">Valor:</label>
          <input type="number" v-model="valor" required />
        </div>
        <div>
          <label for="metodoPagamento">Método de Pagamento:</label>
          <select v-model="metodoPagamento" required>
            <option value="PIX">PIX</option>
            <option value="Cartão de Crédito">Cartão de Crédito</option>
            <option value="Dinheiro">Dinheiro</option>
          </select>
        </div>
        <button type="button" @click="cancelar">Cancelar</button>
        <button type="submit">Registrar</button>
      </form>
    </div>
  </div>
</template>

<script>
import { getPedidos, registrarEntrega } from '@/services/api';
import axios from 'axios'

export default {
  data() {
    return {
      pedidos: [],
      pedidoSelecionado: null,
      dataEntrega: '',
      endereco: '',
      valor: '',
      metodoPagamento: 'PIX',
    };
  },
  async created() {
    const {data} = await axios.get('http://localhost:8000/api/getPedido')
    this.pedidos = data
    console.log(this.pedidos)
  },
  methods: {
    selecionarPedido(pedido) {
      this.pedidoSelecionado = pedido;
      this.dataEntrega = '';
      this.endereco = pedido.endereco || '';
      this.valor = '';
      this.metodoPagamento = 'PIX';
    },
    async registrarEntrega() {
      const dadosEntrega = {
        cod_pedido: this.pedidoSelecionado.cod_pedido,
        data_entrega: this.dataEntrega,
        endereco: this.endereco,
        cod_entrega: 300,
        cod_cidade: 1,
        cod_bairro: 10,
        cod_localidade: 100,
        cod_funcionario: 22,
        valor: this.valor,
        metodo_pagamento: this.metodoPagamento,
      };

      await registrarEntrega(dadosEntrega);
      this.pedidoSelecionado.icon_class = 'entrega-em-andamento';
      this.pedidoSelecionado = null;
    },
    cancelar() {
      this.pedidoSelecionado = null;
    },
  },
};
</script>

<style scoped>
.entrega-view {
  padding: 20px;
}

.pedido-lista {
  display: flex;
  flex-direction: column;
}

.pedido-item {
  cursor: pointer;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
}

.pedido-item span {
  margin-left: 10px;
}

.pedido-detalhes {
  margin-top: 20px;
}

.pedido-detalhes form div {
  margin-bottom: 10px;
}
</style>
