<script setup>
import { RouterLink } from 'vue-router';

</script>

<template>
  <header>
    <h2><a href="/">IFoodSocial</a></h2>
    <nav>
        <RouterLink to="/" class="nav-item">Home</RouterLink>
        <RouterLink to="/other" class="nav-item">Outro</RouterLink>
        <RouterLink to="/disponibilidade" class="nav-item">Disponibilidade</RouterLink>
    </nav>
  </header>
</template>

<style scoped>
  header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    background-color: var(--orange);
    height: 8vh;
    padding: 0vh 4vh;
  }

  h2 a {
    color: var(--white);
    text-decoration: none;
  }

  h2 {
    transform: none;
    transition: transform 0.2s ease-out;
  }

  h2:hover {
    transform: translateX(2vh);
  }

  nav {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .nav-item {
    margin: 0vh 2vh;
    text-decoration: none;
    color: var(--white);
  }

  .nav-item:hover {
    text-decoration: underline;
  }
  
</style>
