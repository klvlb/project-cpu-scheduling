<template>
  <div>
    <form method='post' id='algo-form'>
      <select id='algo' name='algo-list' form='algo-form'>
        <option value='fcfs'>First-Come, First-Served</option>
        <option value='sjf'>Shortest Job First</option>
        <option value='srtf'>Shortest Remaining Time First</option>
        <option value='rr'>Round Robin</option>
        <option value='ps'>Priority Scheduling</option>
      </select>
      <div id='process-add-container' ref='processAddContainer'>
        <label>Arrival time</label>
        <input id='arrival-time-input' ref='arrivalTimeInput' type='integer' />
        <label>Burst time</label>
        <input id='burst-time-input' ref='burstTimeInput' type='integer' />
        <button id='add-process-btn' @click='addProcess'>Add Process</button>
      </div>
      <button id='algo-form-submit-btn'
        ref='algoFormSubmitBtn'
        @click='submitAlgoForm'
        class='btn btn-primary'>
        Graph
      </button>
    </form>
    <div id='process-list'>
      {{ processes }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Scheduling',
  data() {
    return {
      processes: [],
      processCount: 1,
    };
  },
  methods: {
    addProcess() {
      const [arrival, burst] = [
        this.$refs.arrivalTimeInput.value,
        this.$refs.arrivalTimeInput.value,
      ];
      if (burst && arrival) {
        this.processes.push({
          process: this.processCount,
          arrival,
          burst,
        });
        this.processCount += 1;
      }
    },
    submitAlgoForm() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
