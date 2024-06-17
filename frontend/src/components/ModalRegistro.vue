<!-- ModalComponent.vue -->
<template>
    <div class="modal" v-if="isVisible">
      <div class="modal-content">
        <form @submit.prevent="handleSubmit">
      <div>
        <label for="num_dia_semana">Número de Dias da Semana:</label>
        <input type="number" id="num_dia_semana" v-model="form.num_dia_semana" min="1" max="7" required>
      </div>
      <div>
        <label for="hora_inicio">Hora de Início:</label>
        <input type="datetime-local" id="hora_inicio" v-model="form.hora_inicio" required>
      </div>
      <div>
        <label for="hora_fim">Hora de Fim:</label>
        <input type="datetime-local" id="hora_fim" v-model="form.hora_fim" required>
      </div>
      <div>
        <label for="localidade">Localidade:</label>
        <select id="localidade" v-model="form.cod_localidade" required>
          <option v-for="localidade in localidades" :key="localidade.cod_localidade" :value="localidade.cod_localidade">
            {{ localidade.dcr_localidade }}
          </option>
        </select>
      </div>
      <div>
        <label for="empreendimento">Empreendimento:</label>
        <select id="empreendimento" v-model="form.cod_empreedimento" required>
          <option v-for="empreendimento in empreendimentos" :key="empreendimento.cod_empreedimento" :value="empreendimento.cod_empreedimento">
            {{ empreendimento.dcr_empreendimento }}
          </option>
        </select>
      </div>
      
      <div class="btns">
        <button>Registrar</button>
        <button @click="closeModal">Fechar</button>
      </div>
    </form>
      </div>
    </div>
  </template>
  
  <script>
import { getLocalidade, getEmpreendimento, postDisponibilidade, getDisponibilidade } from '@/services/api';
import { onMounted } from 'vue';
import { reactive } from 'vue';

  export default {
    data() {
      return {
        form: {
          num_dia_semana: '',
          hora_inicio: '',
          hora_fim: '',
          cod_localidade: '',
          cod_empreedimento: ''
        },
        localidades: [],
        empreendimentos: []
      }
    },
    props: ['isVisible'],
    methods: {
      closeModal() {
        this.$emit('update:isVisible', false); // Atualiza a propriedade para fechar o modal
      },
      async handleSubmit() {
        try {
          console.log('Formulario: ', this.form);
          const response = await postDisponibilidade(this.form);
          console.log('Resposta: ', response)
          if (response.status === 201)
            this.closeModal();
            getDisponibilidade();

        } catch (err) {
          console.error("Failed to fetch data:", err);
        }
      }
      
    },
    setup() {
      const localidades = reactive([]);
      const empreendimentos = reactive([]);
  
      onMounted(async () => {
        try {
          const response = await getLocalidade();
          localidades.splice(0, localidades.length, ...response);
          const response2 = await getEmpreendimento();
          empreendimentos.splice(0, empreendimentos.length, ...response2);

          console.log(localidades);
          console.log(empreendimentos);
        } catch (error) {
          console.error("Failed to fetch data:", error);
        }
      });
  
      return {
        localidades,
        empreendimentos,
      };
    }
  }
  
  </script>

<style scoped>

.modal button {
  display: block;
    margin: 4vh auto;
    padding: 1vh 2vh;
    background-color: var(--orange);
    color: var(--white);
    border: none;
    border-radius: 2vh;
    cursor: pointer;
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

.btns {
  display: flex;
  flex-direction: row;
  gap: 5vh;
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

.modal form select, input {
  width: 100px;
  margin-bottom: 1vh;
  margin-left: 1vh;
}

</style>