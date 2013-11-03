(function($) {
	function add(unit, a, b) {
		var s = 0;
		for (var i = 1; i < arguments.length; i++)
			s += parseInt(arguments[i], 10);
		return s + unit;
	}
	$(document).ready(function() {
		var $body = $("body"),
			$sidebar = $(".sidebar"),
			$label = $(".sidebar-label"),
			$bodyWrapper = $(".sidebar-body-wrapper");

		var labelWidth = $label.css("width"),
			bodyWidth = "250px",
			bodyPadding = "10px",
			// total width
			sidebarWidth = add("px", labelWidth, bodyWidth, bodyPadding, bodyPadding);

		console.log(sidebarWidth);
		$sidebar.hover(function() {
			$bodyWrapper.css({
				width: bodyWidth,
				"padding-left": bodyPadding,
				"padding-right": bodyPadding
			});
			$body.css("padding-left", sidebarWidth);
		}, function() {
			$bodyWrapper.css({
				width: "",
				"padding-left": "0",
				"padding-right": "0"
			});
			$body.css("padding-left", "");
		});
	});
})(jQuery);