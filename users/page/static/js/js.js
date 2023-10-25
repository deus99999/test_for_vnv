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

MakeCurrentActiveReference()
