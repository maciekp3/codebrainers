function add_product(){
    var box = document.getElementById("lista");
    var new_div = document.createElement("div");
    var produkt = document.getElementById("my_input").value;
    document.getElementById("my_input").value="";
    new_div.className = "produkt";
    var text = document.createTextNode(produkt);
    new_div.appendChild(text);
    box.appendChild(new_div);
}

