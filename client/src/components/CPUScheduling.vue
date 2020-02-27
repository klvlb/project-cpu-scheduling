<template>
  <div>
    <form method="post" id="algo-form">
      <select id="algo" name="algo-list" form="algo-form">
        <option value="fcfs">First-Come, First-Served</option>
        <option value="sjf">Shortest Job First</option>
        <option value="srtf">Shortest Remaining Time First</option>
        <option value="rr">Round Robin</option>
        <option value="ps">Priority Scheduling</option>
      </select>
      <button id="add-process-btn" @click="addProcess">Add Process</button>
      <div id="process-add-container" style="visibility: hidden;">
        <label>Arrival time</label>
        <input id="arrival-time-input" />
        <label>Burst time</label>
        <input id="burst-time-input" />
      </div>
      <div id="process-list">{{ processes }}</div>
    </form>
  </div>
</template>

<script>
const processListEl = document.getElementById("process-list");

const processBtn = new Vue({
  el: "#add-process-btn",
  data: {
    processes: [],
  },
  methods: {
    addProcess: (e) => {
      // e.target.nextSibling.append();
      e.target.disable();
      processListEl.style.visibility = "visible";
      //   const elParent = processListEl.parentNode;
      //   elParent.insertBefore();
    },
  },
});

export default processBtn;

// export default {
//   name: 'CPU Scheduling',
// //   data: {
// //     processes: [],
// //   },
//   methods: {
//     addProcess(el) {
//       // el.
//     },
//     mounted() {
//       this.addProcess();
//     },
//   },
// };
</script>
