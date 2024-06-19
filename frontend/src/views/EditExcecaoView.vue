<template>
    <form @submit.prevent="saveChanges" class="form-container">
        <label for="empreendimento">Empreendimento</label>
        <input id="empreendimento" v-model="formData.cod_empreedimento.dcr_nome_fantasia" placeholder="Nome Fantasia" disabled>
        
        <label for="tip_excecao">Tipo Exceção:</label>
        <input type="text" id="tip_excecao" v-model="formData.tip_excecao" maxlength="1" required>

        <label for="data_excecao">Data da Exceção:</label>
        <input type="datetime-local" id="data_excecao" v-model="formData.data_excecao" required>

        <label for="hora-inicio">Hora de Início</label>
        <input type="datetime-local" id="hora_inicio" v-model="formData.hora_inicio" placeholder="Hora de Início">
        
        <label for="hora-fim">Hora de Fim</label>
        <input type="datetime-local" id="hora_fim" v-model="formData.hora_fim" placeholder="Hora de Fim">
        
        <label for="bairro">Bairro</label>
        <input id="bairro" v-model="formData.cod_localidade.cod_bairro.dcr_bairro" placeholder="Bairro">
        
        <label for="localidade">Localidade</label>
        <input id="localidade" v-model="formData.cod_localidade.dcr_localidade" placeholder="Localidade">
        
        <button type="submit">Salvar</button>
        <button @click="cancel">Cancelar</button>
    </form>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { patchDisponibilidadeExcecao } from '@/services/api';

const route = useRoute();
const router = useRouter();

const formData = route.query.data ? JSON.parse(decodeURIComponent(route.query.data)) : null;
if (formData) {
    formData.data_excecao = formatDateTimeLocal(formData.data_excecao);
    formData.hora_inicio = formatDateTimeLocal(formData.hora_inicio);
    formData.hora_fim = formatDateTimeLocal(formData.hora_fim);
}

function formatDateTimeLocal(isoString) {
  if (!isoString) return '';
  const date = new Date(isoString);
  const localISOTime = (new Date(date)).toISOString().slice(0,16);
  return localISOTime;
}

console.log('Dados do item: ', formData);

async function saveChanges() {
    try {
        const data = {
            cod_dispon_excecao: formData.cod_dispon_excecao,
            tip_excecao: formData.tip_excecao,
            data_excecao: formData.data_excecao,
            hora_inicio: formData.hora_inicio,
            hora_fim: formData.hora_fim,
            cod_localidade: formData.cod_localidade.cod_localidade,
            cod_empreedimento: formData.cod_empreedimento.cod_empreedimento
        }

        const response = await patchDisponibilidadeExcecao(data);
        if (response.status === 200) {
            router.back();
        }
    } catch (error) {
        console.error('Erro ao salvar alterações: ', error);
    }
}

function cancel() {
    router.back();
}

</script>

<style scoped>
form {
    background-color: var(--white);
    padding: 2vh;
    border-radius: 2vh;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

form input,
form select,
form textarea {
    width: 100%;
    padding: 1vh;
    margin: 1vh 0;
    border: 1px solid #ccc;
    border-radius: 1vh;
}

form button {
    display: block;
    width: auto;
    padding: 1vh 2vh;
    margin: 2vh auto;
    background-color: var(--orange);
    color: var(--white);
    border: none;
    border-radius: 2vh;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

form button:hover {
    background-color: var(--orange-hover);
}

.form-container {
  max-width: 60%;
  min-width: 40%;
  margin: auto;
}

label {
  display: block;
  margin-top: 20px;
}

input, button {
  display: block;
  width: 100%;
  margin-top: 5px;
}

</style>