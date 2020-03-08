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
      // this.algo = this.$refs.algoSelect.value;
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
        // processes: this.processes,
        processes: JSON.stringify(this.processes),
      };
      console.log(data);
      $.ajax({
        url: path,
        type: 'POST',
        data,
        // data: JSON.stringify(data),
        // contentType: 'application/json',
        dataType: 'json',
        beforeSend: (x) => {
          if (x && x.overrideMimeType) {
            // x.overrideMimeType('application/json');
            x.overrideMimeType('application/json;charset=UTF-8');
          }
        },
        success: (result) => {
          this.ganttData = result;
          // this.ganttData = JSON.parse(result);
          console.log(this.ganttData);
          console.log(this.ganttData.sequence);
        },
      });
      // axios.post(path, {
      //   algo: this.algo.toString(),
      //   // processes: JSON.stringify(this.processes),
      // })
      //   .then((res) => {
      //     this.calculations = res.data;
      //     // console.log('calculations', this.calculations);
      //   })
      //   .catch((error) => {
      //     // eslint-disable-next-line
      //     console.error(error);
      //   });
      // // Format nested params correctly
      // axios.interceptors.request.use(config => {
      //
      //   config.paramsSerializer = params => {
      //     // Qs is not included in the Axios package
      //     return Qs.stringify(params, {
      //       arrayFormat: "brackets",
      //       encode: false
      //     });
      //   };
      //
      //   return config;
      // });
    },
  },
};
