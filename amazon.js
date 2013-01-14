var url = 'https://www.amazon.com';
var casper = require('casper').create();

casper.start(url, function(){
    this.echo(this.getCurrentUrl());
    this.capture('1.png');
    this.clickLabel('sign in');
});

casper.then(function() {
    this.echo(this.getCurrentUrl());
    this.capture('2.png');
    this.fill('form#ap_signin_form', { email: 'my_email',
                                       password: 'my_password' }, true);
    this.capture('3.png');
});

casper.run();
