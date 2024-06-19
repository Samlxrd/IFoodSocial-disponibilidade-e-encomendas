<template>
  <main>
    <h2>Disponibilidade</h2>
    <button @click="openModal">Registrar Disponibilidade</button>
    <ModalRegistro :isVisible="isModalVisible" @update:isVisible="isModalVisible = $event" class="modal"/> 
    <DisponibilidadeList />
  </main>
</template>

<script setup>
import DisponibilidadeList from '@/components/DisponibilidadeList.vue';
import ModalRegistro from '@/components/ModalRegistro.vue';
import { ref } from 'vue';
/* 
const form = ref({
    num_dia_semana: '',
    hora_inicio: '',
    hora_fim: '',
    localidade: '',
    empreendimento: ''
});*/

const isModalVisible = ref(false);

function openModal() {
    isModalVisible.value = true;
} 

</script>

<style scoped>
h2 {
    text-align: center;
    margin: 2vh;
}

main button {
    display: block;
    margin: 4vh auto;
    padding: 1vh 2vh;
    background-color: var(--orange);
    color: var(--white);
    border: none;
    border-radius: 2vh;
    cursor: pointer;
    transform: translateY(5vh);
}

main button:hover {
    background-color: var(--orange-hover);
}

.modal {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1;
}

.modal form {
    background-color: var(--white);
    padding: 5vh;
    border-radius: 2vh;
}

</style>