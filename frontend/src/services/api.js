import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Content-Type': 'application/json'
    }
});

export async function getPedidos() {
    try {
      const response = await api.get('/getPedido');
      return response.data;
    } catch (err) {
      console.error('Falha ao buscar pedidos: ', err);
    }
  }
  
  export async function registrarEntrega(dadosEntrega) {
    try {
      const response = await api.post('/postEntrega', dadosEntrega);
      return response.data;
    } catch (err) {
      console.error('Falha ao registrar entrega: ', err);
    }
  }

export async function getDisponibilidade() {
    try {
        const response = await api.get('/getDisponibilidade');
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar disponibilidade: ', err);
    }
}

export async function getLocalidade() {
    try {
        const response = await api.get('/getLocalidade');
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar localidade: ', err);
    }
}

export async function getEmpreendimento() {
    try {
        const response = await api.get('/getEmpreendimento');
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar empreendimento: ', err);
    }
}

export async function postDisponibilidade(dados) {
    try {
        const response = await api.post('/postDisponibilidade', dados);
        return response;
    } catch (err) {
        console.log('Falha ao enviar disponibilidade: ', err);
    }
}

export async function patchDisponibilidade(dados) {
    try {
        const response = await api.patch(`/patchDisponibilidade/${dados.cod_disponibilidade}/`, dados);
        return response;
    } catch (err) {
        console.log('Falha ao atualizar disponibilidade: ', err);
    }
}

export async function deleteDisponibilidade(id) {
    try {
        const response = await api.delete(`/deleteDisponibilidade/${id}/`);
        return response;
    } catch (err) {
        console.log('Falha ao deletar disponibilidade: ', err);
    }
}

export async function getDisponibilidadeExcecao() {
    try {
        const response = await api.get('/getDisponExcecao');
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar disponibilidade exceção: ', err);
    }
}

export async function postDisponibilidadeExcecao(dados) {
    try {
        const response = await api.post('/postDisponExcecao', dados);
        return response;
    } catch (err) {
        console.log('Falha ao enviar exceção de disponibilidade: ', err);
    }
}

export async function patchDisponibilidadeExcecao(dados) {
    try {
        const response = await api.patch(`/patchDisponExcecao/${dados.cod_dispon_excecao}/`, dados);
        return response;
    } catch (err) {
        console.log('Falha ao atualizar disponibilidade: ', err);
    }
}

export async function deleteDisponibilidadeExcecao(id) {
    try {
        const response = await api.delete(`/deleteDisponExcecao/${id}/`);
        return response;
    } catch (err) {
        console.log('Falha ao deletar exceção de disponibilidade: ', err);
    }
}