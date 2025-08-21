<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Comparison of mass versus height specifications</h5>
      <div ref="chart"></div>
      <p class="card-text">The size of the circles represents the difference in masses in kilograms on the x-axis and the height on the y-axis in meters.</p>
    </div>
  </div>
</template>
<script>
import * as d3 from 'd3';
export default {
  name: 'ScatterPlot',
  props: {
    data: {
      type: Array,
      default:[]
    }
  },
  mounted() {
    console.log(this.data)
    this.createScatterPlot();
  },
  methods: {
    createScatterPlot() {
      const data = this.data;
      console.log(data)
      const margin = {top: 10, right: 30, bottom: 30, left: 60},
          width = 600 - margin.left - margin.right,
          height = 400 - margin.top - margin.bottom;

      const svg = d3.select(this.$refs.chart)
          .append('svg')
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform", `translate(${margin.left}, ${margin.top})`);

      // // Add X axis
      const x = d3.scaleLinear()
          .domain([0, 1500000 ])
          .range([ 0, width ]);
      svg.append("g")
          .attr("transform", `translate(0, ${height})`)
          .call(d3.axisBottom(x).tickFormat(d=>d+" kg"));

      // Add Y axis
      const y = d3.scaleLinear()
          .domain([0, 150])
          .range([ height, 0]);
      svg.append("g")
          .call(d3.axisLeft(y).ticks(10).tickFormat(d=>d+" m"));

      const radiusScale = d3.scaleLinear()
          .domain([d3.min(data, d => d.mass.kg), d3.max(data, d => d.mass.kg)])
          .range([20, 50]);

      // Add dots
      svg.append('g')
          .selectAll("dot")
          .data(data)
          .join("circle")
          .attr("cx", function (d) { return x(d.mass.kg); } )
          .attr("cy", function (d) { return y(d.height.meters); } )
          .attr("r", d => radiusScale(d.mass.kg))
          .style("fill", "#1a73e8")

      svg.append('g')
          .selectAll("dot")
          .data(data)
          .join("text")
          .text(function(d) { return d.name; }) // Display the 'name' property from your data
          .attr("x", function (d) { return x(d.mass.kg); }) // Adjust x position relative to the group's center
          .attr("y", function (d) { return y(d.height.meters+23); }) // Adjust y position relative to the group's center
          .attr("text-anchor", "middle") // Center the text horizontally
          .attr("dy", "0.35em"); // Vertically align the text in the middle

    }
  }
};
</script>
