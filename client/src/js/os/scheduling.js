import $ from 'jquery';
import ApexCharts from 'apexcharts';


export default {
  name: 'Scheduling',
  data() {
    return {
      processes: [],
      processCount: 1,
      calculations: [],
      algo: '',
      ganttData: {
        awt: 0,
      },
      series: [],
      chartOptions: {
        chart: {
          height: 350,
          type: 'rangeBar',
        },
        plotOptions: {
          bar: {
            horizontal: true,
            distributed: true,
            dataLabels: {
              hideOverflowingLabels: false,
            },
          },
        },
        xaxis: {
          type: 'numeric',
        },
        yaxis: {
          show: true,
        },
        series: this.series,
        dataLabels: {
          enabled: true,
          grid: {
            row: {
              colors: ['#f3f4f5', '#567'],
              opacity: 1,
            },
          },
        },
      },
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
        quantum: this.$refs.quantumTimeInput.value,
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
          this.ganttData = {
            sequence: result.sequence,
            awt: result.ave_waiting_time,
          };
          console.log(this.ganttData);
          // this.chartOptions.series = this.series;
          this.createChart();
        },
      });
    },
    createChart() {
      this.series = [{
        data: [],
      }];
      let g = '0x0';
      let b = '0x0';
      for (let i = 0; i < this.ganttData.sequence.length; i += 1) {
        const item = this.ganttData.sequence[i];
        g += '0xa0';
        b += '0x10';
        this.series[0].data.push({
          x: `P${item.process}`,
          y: [
            item.start_time,
            item.end_time,
          ],
          fillColor: this.fullColorHex(100, g, b),
        });
      }
      this.chartOptions.series = this.series;
      const chart = new ApexCharts(document.querySelector('#chart'), this.chartOptions);
      chart.render();
    },
    fullColorHex(r, g, b) {
      const red = this.rgbToHex(r);
      const green = this.rgbToHex(g);
      const blue = this.rgbToHex(b);
      return red + green + blue;
    },
    rgbToHex(c) {
      let hex = Number(c).toString(16);
      if (hex.length < 2) {
        hex = `'0'${hex}`;
      }
      return hex;
    },
  },
};
