<template>
  <main>
    <h2>Disponibilidade</h2>
    <button class="navigate" @click="handleClick">Visualizar Exceções</button>
    <button @click="openModal">Registrar Disponibilidade</button>
    <ModalRegistro :isVisible="isModalVisible" @update:isVisible="isModalVisible = $event" class="modal"/> 
    <DisponibilidadeList />
  </main>
</template>

<script setup>
import DisponibilidadeList from '@/components/DisponibilidadeList.vue';
import ModalRegistro from '@/components/ModalRegistro.vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const isModalVisible = ref(false);
const router = useRouter();

function openModal() {
    isModalVisible.value = true;
}

function handleClick() {
    router.push({ name: 'disponibilidadeExcecao' });
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

main button.navigate {
    padding: 2vh;
    width: 30%;
}

main button:hover {
    background-color: var(--orange-hover);
}

</style>