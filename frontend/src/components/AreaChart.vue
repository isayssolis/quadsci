<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Space launches per year</h5>
      <div ref="chart"></div>
      <p class="card-text"></p>
    </div>
  </div>
</template>
<script>
import * as d3 from 'd3';
export default {
  name: 'AreaChart',
  props: {
    data: {
      type: Array,
      default:[]
    }
  },
  mounted() {
    //console.log(this.data)
    this.createAreaChart();
  },
  methods: {

    createAreaChart() {
      const data = this.data;
      console.log(data)
      // const formatTime = d3.timeParse("%Y-%m-%d");
      // console.log(formatTime("2013-04-28"))
      //console.log(d3.isoParse("2006-03-17T00:00:00.000Z"))


// set the dimensions and margins of the graph
      const margin = {top: 10, right: 30, bottom: 30, left: 50},
          width = 460 - margin.left - margin.right,
          height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
      const svg = d3.select(this.$refs.chart)
          .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");


      // date format
      const x = d3.scaleTime()
          //.domain([d3.extent(data, function(d) { return d3.isoParse(d.static_fire_date_utc) })])
          .domain(d3.extent(data, function(d) { return d3.isoParse(d.static_fire_date_utc) }))
          .range([ 0, width ]);
      svg.append("g")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x));

      // Add Y axis
      const y = d3.scaleLinear()
          .domain([0, d3.max(data, function(d,i) { return i; })])
          .range([ height, 0 ]);
      svg.append("g")
          .call(d3.axisLeft(y));

      // Add the area
      svg.append("path")
          .datum(data)
          .attr("fill", "#cce5df")
          .attr("stroke", "green")
          .attr("stroke-width", 1.5)
          .attr("d", d3.area()
              .x(function(d) { return x(d3.isoParse(d.static_fire_date_utc)) })
              .y0(y(0))
              .y1(function(d,i) { return y(i+1) })
          )

    } //createAreaChar()
  } //methods


}
</script>
