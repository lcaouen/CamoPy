$(document).ready(() => {
	loadData();
});

const swapImages = () => {
	let d = new Date();
	$("#currentImage").attr("src", "/api/currentImage/" + $("#password").val() + "?" + d.getTime());
};

const loadData = () => {
	$.ajax({
		url: "/api/config/" + $("#password").val()
	}).done(data => {
		if (typeof data === "object") {
			let rootKeys = Object.keys(data);
			rootKeys.forEach(rootKey => {
				let keys = Object.keys(data[rootKey]);
				keys.forEach(key => {
					$("#" + key).val(data[rootKey][key]);
				});
			});
			$(".collapse").collapse();
			setInterval(swapImages, 1000);
		}
	});
};
