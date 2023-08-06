let home_btn = document.getElementById('home_btn');
let credits_btn = document.getElementById('credits_btn');

home_btn.addEventListener('click', ()=>{
    window.location = './';
});

credits_btn.addEventListener('click', ()=>{
    window.location = 'https://github.com/Boubajoker/SearchGooglePy/blob/master/ThirdPartyNotice.md';
});