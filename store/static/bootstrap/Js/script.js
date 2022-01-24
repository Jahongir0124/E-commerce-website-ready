const menu_btn = document.querySelector('#menu_btn');
const navigation = document.querySelector('.navbar_a');
const close_btn = document.querySelector('#close');
const navItems = document.querySelectorAll('.navbar_a a');
const upbtn = document.querySelector('.btn-up');
const upbtndiv = document.querySelector('.up-btn');
const loader = document.querySelector('.loader');
function showLoader() {
    loader.style.display = 'none';
}
const timer = setTimeout(showLoader,3000);
menu_btn.addEventListener('click',()=>{
    navigation.classList.toggle('active');
    close_btn.style.display='block';
    
});

close_btn.addEventListener('click',()=>{
    navigation.classList.remove('active');
    menu_btn.style.display='block';
    close_btn.style.display='none';
});

navItems.forEach(item=>{
    item.addEventListener('click',()=>{
        navigation.classList.remove('active');
        close_btn.style.display='none';

    });
});

window.addEventListener('scroll',()=>{
    upbtndiv.classList.toggle('active',window.scrollY>300);
});
upbtn.addEventListener('click',()=>{
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
});

