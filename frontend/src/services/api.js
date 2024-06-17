import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        'Content-Type': 'application/json'
    }
});

export async function getDisponibilidade() {
    try {
        const response = await api.get('/getDisponibilidade');
        console.log('Dados ', response)
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar disponibilidade: ', err);
    }
}

export async function getLocalidade() {
    try {
        const response = await api.get('/getLocalidade');
        console.log('Dados ', response)
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar localidade: ', err);
    }
}

export async function getEmpreendimento() {
    try {
        const response = await api.get('/getEmpreendimento');
        console.log('Dados ', response)
        return response.data;
    } catch (err) {
        console.log('Falha ao buscar empreendimento: ', err);
    }
}

export async function postDisponibilidade(dados) {
    try {
        console.log('Dados enviados:', dados);
        const response = await api.post('/postDisponibilidade', dados);
        return response;
    } catch (err) {
        console.log('Falha ao enviar disponibilidade: ', err);
    }
}