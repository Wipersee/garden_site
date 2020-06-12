function execute(){
    Swal.fire({
    title: 'Залиште заявку на замовлення',
    html:
        '<form method="POST" class="order_form">'+
            '<input type="text" placeholder="Ім\'я" class="order_form-name">'+
            '<input type="tel" placeholder="Телефон" class="order_form-phone">'+
            '<button class="order_btn order_button">Відправити</button>'+
        '</form>',
    focusConfirm: false,
    showConfirmButton:false,
})};
