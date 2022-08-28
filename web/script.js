async function passwords(){
    let num = document.getElementById('location').value;
    let res = await eel.generator(num)();
    document.getElementById('info').innerHTML = res;
}

document.querySelector(".boom").onclick = function(){
    passwords();
    }


