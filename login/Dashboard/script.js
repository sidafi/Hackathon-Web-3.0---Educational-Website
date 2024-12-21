function changeContent(page, element) {
    const contentDiv = document.getElementById('content');

    if (page === 'belajar') {
        contentDiv.innerHTML = `
            <h1>Belajar</h1>
        `;
    } else if (page === 'materi') {
        contentDiv.innerHTML = `
            <h1>Materi</h1>
        `;
    } else if (page === 'kuis') {
        contentDiv.innerHTML = `
            <h1>Kuis</h1>
        `;
    } else if (page === 'prestasi') {
        contentDiv.innerHTML = `
            <h1>Prestasi</h1>
        `;
    } else if (page === 'home') {
        contentDiv.innerHTML = `
            <h1>Welcome to Home</h1>\
        `;
    } else if (page === 'timer') {
        contentDiv.innerHTML = `
            <h1>Timer</h1>
        `;
    } else if (page === 'notifications') {
        contentDiv.innerHTML = `
            <h1>Notifications</h1>
        `;
    }

    const allLinks = document.querySelectorAll('.sidebar ul li a');
    const allButtons = document.querySelectorAll('.sidebar-btn');

    allLinks.forEach(link => link.classList.remove('active'));
    allButtons.forEach(button => button.classList.remove('active'));

    if (element.tagName === 'A') {
        element.classList.add('active');
    } else if (element.tagName === 'BUTTON') {
        element.classList.add('active');
    }
}

window.onload = function() {
    changeContent('home', document.querySelector('.sidebar ul li a'));
}
