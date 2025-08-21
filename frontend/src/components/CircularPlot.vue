<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">SpaceX Ship Inventory and total launches per ship
      </h5>
      <div ref="chart"></div>
      <p class="card-text"></p>
    </div>
  </div>
</template>
<script>
import * as d3 from 'd3';
export default {
  name: 'CircularPlot',
  props: {
    data: {
      type: Array,
      default:[]
    }
  },
  mounted() {
    //console.log(this.data)
    this.createCircularPlot();
  },
  methods: {
    createCircularPlot() {
      const data = this.data;

      const margin = {top: 80, right: 0, bottom: 0, left: 100};
      const width = 980 - margin.left - margin.right;
      const height = 700 - margin.top - margin.bottom;
      const innerRadius = 70;
      const outerRadius = Math.min(width, height) / 1;   // the outerRadius goes from the middle of the SVG area to the border

// append the svg object
      const svg = d3.select(this.$refs.chart)
          .append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform", "translate(" + (width / 2 + margin.left) + "," + (height / 3 + margin.top) + ")");

// Scales
      const x = d3.scaleBand()
          .range([0, 2 * Math.PI])    // X axis goes from 0 to 2pi = all around the circle. If I stop at 1Pi, it will be around a half circle
          .align(0)                  // This does nothing
          .domain(data.map(function(d) { return d.name; })); // The domain of the X axis is the list of states.
      const y = d3.scaleRadial()
          .range([innerRadius, outerRadius])   // Domain will be define later.
          .domain([0, 100]); // Domain of Y is from 0 to the max seen in the data

      // Add the bars
      svg.append("g")
          .selectAll("path")
          .data(data)
          .enter()
          .append("path")
          .attr("fill", "#1a73e8")
          .attr("d", d3.arc()     // imagine your doing a part of a donut plot
              .innerRadius(innerRadius)
              .outerRadius(function(d) { return y(d['launches'].length); })
              .startAngle(function(d) { return x(d.name); })
              .endAngle(function(d) { return x(d.name) + x.bandwidth(); })
              .padAngle(0.02)
              .padRadius(innerRadius))

      // Add the labels
      svg.append("g")
          .selectAll("g")
          .data(data)
          .enter()
          .append("g")
          .attr("text-anchor", function(d) { return (x(d.name) + x.bandwidth() / 2 + Math.PI) % (2 * Math.PI) < Math.PI ? "end" : "start"; })
          .attr("transform", function(d) { return "rotate(" + ((x(d.name) + x.bandwidth() / 2) * 180 / Math.PI - 90) + ")"+"translate(" + (y(d['launches'].length)+10) + ",0)"; })
          .append("text")
          .text(function(d){return(d.name + '  🚀 : '+d.launches.length)})
          .attr("transform", function(d) { return (x(d.name) + x.bandwidth() / 2 + Math.PI) % (2 * Math.PI) < Math.PI ? "rotate(180)" : "rotate(0)"; })
          .style("font-size", "1rem")
          .attr("alignment-baseline", "middle")

    }
  }



}
</script>
