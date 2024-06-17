<template>
    <section class="content">
        <section class="disp-list">
            <ul v-for="(d, index) in dispList" :key="index">
                <li>Empreendimento: {{ d.cod_empreedimento.dcr_nome_fantasia }}</li>
                <li>Dias na semana: {{ d.num_dia_semana }}</li>
                <li>Abre: {{ d.hora_inicio }}</li>
                <li>Fecha: {{ d.hora_fim }}</li>
                <li>Bairro: {{ d.cod_localidade.cod_bairro.dcr_bairro }}</li>
                <li>Local: {{ d.cod_localidade.dcr_localidade }}</li>
            </ul>
        </section>
    </section>
</template>

<script setup>
import { getDisponibilidade } from '@/services/api';
import { reactive } from 'vue';

const dispList = reactive([]);

async function getData() {
    const data = await getDisponibilidade();
    dispList.splice(0, dispList.length, ...data);
}

getData();

</script>

<style scoped>

.content {
    margin-top: 10vh;
}

.disp-list {
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
}

ul li {
    list-style-type: none;
    
}
</style>