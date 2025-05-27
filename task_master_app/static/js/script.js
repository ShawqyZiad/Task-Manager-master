$('.header a').hover(function() {
    $(this).css('background-color', 'white').css('opacity', '60%').css('border-style', 'outset')
}, function() {
    $(this).css('background-color', 'transparent').css('opacity', '100%').css('border-style', 'none')
})

$('.button-link, .ls-box button').hover(function() {
    $(this).css('background-color', 'transparent').css('color', 'rgba(18,90,133,1)')
}, function() {
    $(this).css('background-color', 'rgba(18,90,133,1)').css('color', 'whitesmoke')
})

$('.logout_link a').click(function() {
    if (confirm("Are you sure you want to logout?") == true) {
        window.location = "process_logout"
    }
})

var nav = document.querySelector('.header');

window.addEventListener('scroll', function() {
    if(window.pageYOffset > 130) {
        nav.classList += ' small';
    } else {
        nav.classList = 'header';
    }
})