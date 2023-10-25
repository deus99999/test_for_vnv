function MakeCurrentActiveReference() {
	// Получаем текущий URL страницы
	var currentUrl = window.location.pathname;
	// Находим соответствующую ссылку в меню и устанавливаем ей класс 'active'
	document.querySelectorAll(".nav a").forEach(function(link) {
    if (link.getAttribute("href") === currentUrl) {
       	link.classList.add("active");
    	}
	});
}


// function onclick() {
//   $.ajax({
//     url: 'delete_user/',
//     success: function() {
//       confirm('Are You sure?');
//    }
//   })
// }


MakeCurrentActiveReference()
