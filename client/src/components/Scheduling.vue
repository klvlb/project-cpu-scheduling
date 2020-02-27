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
        <button id='add-process-btn' @click='addProcess' type='button'>Add Process</button>
      </div>
      <ul id='process-list'>
        <li class='process' v-for='(item, index) in processes' v-bind:key=index>
          <div>
            <span class='list-label'>Process Number</span>
            <span class='process-no'>{{ item.process }}</span>
          </div>
          <div>
            <span class='list-label'>Arrival time</span>
            <span class='process-arrival'>{{ item.arrival }}</span>
          </div>
          <div>
            <span class='list-label'>Burst time</span>
            <span class='process-burst'>{{ item.burst }}</span>
          </div>
        </li>
      </ul>
      <button id='algo-form-submit-btn'
        ref='algoFormSubmitBtn'
        @click='submitAlgoForm'
        type='button'
        class='btn btn-primary'>
        Graph
      </button>
    </form>
    {{ calculations }}
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
      calculations: [],
    };
  },
  methods: {
    addProcess() {
      const [arrival, burst] = [
        this.$refs.arrivalTimeInput.value,
        this.$refs.burstTimeInput.value,
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
      const path = 'http://localhost:5000/cpu-scheduling';
      axios.post(path, this.processes)
        .then((res) => {
          this.calculations = res.data;
          console.log('calculations', this.calculations);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
