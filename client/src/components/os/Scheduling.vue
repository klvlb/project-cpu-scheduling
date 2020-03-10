<template>
  <div>
    <div class='section'>
      <form method='post' id='algo-form'>
        <select id='algo-select' ref='algoSelect' name='algo-list' form='algo-form'>
          <option value='fcfs'>First-Come, First-Served</option>
          <option value='sjf'>Shortest Job First</option>
          <option value='srtf'>Shortest Remaining Time First</option>
          <option value='rr'>Round Robin</option>
          <option value='prio'>Priority Scheduling</option>
          <option value='priorr'>Priority Scheduling with Round Robin</option>
        </select>
        <div id='process-add-container' ref='processAddContainer'>
          <div class='input-block'>
            <label class='input-label'>Arrival</label>
            <input id='arrival-time-input' ref='arrivalTimeInput' type='integer'/>
          </div>
          <div class='input-block'>
            <label>Priority</label>
            <input id='priority-input' ref='priorityInput' type='integer'/>
          </div>
          <div class='input-block'>
            <label>Burst</label>
            <input id='burst-time-input' ref='burstTimeInput' type='integer'/>
          </div>
          <button id='add-process-btn' @click='addProcess' type='button'>Add Process</button>
        </div>
      </form>
    </div>
    <div class='section'>
      <div class='process-list-labels'>
        <span class='list-label'>Process Number</span>
        <span class='list-label'>Arrival</span>
        <span class='list-label'>Priority</span>
        <span class='list-label'>Burst</span>
      </div>
      <ul id='process-list'>
        <li class='process' v-for='(item, index) in processes' v-bind:key=index>
          <div class='entry-block'>
            <span class='process-no'>{{ item.process }}</span>
          </div>
          <div class='entry-block'>
            <span class='process-arrival'>{{ item.arrival }}</span>
          </div>
          <div class='entry-block'>
            <span class='process-priority'>{{ item.priority }}</span>
          </div>
          <div class='entry-block'>
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
    </div>
    <div id='chart'>
      <apexchart name='chart' type='rangeBar' height='350' :options='chartOptions'
                 :series='series'></apexchart>
    </div>
    <div id='awt'>Average waiting time: {{ this.ganttData.awt }} ns</div>
  </div>
</template>

<script src='../../js/scheduling.js'></script>

<style lang='scss' src='../../scss/scheduling.scss'></style>
