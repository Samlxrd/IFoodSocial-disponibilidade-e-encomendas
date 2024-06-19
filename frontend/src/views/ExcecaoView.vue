<template>
    <main>
        <h2>Disponibilidade Exceção</h2>
        <button class="navigate" @click="handleClick">Visualizar Disponibilidade</button>
        <button @click="openModal">Registrar Exceção</button>
        <ModalRegistroExcecao :isVisible="isModalVisible" @update:isVisible="isModalVisible = $event" class="modal"/>
        <ExcecaoList/>
    </main>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import ExcecaoList from '@/components/ExcecaoList.vue';
import ModalRegistroExcecao from '@/components/ModalRegistroExcecao.vue';

const isModalVisible = ref(false);
const router = useRouter();

function openModal() {
    isModalVisible.value = true;
}

function handleClick() {
    router.push({ name: 'disponibilidade' });
}

</script>

<style scoped>

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

h2 {
    text-align: center;
    margin: 2vh;
}

</style>