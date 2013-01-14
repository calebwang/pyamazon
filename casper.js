var url = 'https://www.amazon.com';
var casper = require('casper').create();

casper.userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11");

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

    document.querySelector('#ap_email').value = 'calebd.wang@gmail.com';
    document.querySelector('#ap_password').value = 'hunter2';
    // document.querySelector('#signInSubmit').click();
    document.querySelector('#ap_signin_form').submit();

});

casper.then(function() {
    this.echo(this.getCurrentUrl());
    this.capture('4.png');
});

casper.run();
