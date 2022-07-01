//Dynamic fill creation

const addBtn=document.querySelector(".add");

const input=document.querySelector(".inp-group");

function removeInput(){
    this.parentElement.remove();
}

function addInput(){
   
    
    const value=document.createElement("input");
    value.type="text";
    value.placeholder="Ingresa el valor"
 
    const btn=document.createElement("a");
    btn.className="delete";
    btn.innerHTML="&times";

    btn.addEventListener("click", removeInput);

    const flex=document.createElement("div");
    flex.className="flex";

    input.appendChild(flex);
    flex.appendChild(value);
    flex.appendChild(btn);

}

addBtn.addEventListener("click",addInput);