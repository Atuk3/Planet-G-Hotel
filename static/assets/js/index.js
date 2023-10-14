// JavaScript code to populate the dropdowns
for (let i = 1; i <= 48; i++) {
    const option = document.createElement("option");
    option.value = i;
    option.text = i;

    document.getElementById("select1").appendChild(option);
    document.getElementById("select2").appendChild(option.cloneNode(true));
    document.getElementById("select3").appendChild(option.cloneNode(true));
}