<template>
    <section class="content">
        <section class="excecao-list">
            <ul v-for="(e, index) in excecaoList" :key="index">
                <li>Empreendimento: {{ e.cod_empreedimento.dcr_nome_fantasia }}</li>
                <li>Data Exceção: {{ e.data_excecao }}</li>
                <li>Tipo Exceção: {{ e.tip_excecao }}</li>
                <li>Abre: {{ e.hora_inicio }}</li>
                <li>Fecha: {{ e.hora_fim }}</li>
                <li>Bairro: {{ e.cod_localidade.cod_bairro.dcr_bairro }}</li>
                <li>Local: {{ e.cod_localidade.dcr_localidade }}</li>
                <section class="btns">
                    <button @click="handleChange(e)">Editar</button>
                    <button @click="handleDelete(index+1)">Excluir</button>
                </section>
            </ul>
        </section>
    </section>
</template>

<script setup>
import { getDisponibilidadeExcecao, deleteDisponibilidadeExcecao } from '@/services/api';
import { reactive } from 'vue';
import { useRouter } from 'vue-router';

const excecaoList = reactive([]);
const router = useRouter();

async function getData() {
    const data = await getDisponibilidadeExcecao();
    excecaoList.splice(0, excecaoList.length, ...data);
    console.log('Exceções: ', excecaoList);
}

function handleChange(e) {
    const dataString = JSON.stringify(e);
    router.push({ name: 'EditDisponExcecao', query: { data: encodeURIComponent(dataString) } });
}

async function handleDelete(id) {
    if (confirm('Tem certeza que deseja excluir este item?')) {
        const response = await deleteDisponibilidadeExcecao(id);
        console.log('Response: ', response.status)
        if (response.status === 204) {
            getData();
        }
    }
}

getData();

</script>

<style scoped>

.content {
    margin-top: 10vh;
}

.excecao-list {
    margin-top: 8vh;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 80%;
    margin: 0 auto;
    align-items: center;
    justify-content: space-evenly;
    gap: 4vh;
}

ul {
    display: flex;
    flex-direction: column;
    width: 320px;
    padding: 2vh;
    background-color: #f5f5f5;
    border-radius: 2vh;
    border: 1px solid var(--orange);
}

ul li {
    list-style-type: none;
}

ul .btns {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 0 2vh;
    margin-top: 2vh;
}

ul .btns button {
    padding: 1vh 2vh;
    background-color: var(--orange);
    color: var(--white);
    border: none;
    border-radius: 2vh;
    cursor: pointer;
}

ul .btns button:hover {
    background-color: var(--orange-hover);
}

</style>