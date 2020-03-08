import $ from 'jquery';


export default {
  name: 'Scheduling',
  data() {
    return {
      processes: [],
      processCount: 1,
      calculations: [],
      algo: '',
      ganttData: {},
    };
  },
  methods: {
    addProcess() {
      const [arrival, priority, burst] = [
        this.$refs.arrivalTimeInput.value,
        this.$refs.priorityInput.value,
        this.$refs.burstTimeInput.value,
      ];
      if (burst && arrival && priority) {
        this.processes.push({
          process: this.processCount,
          arrival,
          priority,
          burst,
        });
        this.processCount += 1;
      }
    },
    submitAlgoForm() {
      const path = 'http://localhost:5000/cpu-scheduling';
      this.algo = this.$refs.algoSelect.value;
      const data = {
        algo: this.algo,
        processes: JSON.stringify(this.processes),
      };
      console.log(data);
      $.ajax({
        url: path,
        type: 'POST',
        data,
        dataType: 'json',
        beforeSend: (x) => {
          if (x && x.overrideMimeType) {
            x.overrideMimeType('application/json;charset=UTF-8');
          }
        },
        success: (result) => {
          this.ganttData = result;
        },
      });
    },
  },
};
