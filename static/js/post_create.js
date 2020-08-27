FReader = new FileReader();
         
// событие, когда файл загрузится
FReader.onload = function(e) {
    document.querySelector("#result").src = e.target.result;
    document.querySelector("#result").classList.remove("display_none");
    document.querySelector("#img_label").classList.add("display_none");
    document.querySelector("#file").style.height = "auto";
};
    
// выполнение функции при выборки файла
document.querySelector("#id_img").addEventListener("change", loadImageFile);
    
// функция выборки файла
function loadImageFile() {
    var file = document.querySelector("#id_img").files[0];
    FReader.readAsDataURL(file);
}