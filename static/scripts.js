
/*===== MENU SHOW =====*/
const myMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show')
        })
    }
}
myMenu('menu_bar','nav_menu')

/*===== ACTIVE AND REMOVE MENU =====*/
const myLink = document.querySelectorAll('.nav__link');

function linkAction(){
  /*Active link*/
  myLink.forEach(n => n.classList.remove('active'));
  this.classList.add('active');

  /*Remove menu mobile*/
  const myMenu = document.getElementById('nav_menu')
  myMenu.classList.remove('show')
}
