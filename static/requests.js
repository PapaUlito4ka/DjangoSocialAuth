function sendBroMessage(userId) {
    userId = parseInt(userId);
    let data = {
        'text': 'Bro!',
        'user_id': userId
    };

    $.ajax({
        url: `https://agile-sands-61045.herokuapp.com/api/messages/send`,
        type: 'POST',
        data: JSON.stringify(data),
        beforeSend: function(xhr){xhr.setRequestHeader('token', `django-insecure-v9kx#5*0pmdzw)tithibg(au*z6ii@oij5$bg1o+%)c5(+c1rf`);}
    });

}

function sendSisMessage(userId) {
    userId = parseInt(userId);
    let data = {
        'text': 'Sis!',
        'user_id': userId
    };

    $.ajax({
        url: `https://agile-sands-61045.herokuapp.com/api/messages/send`,
        type: 'POST',
        data: JSON.stringify(data),
        beforeSend: function(xhr){xhr.setRequestHeader('token', `django-insecure-v9kx#5*0pmdzw)tithibg(au*z6ii@oij5$bg1o+%)c5(+c1rf`);}
    });

}

