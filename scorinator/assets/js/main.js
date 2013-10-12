$(document).ready(function() {
    $("span.score").tooltip({
        placement: 'right'
    });

    /* handle charting */
    var w = 300;
    var h = 150;
    var max = d3.max(chart_dataset);
    var padding = 10;

    var x = d3.scale.linear()
        .domain([0, chart_dataset.length - 1]).range([0 + padding, w - padding * 2]);

    var y = d3.scale.linear()
        .domain([0, max]).range([h - padding, 0 + padding * 2]);

    var line = d3.svg.line()
        .x(function(d, i) { return x(i); })
        .y(function(d) { return y(d); });

    vis = d3.select("div#chart-scores").append("svg:svg").attr("width", w).attr("height", h);

    vis.selectAll("path.line").data([chart_dataset]).enter().append("svg:path")
        .attr("d", line);

    vis.selectAll("circle").data(chart_dataset).enter().append("svg:circle")
        .attr("cx", function(d, i) { return x(i); })
        .attr("cy", function(d) { return y(d); })
        .attr("r", 5);

    vis.selectAll("text").data(chart_dataset).enter().append("svg:text")
        .text(function(d) { return d; })
        .attr("x", function(d, i) { return x(i) - 7; })
        .attr("y", function(d) { return y(d) - 7; });
});
