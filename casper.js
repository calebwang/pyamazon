var url = 'https://www.amazon.com';
var casper = require('casper').create();

phantom.cookiesEnabled = true;

casper.start(url, function(){
    this.echo(this.getCurrentUrl());
    this.capture('1.png');
});

casper.thenEvaluate(function() {
    document.querySelector('#twotabsearchtextbox').value = 'hi';
    document.querySelector('form[name="site-search"]').submit()
});

casper.then(function() {
    this.echo(this.getCurrentUrl());
    this.capture('2.png');
    this.clickLabel('sign in');
});

casper.thenEvaluate(function() {

    document.querySelector('#ap_email').value = 'my_email';
    document.querySelector('#ap_password').value = 'my_email';
    // document.querySelector('#signInSubmit').click();
    document.querySelector('#ap_signin_form').submit();

});

casper.then(function() {
    this.echo(this.getCurrentUrl());
    this.capture('4.png');
});

casper.run();
