function execute(){
    Swal.fire({
    title: 'Залиште заявку на замовлення',
    html:
        '<form method="POST" class="order_form">'+
                        {{ form.as_p }}+
                        {% csrf_token %}+
                        '<p class="order_p">Телефон у вигляді +380xxxxxxxxx</p>'+
            '<button class="order_btn order_button">Відправити</button>'+
        '</form>',
    focusConfirm: false,
    showConfirmButton:false,
})};
