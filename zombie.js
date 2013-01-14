var Browser = require('zombie');

br = new Browser();

br
    .visit('https://www.amazon.com')
    .then(function() {
        br.pressButton('sign in');
    })
    .then(function() {
        br.fill('#ap_email', 'calebd.wang@gmail.com');
        br.fill('#ap_password', 'hunter2');
        br.pressButton('#signInSubmit');
    })
    

