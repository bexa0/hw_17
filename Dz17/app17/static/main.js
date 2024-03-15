const input_title = document.querySelector('#id_title')
const input_priority = document.querySelector('#id_priority')
const input_deadline = document.querySelector('#id_deadline')
const body = document.querySelector('body')
let curr_theme = 'black'
console.log(window.location.href)

if(window.location.href == 'http://127.0.0.1:8000/create/' || window.location.href == 'http://127.0.0.1:8000/update//\\b\\d+(\\.\\d+)?\\b/g'){
    input_title.addEventListener('focus', function (e){
        input_title.parentElement.classList.add('focus')
    })
    input_priority.addEventListener('focus', function (e){
        input_priority.parentElement.classList.add('focus')
    })
    input_deadline.addEventListener('focus', function (e){
        input_deadline.parentElement.classList.add('focus')
    })

    input_title.addEventListener('blur', function (e){
        if(input_title.value === ''){
            input_title.parentElement.classList.remove('focus')
        }
    })
}


const getTheme = () =>{
    const theme = document.getElementsByName('theme')
    for(let i = 0; i < theme.length; i++){
        if(theme[i].checked){
            let ii = localStorage.setItem('theme', theme[i].value)
            return ii
        }
    }
}


if(window.location.href == 'http://127.0.0.1:8000/settings/'){
    const con = document.querySelector('.confrim')
    con.addEventListener('click', function (e){
        getTheme()
    })
}
if (body.classList.value == 'black'){
    body.classList.remove('blask')
    body.classList.add(localStorage.getItem('theme'))
}
else if(body.classList.value == 'white'){
    body.classList.remove('white')
    body.classList.add(localStorage.getItem('theme'))
}